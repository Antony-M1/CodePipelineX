import os
import openai
from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.environ.get('OPENAI_API_KEY')
model_name = os.environ.get('MODEL_NAME', "gpt-3.5-turbo-instruct")


TEST_V1 = os.environ.get('TEST_V1')
TEST_S1 = os.environ.get('TEST_S1')


class OpenAIAPIKeyNotFound(Exception):
    pass


class BothTestVailed(Exception):
    pass

class TEST_V1_NotFound(Exception):
    pass

class TEST_S1_NotFound(Exception):
    pass

if not TEST_V1 and not TEST_S1:
    raise BothTestVailed
elif TEST_V1 and not TEST_S1:
    raise TEST_V1_NotFound
elif not TEST_V1 and TEST_S1:
    raise TEST_S1_NotFound

if not openai.api_key:
    raise OpenAIAPIKeyNotFound


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
    generated_code = generate_code(prompt)
    print(generated_code)
 