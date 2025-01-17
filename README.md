How to run the program.
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
      
        
