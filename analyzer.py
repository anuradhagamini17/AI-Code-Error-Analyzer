import ollama


def analyze_code(code, language, error):

    prompt = f"""

You are an expert software debugger.

Analyze and FIX the given code.

Programming Language:
{language}


CODE:
----------------
{code}
----------------


ERROR MESSAGE:
----------------
{error}
----------------


Your response MUST follow this exact format:


## Error Found
Mention the exact line number and error.


## Reason
Explain why this error happened.


## Corrected Code
IMPORTANT:
Provide the FULL corrected code.
Do not give only snippets.
Do not use placeholders.
The code must be ready to run.


## Explanation
Explain what changes you made.


Rules:
- Always return corrected code.
- Keep the original logic.
- Only fix the mistakes.
- Make sure corrected code has proper syntax.
"""

    response = ollama.chat(
        model="qwen2.5-coder",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature":0.1
        }
    )

    return response["message"]["content"]