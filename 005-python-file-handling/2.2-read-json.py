import json

with open("./upload/demo.json", "r") as file:
    data = json.load(file)
    print(data)

jsondata = '{ "name": "Satyam kumar", "place": "patna", "skills": [ "Raspberry pi", "Machine Learning", "Web Development" ], "email": "xyz@gmail.com", "projects": [ "Python Data Mining", "Python Data Science" ] }'
jsonres = json.loads(jsondata)
print(jsonres)
