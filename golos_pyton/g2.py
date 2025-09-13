import os

from groq import Groq
client = Groq(api_key="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")

def generate(prompt):
    

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.1-8b-instant",
    )

    return chat_completion.choices[0].message.content
#pp = input("запитай:")
#print(generate(pp))