import os
import streamlit as st
from fpdf import FPDF
from openai import OpenAI

rigor_values = [1, 2, 3]
rigor_names = ["Beginner!", "Advanced!", "Expert!"]
api_key = os.getenv('API_KEY')
client = OpenAI(api_key=api_key)

keywords = ["generate", "quiz", "question", "create", "give"]


def rigor_string(i: int = 0) -> str:
    return rigor_names[i - 1]


def validate_message(msg):
    tokens = [a.lower() for a in msg.split(" ")]
    for token in tokens:
        if token in keywords:
            return True
    return False


st.title("Kwiz..!")
st.write("Welcome to Kwiz..! A Platform powered by AI to test your knowledge on various topics!")
no_of_questions = st.slider("Select number of questions", min_value=1, max_value=50)
rigor = st.select_slider("Select Rigor..!", options=rigor_values, format_func=rigor_string)
col = st.columns([0.5, 0.5],gap="small")
with col[0]:
    answers = st.checkbox("Answers")

with col[1]:
    explanation = st.checkbox("Explanation")


message = st.chat_input()


if message:
    if validate_message(message):
        prompt = f'{message} with {no_of_questions} question at {rigor} level with 4 choices'
        if answers and explanation:
            prompt = f'{message} with {no_of_questions} question at {rigor} level with 4 choices along with answers and explaination'
        elif answers and not explanation:
            prompt = f'{message} with {no_of_questions} question at {rigor} level with 4 choices along with answers and no explaination'
        elif explanation and not answers:
            prompt = f'{message} with {no_of_questions} question at {rigor} level with 4 choices along with explanation but no answers'
        else:
            prompt = f'{message} with {no_of_questions} question at {rigor} level with 4 choices with no explanation no answers'

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        content = response.choices[0].message.content
        pdf = FPDF(orientation="P", unit="mm", format="letter")
        pdf.add_page()
        pdf.add_font('Courier', '', fname='fonts/Courier.ttf', uni=True)
        pdf.set_font('Courier', '', 12)
        pdf.set_xy(10.0, 20)
        pdf.set_auto_page_break(False)
        pdf.multi_cell(w=75.0, h=5.0, align="L", txt=content)

        with st.expander(message, expanded=True):
            st.write(content)
            st.snow()
            st.download_button(
                "Download",
                data=pdf.output(name="Quiz.pdf", dest='S').encode('latin-1'),
                file_name="Quiz.pdf",
            )
    else:
        st.write("I did not get that! "
                 "I am designed to generate questions on various subjects at different levels of expertise. "
                 "Hint: You may ask like 'Give me a math quiz'. "
                 "Also, adjust the number of questions and select rigor using the slide bars above!")
