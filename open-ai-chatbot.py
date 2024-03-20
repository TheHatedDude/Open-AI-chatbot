import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key'

def ask_openai(question):
    response = openai.Completion.create(
        engine="davinci",
        prompt=question,
        temperature=0.5,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def main():
    print("Welcome to the OpenAI Chatbot!")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        response = ask_openai(user_input)
        print("OpenAI: ", response)

if __name__ == "__main__":
    main()
