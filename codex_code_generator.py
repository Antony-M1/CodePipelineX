import os
import openai
from dotenv import load_dotenv
load_dotenv()

print(f"Open API key: {os.environ.get('OPENAI_API_KEY')}")
openai.api_key = os.environ.get('OPENAI_API_KEY')
model_name = os.environ.get('MODEL_NAME', "gpt-3.5-turbo-instruct")
print(f"API Key: {openai.api_key}")


def generate_code(prompt: str, **kwargs) -> str:
    """
        Generate code based on the given prompt
    """

    response = openai.completions.create(
        model=model_name,
        prompt=prompt,
        temperature=kwargs.get('temperature', 0.2),
        max_tokens=kwargs.get('max_tokens', 300),
        n=kwargs.get('n', 1),
        stop=kwargs.get('stop', None)
    )
    return response.choices[0].text.strip()


if __name__ == '__main__':
    prompt = "Generate a Python function that sorts a list of numbers using\
        bubble sort."
    print(prompt)
    # generated_code = generate_code(prompt)
    # print(generated_code)
