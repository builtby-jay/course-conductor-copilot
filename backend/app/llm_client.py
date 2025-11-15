from .config import settings

def call_llm(prompt: str) -> str:
    """
    Replace this stub with an actual call to Claude/GPT.
    For hackathon demo, you can mock or log the prompt.
    """
    # Example (OpenAI-style, commented out):
    # from openai import OpenAI
    # client = OpenAI(api_key=settings.llm_api_key)
    # resp = client.chat.completions.create(
    #     model=settings.llm_model,
    #     messages=[
    #         {"role": "system", "content": "You are a helpful course ops copilot."},
    #         {"role": "user", "content": prompt},
    #     ],
    # )
    # return resp.choices[0].message.content

    # Temporary stub:
    return f"[LLM RESPONSE PLACEHOLDER for prompt length {len(prompt)}]"
