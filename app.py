import streamlit as st
import ollama


st.set_page_config(
    page_title="AI Code Error Analyzer",
    page_icon="🤖"
)


st.title("🤖 AI Code Error Analyzer")
st.write("AI detects programming errors and provides corrections")


# Supported languages

languages = [
    "Python",
    "Java",
    "JavaScript",
    "C",
    "C++",
    "C#",
    "Go",
    "Rust",
    "PHP",
    "SQL",
    "HTML/CSS"
]


language = st.selectbox(
    "Choose Programming Language",
    languages
)


code = st.text_area(
    "Paste your code here",
    height=350
)


if st.button("Analyze Code"):

    if code == "":
        st.warning("Please enter code")

    else:

        prompt = f"""
You are an expert AI programming debugger.

Programming Language:
{language}


Analyze the given code.

Find:
- Syntax errors
- Runtime errors
- Logical errors
- Exact line number of the mistake
- Explanation of the error
- Correct solution
- Fixed code


Response format:

Error:
Line Number:

Explanation:

Correction:

Fixed Code:


Code:

{code}

"""


        try:

            result = ollama.chat(
                model="llama3",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )


            answer = result["message"]["content"]


            st.subheader("AI Analysis")

            st.write(answer)


        except Exception as e:

            st.error(
                "Ollama connection error. Make sure Ollama is running."
            )

            st.write(e)