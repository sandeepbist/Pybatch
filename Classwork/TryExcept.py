a = 10 
try:
    print(f"value of {a}")
except:
    print(f"Value of a does not exist")


b=10
c=20

try: 
    assert a > b
    print("assertion is true")
    
except:
    print("assertion is false")

d = int(input("enter number 1 : "))
e = int(input("enter number 2 : "))

def div(a,b):
    assert b != 0
    return a/b

print(f"division of {d}/{e} is {div(d,e)}")