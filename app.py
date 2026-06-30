import streamlit as st
from groq import Groq


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

    if code.strip() == "":
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

            client = Groq(
                api_key=st.secrets["GROQ_API_KEY"]
            )


            response = client.chat.completions.create(

                model="llama-3.1-8b-instant",

                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]

            )


            answer = response.choices[0].message.content


            st.subheader("🤖 AI Analysis")

            st.write(answer)


        except Exception as e:

            st.error(
                "API connection error. Check your GROQ API key."
            )

            st.write(e)