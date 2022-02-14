import requests
def get_data():
    res = requests.get("http://localhost:5000/students")
    if res.status_code==200:
        data = res.json()
        if len(data)==0:
            print("empty array")
        for std in data:
            print(f"Name: {std['name']}", f"ID: {std['id']}")
    else:
        print("opsss ... something went wrong")


def post_data():
    res = requests.post("http://localhost:5000/students/new", data={"name": "name"})
    if res.status_code>=200 and res.status_code<250:
        print(res.json())
    if res.status_code==400:
        print("error: ", res.json()["error"])
    else:
        print("ops something went wrong")

post_data()