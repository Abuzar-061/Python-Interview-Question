import requests

url = "https://www.wikipedia.com/"

response = requests.get(url)

try:
    data = response.json()  # Try to parse JSON
    print(data.get("name", "Key 'name' not found"))
except requests.exceptions.JSONDecodeError:
    print("Response is not in JSON format. Here is the raw response:")
    print(response.text[:50100000])  # Print the first 500 characters for debugging
    