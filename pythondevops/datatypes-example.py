# arn="arn:aws:ec2:us-east-1:123456789012:instance/i-012abcd34efghi56"
# print(arn.split("/")[0].split(":")[3])

# # Concat
# str1="Hello"
# str2="world"
# res = str1 +","+ str2
# print(res)
# print(len(arn))

# Replacing:
filepath=r"D:/cicd-project1/pythondevops/test.txt"
with open(filepath, "r") as file:
    content=file.read()
    print(content)

updated_content=content.replace("Python", "java")
print(updated_content)
with open(filepath, "w") as file:
    file.write(updated_content)

# split
text = "Python is awesome"
words = text.split()
print("Words:", words)

# re find all
import re
text = "The quick brown fox"
pattern = r"brown"
search = re.search(pattern, text)
if search:
    print("pattern found:", search.group())
else:
    print("Pattern not found")