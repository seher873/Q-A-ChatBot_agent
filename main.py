import chainlit as cl
import os
import google.generativeai as genai

# Gemini API configuration
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY") or "YOUR_GEMINI_API_KEY_HERE"
genai.configure(api_key=GOOGLE_API_KEY)

# Using Gemini Flash 2.0 model
model = genai.GenerativeModel("gemini-2.0-flash")

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="👋 Hello! How can I assist you today?").send()

@cl.on_message
async def on_message(message: cl.Message):
    try:
        response = model.generate_content(message.content)
        if hasattr(response, "text"):
            await cl.Message(content=response.text).send()
        else:
            await cl.Message(content="❌ Sorry, I couldn't generate a response.").send()
    except Exception as e:
        await cl.Message(content=f"⚠️ An error occurred: {str(e)}").send()
