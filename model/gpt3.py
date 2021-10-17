import os
import openai

openai.api_key = os.getenv("GPT3KEY")


def generate(sentence, max_tokens=1000):
    response = openai.Completion.create(engine="davinci",
                                        prompt=sentence,
                                        max_tokens=max_tokens,
                                        temperature=0.95)
    print(response.choices[0].text)
