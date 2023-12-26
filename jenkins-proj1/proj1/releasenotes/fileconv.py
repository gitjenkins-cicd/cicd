import json
file=open("jenkins-proj1\\proj1\\releasenotes\\first.json", "r")
x=file.read()
finaldata=json.loads(x)

for i in finaldata:
    f=open("color.txt", "w")
    print(i["color"])
    col=i["color"]
    col.write("color.txt")
    f.close()

