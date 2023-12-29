import requests
url=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
repo_details=url.json()
# print(repo_details[1]["user"]["login"])

print(len(repo_details))

for i in range(len(repo_details)):
    print(repo_details[i]["user"]["login"])