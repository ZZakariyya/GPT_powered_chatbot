import chainlit as cl
import openai
import os

openai.api_key = 'your api_key'

@cl.on_message
async def on_message(message: str):
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {"role":"assistant", "content":"You are helpful assistant"},
            {"role":"user", "content":message}
        ],
        temperature = 1,
    )
    await cl.Message(content=response['choices'][0]['message']['content']).send()
