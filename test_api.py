import requests
from requests import Response

def test_get_users():
    response: Response = requests.get(url = "https://reqres.in/api/users/2")
    print(response.status_code)