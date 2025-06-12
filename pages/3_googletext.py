
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

models = genai.list_models()

for model in models:
    print(f"{model.name} - {'✅' if 'generateContent' in model.supported_generation_methods else '❌'} supports generateContent")
