from huggingface_hub import InferenceClient
from config import HF_KEY, SYSTEM_PROMPT, MAX_TOTAL_TOKENS, SAFE_BUFFER
from search import bing_search, extract_search_results
from helper import limit_history, count_tokens

client = InferenceClient(api_key=HF_KEY)

def generate_search_query(user_input):
    messages = [
        {"role": "system", "content": "You generate search queries for business analysis."},
        {"role": "user", "content": f"Convert this user input into an effective web search query: {user_input}"}
    ]
    
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.2-11B-Vision-Instruct",
        messages=messages,
        max_tokens=50
    )
    return response.choices[0].message["content"].strip()

def chat_with_model(user_input, history):
    history = limit_history(history)
    search_query = generate_search_query(user_input)
    search_results = bing_search(search_query)
    web_context = extract_search_results(search_results)

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for user_msg, model_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": model_msg})
    messages.append({"role": "user", "content": user_input})

    if web_context:
        messages.append({"role": "system", "content": f"Relevant web search results:\n{web_context}"})

    total_tokens = count_tokens(messages)
    max_tokens = max(500, min(1500, MAX_TOTAL_TOKENS - total_tokens - SAFE_BUFFER))

    if max_tokens < 100:
        history = limit_history(history, max_entries=3)
        return chat_with_model(user_input, history)

    stream = client.chat.completions.create(
        model="meta-llama/Llama-3.2-11B-Vision-Instruct",
        messages=messages,
        max_tokens=max_tokens,
        stream=True
    )

    response = "".join(chunk.choices[0].delta.content or "" for chunk in stream)
    history.append((user_input, response))
    return history
