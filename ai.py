import openai
import os
import pandas as pd
import time

def chatgpt():
    #set up your api key
    openai.api_key = '<YOUR API KEY>'

    prompt = input("Enter the question you want to ask to chatGPT: ")
    messages = [{"role": "user", "content": prompt}]
   
    # Make the API call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7  # You can adjust the temperature parameter
    )

    # Check if the API call was successful
    if response['choices'][0]['message']['content']:
        # Extract the generated answer
        answer = response['choices'][0]['message']['content']
        print(f"ChatGPT's answer: {answer}")
    else:
        print("Error in API response.")

if __name__ == "__main__":
    chatgpt()
