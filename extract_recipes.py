from huggingface_hub import InferenceClient
from langchain.prompts import ChatPromptTemplate
from langchain_core.prompt_values import PromptValue

from utils import config


def llm_invoke(prompt: PromptValue) -> str:
    """
    invoke llm with given prompt and return answer
    """
    # Step 1: Initialize Hugging Face API with a Model Endpoint
    client = InferenceClient(
        model="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
        token=config["api_key"]
    )

    # Step 2: Invoke LLM using the formatted prompt
    response = client.text_generation(prompt)

    # Step 3: process Response
    return response


if __name__ == '__main__':

    prompt = ChatPromptTemplate.from_template("You are an AI. Answer this: {question}")

    # Format the prompt
    formatted_prompt = prompt.format(question="What is the capital of CZ?")
    
    response = llm_invoke(formatted_prompt)
    print(response)