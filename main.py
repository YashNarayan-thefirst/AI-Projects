import openai
import sys

# Replace 'your_api_key' with your actual API key
openai.api_key = "your_api_key"

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4095,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

def main():
    if len(sys.argv) < 2:
        print("Usage: python code_debugger.py <code_snippet>")
        sys.exit(1)

    code_snippet = sys.argv[1]
    prompt = f"Debug the following Python code snippet: ```python\n{code_snippet}\n```\n"
    debug_output = chat_with_gpt(prompt)
    print(f"Debug output:\n{debug_output}")

if __name__ == "__main__":
    main()
