from langchain_openai import OpenAIEmbeddings
from chromadb import Client
from chromadb.config import Settings
from AIkey import get_API_KEY

key = get_API_KEY()
embeddings_model = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=key)


def embeddedModel(name):
    # Open file and read lines
    with open("SQLData", "r") as file:
        lines = file.readlines()
    
    # Set the OpenAI API key directly
    embeddings = embeddings_model.embed_documents(lines)
    
    # Initialize Chroma client and create a collection
    client = Client(Settings(persist_directory="./chroma_db"))
    collection = client.create_collection(name)
    
    # Add lines and embeddings to the collection
    for i, (lin, embedding) in enumerate(zip(lines, embeddings)):
        collection.add(
            documents=[lin],
            embeddings=[embedding],
            ids=[f"id_{i}"]
        )
    return client
    

def ask_agent(client, name):
    # Query the collection
    query = input("Enter a Question")
    query_embedding = embeddings_model.embed_query(query)
    collection = client.get_collection(name)


    # n_results is how many results it will return
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    arr = list()
    # Display results
    for doc in results['documents'][0]:
        arr.append(doc)
    return query, arr

