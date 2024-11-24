import openai
from dotenv import find_dotenv, load_dotenv
import time
import logging
from datetime import datetime

# === Environment Setup ===
load_dotenv()

# === OpenAI API Client Configuration ===
client = openai.OpenAI()
model = "gpt-4o-mini"