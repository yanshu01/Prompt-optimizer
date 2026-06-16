from ollama import chat
from prompt_engineer import optimize_prompt

user_prompt = input("Enter prompt: ")

optimized = optimize_prompt(user_prompt)

response = chat(
    model="phi3:mini",
    messages=[
        {
            "role":"user",
            "content":optimized
        }
    ]
)

print("\nOptimized Prompt:\n")
print(response["message"]["content"])