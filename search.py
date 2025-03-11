import requests
from config import BING_API_KEY, BING_ENDPOINT

def bing_search(query):
    headers = {"Ocp-Apim-Subscription-Key": BING_API_KEY}
    params = {"q": query, "count": 3}
    response = requests.get(BING_ENDPOINT, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    return None

def extract_search_results(search_results):
    if not search_results:
        return ""
    snippets = [f"- {result['snippet']}" for result in search_results.get("webPages", {}).get("value", [])]
    return "\n".join(snippets)
