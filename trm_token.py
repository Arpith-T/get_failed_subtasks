import requests
import json


def aciat001_trm_token():
    url = "https://aciat001.authentication.sap.hana.ondemand.com/oauth/token?grant_type=client_credentials"

    payload = {}
    files = {}
    headers = {
        'Authorization': 'Basic c2ItaXQhYjc2NDg6ZmIyMGZmYzktMDFjNy00ZTY2LTk2ODAtMjk3YzU3ZWY0ZTYzJEduMEtEeFYtd2Q4NTNTWTNJVXBjeElOSWU3UzhpRjZhZ3Jsdll0aXdhTE09'
    }

    response = requests.request("GET", url, headers=headers, data=payload, files=files)

    # print(response.text)
    # print("\n")
    # print(type(response.text))
    res_in_dict = json.loads(response.text)
    return res_in_dict["access_token"]


aciat001_trm_token()
