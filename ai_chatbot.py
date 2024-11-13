# File: ai_chatbot.py

import openai

# Configure OpenAI API key
openai.api_key = 'your_openai_api_key'

def chat_with_ai():
    """Simple AI chatbot using OpenAI API."""
    print("AI Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_input,
                max_tokens=150
            )
            print("AI:", response.choices[0].text.strip())
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    chat_with_ai()
