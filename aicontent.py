import os
import openai
import config

openai.api_key = config.OPENAI_API_KEY

def productDescription(query):
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"Generate a detailed product description for: {query}\n",
    temperature=0.5,
    max_tokens=400,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    answer = response['choices'][0]['text']
    return answer

def blogArticle(query):
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"Generate a Blog Article for: {query}\n",
    temperature=0.5,
    max_tokens=400,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    answer = response['choices'][0]['text']
    return answer

def coldEmail(query):
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"Write a cold email to potential client about: {query}\n",
    temperature=0.5,
    max_tokens=400,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    answer = response['choices'][0]['text']
    return answer

