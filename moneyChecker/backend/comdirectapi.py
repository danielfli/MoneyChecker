import requests

def apifcn() :
    print("Hello from api")
    # api_url = "https://jsonplaceholder.typicode.com/todos/2"
    response = requests.get(api_url)
    requests.get(auth=)
    response.json()
    
    if response.status_code == 200:
        print("Got data")
        print(response.content)
        print(response.status_code)
    else:
        return 0
    