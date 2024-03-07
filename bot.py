from openai import OpenAI

client = OpenAI(api_key='') 
messages = [ {"role": "system", "content":  
              "You are a intelligent assistant."} ] 
while True: 
    message = """	given this data when shsould i buy and sell? 
                  Time        Open        High         Low       Close  Volume
0  2024-03-04 09:00:00  100.000000  100.105712   99.815050  100.105712    9068
1  2024-03-04 09:05:00  100.248357  100.282719  100.106584  100.282719   10483
2  2024-03-04 09:10:00  100.179225  100.301409  100.002921  100.002921    6173
11 2024-03-04 09:55:00  102.008597  102.273106  102.000724  102.041723   10135"""
    if message: 
        messages.append( 
            {"role": "user", "content": message}, 
        ) 
        chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages) 
    reply = chat.choices[0].message.content 
    print(f"ChatGPT: {reply}") 
    messages.append({"role": "assistant", "content": reply}) 
