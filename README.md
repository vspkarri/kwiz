# KWIZ - AI-Powered Quiz Generation Platform

## Overview

**KWIZ** is a powerful, AI-driven platform designed to generate customizable quizzes across various topics, subjects, and grade levels. With KWIZ, users can easily create quizzes tailored to their specific needs by selecting the number of questions, difficulty level, and other parameters. The platform leverages advanced AI models, including OpenAI's GPT and LLaMA, to generate high-quality questions and explanations. Additionally, users can export quizzes to PDF format for printing and offline use.

## Features

- **Customizable Quizzes:** Generate quizzes by selecting topics, subjects, grade levels, and the number of questions.
- **AI-Driven Question Generation:** Uses AI models like GPT and LLaMA to create relevant and contextually accurate questions and explanations.
- **Difficulty Level Adjustment:** Set the rigor of the quiz according to the target audience.
- **PDF Export:** Download and print quizzes in a neatly formatted PDF.
- **User-Friendly Interface:** Developed with Streamlit, the platform provides an intuitive and responsive user experience.

## Technologies Used

- **Python:** Core programming language for developing backend logic.
- **Streamlit:** Framework for building the web interface.
- **OpenAI GPT & LLaMA:** AI models for generating quiz content.
- **FPDF:** Library for exporting quizzes to PDF format.
- **APIs:** For communication between frontend, backend, and AI models.
- **JSON:** Data format used for data exchange between components.

## System Requirements

### For Development

- **Operating System:** Windows 10 or later, macOS 10.14 or later, or a modern Linux distribution.
- **Processor:** Dual-core processor (Intel Core i5 or equivalent) minimum; Quad-core recommended.
- **Memory:** 8 GB RAM minimum; 16 GB recommended.
- **Storage:** 256 GB SSD minimum; 512 GB recommended.
- **Development Tools:** Python 3.7 or later, PyCharm, Streamlit, Git, Node.js (if needed).

### For Users

- **Operating System:** Windows 7 or later, macOS 10.12 or later, or any modern Linux distribution.
- **Processor:** Dual-core processor (Intel Core i3 or equivalent) minimum.
- **Memory:** 4 GB RAM minimum; 8 GB recommended.
- **Web Browser:** Latest version of Chrome, Firefox, Safari, or Edge.
- **Internet Connection:** Stable broadband (1 Mbps or higher).
- **PDF Reader:** Required to view exported quizzes.

## Installation

### Prerequisites

- Python 3.7 or later
- Git (for cloning the repository)
- Virtual environment tools (optional but recommended)

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/kwiz.git
   cd kwiz
   ```

2. **Create and Activate a Virtual Environment (Optional):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

5. **Access the Platform:**
   Open your web browser and go to `http://localhost:8501` to start using KWIZ.

## Usage

1. **Launch the platform** by running the application as described in the installation steps.
2. **Select your preferences** such as topic, subject, grade level, number of questions, and difficulty level.
3. **Generate the quiz** by clicking the "Generate Quiz" button.
4. **Review the quiz** and, if satisfied, export it to PDF using the provided option.
5. **Download the PDF** to save or print the quiz for offline use.

## Testing

### Running Unit Tests

1. **Navigate to the Project Directory:**
   ```bash
   cd kwiz
   ```

2. **Run the Tests:**
   ```bash
   pytest
   ```

   Ensure all tests pass before deploying or making further changes.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your branch to your forked repository.
5. Open a Pull Request to the main repository.

Please ensure your contributions follow the project's coding standards and pass all tests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions, issues, or suggestions, please open an issue in the GitHub repository or contact the project maintainers directly.

---

Thank you for using KWIZ! We hope this platform helps you create effective and engaging quizzes with ease.
