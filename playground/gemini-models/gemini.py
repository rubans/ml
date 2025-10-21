import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
  vertexai=True, project=os.environ.get("GOOGLE_CLOUD_PROJECT"), location="global",
)
# If your image is stored in Google Cloud Storage, you can use the from_uri class method to create a Part object.
# You will need to define IMAGE_URI for this script to run.
model = "gemini-2.5-flash"
print("setup...")
response = client.models.generate_content(
  model=model,
  contents=[
    "How are you?",
  ],
)
print(response.text, end="")
print("done..")