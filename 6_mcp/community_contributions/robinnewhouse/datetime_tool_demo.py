from agents import Agent, Runner
from agents.mcp import MCPServerStdio
import gradio as gr

params = {"command": "uv", "args": ["run", "datetime_mcp_server.py"]}

async def chat(message, history):
    # Convert Gradio history format to messages format
    messages = [{"role": m["role"], "content": m["content"]} for m in history] if history else []
    messages = messages + [{"role": "user", "content": message}]
    
    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as mcp_server:
        agent = Agent(
            name="datetime_agent",
            instructions="You are an agent that can return the current date and time using the get_datetime tool.",
            model="openai/gpt-4o-mini",
            mcp_servers=[mcp_server],
        )
        result = await Runner.run(agent, messages)
        return result.final_output

gr.ChatInterface(chat, type="messages").launch() 


