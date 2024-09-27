from openai import OpenAI

prompt = []
client = OpenAI(api_key="chave")

def addInfo(comments):        
        prompt.append({"role":"user", "content": comments})
        openIa(prompt)

def openIa(prompt):
    response = client.chat.completions.create(
    messages = prompt,
    model = "gpt-3.5-turbo-0125",
    max_tokens = 1000,
    temperature = 1
    )
    prompt.append({"role":"assistant","content":response.choices[0].message.content})
