
import vector
from openai import OpenAI


# Initialize the client with your API key
def generate(data, user_question):
    i = 0
    text = "ok"
    message = [
        {"role": "system", "content": "You are a SQL finder. Pull the sql tables that have to do with the users question."}, 
        {"role": "user", "content": "Question: " + user_question + " Data: Table: " + data}
    ]
    
    while text != "done":
        client = OpenAI(api_key="Your API KEY goes here")
        if i > 0:
            text = input("Enter feedback for the agent or enter 'done': \n")
            message.append({"role": "user", "content": text})

        completion = client.chat.completions.create(
            model="ft:gpt-4o-mini-2024-07-18:splashbi:create-query1:AXrti2YQ",
            messages=message
        )
        
        message.append({"role": "assistant", "content": completion.choices[0].message.content})

        print(completion.choices[0].message.content)
        i += 1


# def generate_query():
#     print("hi")





if __name__ == "__main__":
    collection_name = "new_collection"
    client = vector.embeddedModel(collection_name)
    user, arr = vector.ask_agent(client, collection_name)
    data = ", ".join(arr)
    print(data)
    print(user)
    generate(data, user)
#     print(generate_query())
