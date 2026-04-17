import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_logs(errors):
    text = "\n".join(errors)

    prompt = f"""
    Analyze the following system logs.

    Identify:
    - Root cause
    - Type of errors
    - Suggested fixes

    Logs:
    {text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']
