# Project RAG
## Project Description
This project is to use an OpenAI model to vector search using RAG. This project uses openAI model text-embedding-ada-002 for the embedding model and chatgpt-4o for the llm. In vector.py, there are two functions. 

    def embeddedModel(name):
    Parameters: Name - name of the vector store. 
    This function takes a file and embeddeds each line into a vector space using the chromadb library as the vector store. The function returns the client that stores the vector store.

    def ask_agent(client, name):
    Parameters: Client - the vector store returned from embeddedModel(Name), Name - name of the vector store
    This function prompts the user for a query. It then embeddes the query and does a RAG vector search on the vectore database. It will return the most likely related lines from the vector store as an array and the users query.

In generate_sql_query.py there is one function 

    def generate(data, user_question): Parameters: data - a string version of the array that was returned in ask_agent, user_querstion - the users query from ask_agent
    This function formulates a response based off the users query and the data provided from the rag. It first creates a memory array to store the conversation between the agent and the user. This is used for feedback to the agent. It then creates an openAI client to call the model. The function prints the response and enters a feedback loop. If you are happy with the response you can enter "done" to exit the loop. 
    

    

## How to run the program.

**Setting up API Key**
  Go to openAI 
  https://auth.openai.com/authorize?audience=https%3A%2F%2Fapi.openai.com%2Fv1&auth0Client=eyJuYW1lIjoiYXV0aDAtc3BhLWpzIiwidmVyc2lvbiI6IjEuMjEuMCJ9&client_id=DRivsnm2Mu42T3KOpqdtwB3NYviHYzwD&device_id=d9c70e31-21b0-4977-8358-e6b1a50a0df9&ext-login-allow-phone=true&ext-use-new-phone-ui=true&issuer=https%3A%2F%2Fauth.openai.com&max_age=0&nonce=OWNCZURZSERfSUJYSWtCTy1CeUstQUo2VEJYSjlpdkd0QmVMQk4wZEtmNA%3D%3D&redirect_uri=https%3A%2F%2Fplatform.openai.com%2Fauth%2Fcallback&response_mode=query&response_type=code&scope=openid+profile+email+offline_access&state=Smg5blpBNlZQRXhYSTh2dk00V1ZXX0xPQUg1ZjNBdnR%2BWGpORlZLVVlfZQ%3D%3D&flow=treatment
  
  Create an account
  
  Click on your profile pic in the top right corner
  
  Click on 'your profile'
  
  Under the Organization tab on the right side press API keys
  
  Create an API key, Make sure you save the key because you will not be shown the key again.


  **Running the code**
  
  Clone the git repository in your IDE
  
  Pip install the appropriate libraries on terminal
  
      pip install langchain-openai chromadb openai
  
  Replace 'Your API KEY goes here' with your API key in vector.py line 5 and generate_sql_query.py line 16
  
  Run the code from generate_sql_query.py
      
        
