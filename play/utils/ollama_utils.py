import ollama

def get_response(prompt, model='llama2'):
    response = ollama.generate(model=model, prompt=prompt)
    return response['response']
