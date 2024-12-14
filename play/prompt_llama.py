from utils.ollama_utils import get_response

if __name__ == "__main__":
    response = get_response(prompt='What are the 48 laws of power?')
    print(response)