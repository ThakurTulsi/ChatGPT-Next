import os
import openai 


os.environ["OPENAI_API_KEY"] = "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"

openai.api_key = os.environ["OPENAI_API_KEY"]

# Define a flag to control the loop
keep_prompting = True

while keep_prompting:
    # get prompt from the user
    prompt = input('What is your question? (Type exit if Done): ')
    if prompt == 'exit':
        keep_prompting = False
    else:
        # generate text
        response = openai.Completion.create(
            engine = "text-davinci-002",
            prompt=prompt,
            max_tokens=200
        ) 

        # print the generated text

        print(response["choices"][0]["text"])