import os
import openai
import config

openai.api_key = config.OPENAI_API_KEY


blogIdeas = openai.Completion.create(
    engine = 'davinci-instruct-beta-v3',
    prompt = 'Blog ideas on The best uses of CRM software in Small Business Operations',
    temprature = 0.7,
    max_token = 100,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0
    )

blogIdeas = openai.Completion.create(
    engine = 'davinci-instruct-beta-v3',
    prompt = 'Write a blog section on the following topic. /n Title: How to use CRM software to manage you client information',
    temprature = 0.5,
    max_token = 200,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0
    )