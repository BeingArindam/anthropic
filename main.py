from dotenv import load_dotenv
import os
from anthropic import Anthropic

load_dotenv()

def add_user_message(messages, content):
    messages.append({"role": "user", "content": content})

def add_assistant_message(messages, content):
    messages.append({"role": "assistant", "content": content})

def chat_with_model(client, messages):
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=messages
    )
    return response.content[0].text

def main():
    api_key = os.getenv("ANTHROPIC_API_KEY")
    client = Anthropic(api_key=api_key)
    messages = []
    add_user_message(messages, "What is the LLM? answer in 2 lines")
    answer = chat_with_model(client, messages)
    print(answer)
    print("\n\n")
    # include assistant reply in history to maintain multi-turn context
    add_assistant_message(messages, answer)
    add_user_message(messages, "Write another answer to the same question")
    answer = chat_with_model(client, messages)
    print(answer)
    

if __name__ == "__main__":
    main()