# pip install openai
from openai import OpenAI

OPENAI_API_KEY = "Your OPENAI Key"

client = OpenAI(
    # This is the default and can be omitted
    api_key=OPENAI_API_KEY,
)


# openai.ChatCompletion is out of date
def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit"]:
            break
        response = chat_with_gpt(user_input)
        print("ChatBot: ", response)
