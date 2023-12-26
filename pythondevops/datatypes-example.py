arn="arn:aws:ec2:us-east-1:123456789012:instance/i-012abcd34efghi56"
print(arn.split("/")[0].split(":")[3])
