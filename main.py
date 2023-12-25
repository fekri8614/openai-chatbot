import openai

# Set your OpenAI API key here
openai.api_key = ''


def get_openai_response(prompt):
    # Use the OpenAI API to generate a response based on the given prompt
    response = openai.Completion.create(
        engine="davinci-codex",  # You can also try "text-davinci-003" or other engines
        prompt=prompt,
        temperature=0.7,
        max_tokens=150
    )

    # Extract the generated text from the API response
    reply = response['choices'][0]['text'].strip()
    return reply


def main():
    print("Chatbot: Hello! I'm your chatbot. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        # Generate a response using OpenAI API
        prompt = f"You: {user_input}\nChatbot:"
        chatbot_response = get_openai_response(prompt)

        print("Chatbot:", chatbot_response)


if __name__ == "__main__":
    main()
