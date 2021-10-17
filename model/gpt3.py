import os
import openai

openai.api_key = os.getenv("GPT3KEY")


def generate(sentence, max_tokens=200):
    response = openai.Completion.create(engine="davinci", prompt="This is a test", max_tokens=max_tokens,
                                        temperature=0.95)
    print(response.choices[0].text)
