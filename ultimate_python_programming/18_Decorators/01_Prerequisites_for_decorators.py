"""
We need to understand that functions are first-class objects in python this means that,

1. Functions can be assigned to different variables
2. Functions can be sent as argument to a function
3. Functions can be returned from a function
"""
# 1. Function being assigned to different variables

def fn():
    print("Hello World")

f1=fn
f2=fn

fn()
f1()
f2()