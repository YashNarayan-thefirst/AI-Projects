from flask import Flask, request
import openai

openai.api_key = "Your Key"

app = Flask(__name__)


@app.route('/debug', methods=['POST'])
def debug():
    code = request.form.get('code')

    if not code:
        return "Error: Code not found in request"

    prompt = f"Debug the following code: \n\n{code}\n\nThe debugged code is:"
    try:
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=prompt,
            temperature=0.5,
            max_tokens=100,
            n=1,
            stop=None
        )
    except Exception as e:
        return f"Error: {e}"

    debugged_code = response.choices[0].text.strip()

    return debugged_code


if __name__ == '__main__':
    app.run()
