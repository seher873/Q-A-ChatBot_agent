import os
from dotenv import load_dotenv
from typing import cast
import chainlit as cl

# Load environment variables from .env
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Raise error if API key is not set
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Agent class definition
class Agent:
    def __init__(self, name: str, instructions: str, model):
        self.name = name
        self.instructions = instructions
        self.model = model

# AsyncOpenAI class definition
class AsyncOpenAI:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

# OpenAIChatCompletionsModel class definition
class OpenAIChatCompletionsModel:
    def __init__(self, model: str, openai_client: AsyncOpenAI):
        self.model = model
        self.client = openai_client

# RunConfig class definition
class RunConfig:
    def __init__(self, model, model_provider, tracing_disabled=True):
        self.model = model
        self.model_provider = model_provider
        self.tracing_disabled = tracing_disabled

# Runner class definition
class Runner:
    @staticmethod
    def run_sync(starting_agent, input, run_config):
        # Simulate AI response for now
        return type("Result", (), {"final_output": "This is a dummy response."})()

# Chat start handler
@cl.on_chat_start
async def start():
    external_client = AsyncOpenAI(
        api_key=gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=external_client
    )

    config = RunConfig(
        model=model,
        model_provider=external_client,
        tracing_disabled=True
    )
    cl.user_session.set("config", config)

    agent: Agent = Agent(name="Q/A chatbot", instructions="You are a helpful chat bot.", model=model)
    cl.user_session.set("agent", agent)

    await cl.Message(content="Welcome to the general question and answer AI Assistant! How can I help you today?").send()

# Message handler
@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content="Thinking...")
    await msg.send()

    agent: Agent = cast(Agent, cl.user_session.get("agent"))
    config: RunConfig = cast(RunConfig, cl.user_session.get("config"))
    history = cl.user_session.get("chat_history") or []
    history.append({"role": "user", "content": message.content})

    try:
        print("\n[CALLING_AGENT_WITH_CONTEXT]\n", history, "\n")
        result = Runner.run_sync(
            starting_agent=agent,
            input=history,
            run_config=config
        )
        msg.content = result.final_output
        await msg.update()

        print(f"User: {message.content}")
        print(f"Assistant: {msg.content}")

    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
        print(f"Error: {str(e)}")
