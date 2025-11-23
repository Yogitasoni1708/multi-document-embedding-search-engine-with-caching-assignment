import requests
import json

API_URL = "http://localhost:8000/search"

def search_query(query, top_k=5):
    payload = {
        "query": query,
        "top_k": top_k
    }
    response = requests.post(API_URL, json=payload)
    return response.json()

if __name__ == "__main__":
    print("Testing API...")
    result = search_query("uk election news", 5)
    print(json.dumps(result, indent=4))
