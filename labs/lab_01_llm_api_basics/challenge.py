import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key without displaying its value

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if OPENROUTER_API_KEY:
    print("OpenRouter API key detected")
else:
    print("..What're you looking for???")

# Configure which API provider we want to contact

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# Ask OpenRouter to select an available free model

MODEL = "openrouter/free"  #this isnt the model, its the model-routing option we want to request

# Construct the API client

openrouter = OpenAI(  #client oject created
    api_key=OPENROUTER_API_KEY,
    base_url=OPENROUTER_BASE_URL, 
    timeout=120,
    max_retries=5
)

message = [
    {"role": "user", "content": "In one sentence, can you explain what is an API?"}
]

response = openrouter.chat.completions.create(
    model=MODEL,
    messages=message
)

# Show which model responded
print("Model:", response.model)

# Show the generated message
# print("Response:", response.choices[0].message.content)

if response.choices:
    print(response.choices[0].message.content)
else:
    print("No choices returned")