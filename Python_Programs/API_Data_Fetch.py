import requests

def fetch_data(API_URL):
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    return response.status_code


# Test
data = fetch_data("https://jsonplaceholder.typicode.com/posts/1")
print(data)

