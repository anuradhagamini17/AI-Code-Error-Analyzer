from groq import Groq
import os


client = Groq(
    api_key=os.environ["GROQ_API_KEY"]
)


def analyze_code(code, language, error):

    prompt = f"""
You are an expert code debugger.

Language:
{language}

Code:
{code}

Error:
{error}

Return exactly:

## Error Found
Give exact line number.

## Reason
Explain the mistake.

## Corrected Code
Give the full corrected code.

## Explanation
Explain the fix.

Always provide complete corrected code.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content