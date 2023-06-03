import openai
import gradio
from os import getenv

#openai.api_key = getenv('OPEN_AI_KEY')
#openai.api_key = "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"
openai.api_key = "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"

def openai_chat_plugin(query):
    completions = openai.Completion.create(
                        model="text-ada-001",
                        prompt=query,
                        temperature=0.7,
                        max_tokens=100,
                        n=1,
                    )

    message = completions.choices[0].text
    return message.strip()

def chatbot(input, history=[]):
    output = openai_chat_plugin(input)
    history.append((input,output))
    return history, history

gradio.Interface(
    fn=chatbot,
    inputs=["text","state"],
    outputs=["chatbot","state"]
).launch(debug=True)