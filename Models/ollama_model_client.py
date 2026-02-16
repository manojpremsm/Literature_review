from autogen_ext.models.ollama import OllamaChatCompletionClient

def ollama_model_client():

    return OllamaChatCompletionClient(model="llama3.2")