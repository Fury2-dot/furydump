import openai

# Initialize the OpenAI API with your API key
openai.api_key = 'your-openai-api-key'

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        response = generate_response(user_input)
        print(f"JARVIS: {response}")