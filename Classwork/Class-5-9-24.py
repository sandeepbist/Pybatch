x=10
def outer_function():
    x = 20
    def inner_function():
        x=30
        print(x)
    inner_function()
    print(x)

outer_function()
print(x)