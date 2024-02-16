import openai
#pip install openai

openai.api_key = "API KEY"


#openai.ChatCompletion is out of date
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="curie",
        prompt=prompt,
        max_tokens=150
    )

    return response.choices[0].text.strip()


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit"]:
            break
        response = chat_with_gpt(user_input)
        print("ChatBot: ", response)


'''
Traceback (most recent call last):
  File "c:\Users\HARI\Desktop\Miniworks\ChatGPT_basic.py", line 23, in <module>
    response = chat_with_gpt(user_input)
               ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\HARI\Desktop\Miniworks\ChatGPT_basic.py", line 9, in chat_with_gpt
    response = openai.Completion.create(
               ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\HARI\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\openai\lib\_old_api.py", line 39, in __call__
    raise APIRemovedInV1(symbol=self._symbol)
openai.lib._old_api.APIRemovedInV1:

You tried to access openai.Completion, but this is no longer supported in openai>=1.0.0 - see the README at https://github.com/openai/openai-python for the API.

You can run `openai migrate` to automatically upgrade your codebase to use the 1.0.0 interface.

Alternatively, you can pin your installation to the old version, e.g. `pip install openai==0.28`

A detailed migration guide is available here: https://github.com/openai/openai-python/discussions/742
'''