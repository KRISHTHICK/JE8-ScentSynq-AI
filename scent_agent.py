import subprocess

def chat_with_agent(prompt):
    user_input = f"Suggest a custom scent or perfume idea for: {prompt}"
    result = subprocess.run(["ollama", "run", "tinyllama", user_input], capture_output=True, text=True)
    return result.stdout.strip()
