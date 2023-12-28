import sys
res=sys.argv[1]
if res == "jmeter":
    print("Executing load test using jmeter")
elif res == "k6":
    print("Executing Load test using k6")
elif res == "locust":
    print("Executing Load test using locust")
else:
    print("Pls provide correct option for load generation")
