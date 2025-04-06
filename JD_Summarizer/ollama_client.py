import ollama

class OllamaClient:
    def __init__(self, model_name="llama3.2:1b"):
        self.model = model_name

    def generate(self, prompt, max_tokens=500):
        try:
            response = ollama.chat(
                model=self.model,
                messages=[{"role": "user", "content": prompt}]
            )
            if response and "message" in response and "content" in response["message"]:
                return response["message"]["content"]
            else:
                print("Unexpected response format from Ollama")
                return ""
        except Exception as e:
            print(f"Error calling Ollama: {str(e)}")
            return ""