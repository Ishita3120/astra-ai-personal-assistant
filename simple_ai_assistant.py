from openai import OpenAI
from dotenv import load_dotenv
import os 
from tools import TOOLS,FUNCTION_NAME_TO_FUNCTION_MAP
import json
load_dotenv()
#call the load_env method by default looks for .env file(load_env method )
client=OpenAI(
    base_url=os.getenv("BASE_URL"), #we ran the ollama by running the command ollama serve
    api_key=os.getenv("API_KEY"),
    
)
messages=[]
messages.append({
    "role":"system",
    "content":"Act like a very humble agent and respond always under 20 words."
})

while True:
    user_input = input("\nIshita: ")
    if user_input.lower() in ["exit", "quit","bye","goodbye"]:
        break
    messages.append({
        "role":"user",
        "content":user_input
    })
#this is the first tool call
# isko repeat rna hai jb tak llm assistant se bol rha krne so put in while loop
    
  #this is chained tool calling
    for step in range(MAX_STEPS):
        
        response=client.chat.completions.create(
                model=os.getenv("MODEL"),
                messages=messages,
                tools=TOOLS
        )
        msg=response.choices[0].message
        messages.append(msg)
        if not msg.tool_calls:
            break
        
        for tool_call in msg.tool_calls:
            func_name=tool_call.function.name

            try:
                func_args=json.loads(tool_call.function.arguments or "{}")
                fn=FUNCTION_NAME_TO_FUNCTION_MAP[func_name]
                result=fn(**func_args)
            except Exception as e:
                result=f"Error while running{func_name}: {str(e)}"
            messages.append({
                    "role":"tool",
                    "tool_call_id":tool_call.id,
                    "content":str(result)   
                        }
                            
                        )
        msg=response.choices[0].message
        messages.append({
                "role":"assistant",
                "content":msg.content
            })
    else:
        #we ran out of the steps :the model never gave the final answer
        fallback="Sorry,I could not finish this within the given limit"
        messages.append({
            "role":"assistant",
            "content":fallback

        })
        print("Assistant:"+fallback)
        #ye above statement ko aap is line se bhi change kr skte ho
        #messages.append(msg)->this will be used to preserve the msg structure
        

    print("Assistant:"+msg.content)
