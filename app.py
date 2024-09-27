from bs4 import BeautifulSoup
import json
import streamlit as st


# Function to parse the HTML and extract quiz data
def parse_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    quiz_data = []

    questions = soup.find_all("h3", class_="new-heading")

    for question_heading in questions:
        question_text = question_heading.find_next(
            "p", class_="quiz-question"
        ).text.strip()
        choices_table = question_heading.find_next("table", class_="compact-form")
        choices = []
        for row in choices_table.find_all("tr"):
            label = row.find("label", {"for": True})
            if label:
                choices.append(label.text.strip())
        quiz_data.append({"question": question_text, "choices": choices})

    return quiz_data


# Streamlit UI components
html_content = st.text_area("Input HTML")

if st.button("Parse HTML"):
    quiz_data = parse_html(html_content)
    st.code(json.dumps(quiz_data, indent=4), language="json")
