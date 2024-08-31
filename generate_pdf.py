from fpdf import FPDF
import base64

pdf = FPDF() #pdf object
#pdf = FPDF(orientation="P", unit="mm", format="Legal")
pdf.add_page()

pdf.set_font("Times", "B", 18)
pdf.set_xy(10.0, 20)
pdf.cell(w=75.0, h=5.0, align="L", txt="This is my sample text")

oflnme = "Output.pdf"
b64 = base64.b64encode(pdf.output("", dest="S")).decode()
st.download_button("Download Report", data=b64, file_name=oflnme, mime="application/octet-stream", help=f"Download file {oflnme}")

#alternatively, if I replace the above last 2 lines with the following 3 lines of code for a download hyperlink, it works fine.

b64 = base64.b64encode(pdf.output(dest="S"))
html = f'Download file'
st.markdown(html, unsafe_allow_html=True)