# The purpose of the trace decorator is for debugging and tracking
# It can be used to print the function name,its arguments,its return value
# We want the user to be able choose whether they want to enable tracking or not
from functools import wraps
def trace(active=True):
    def actual_decorator(fn):
        if active==True:
            @wraps(fn)
            def wrapper(*args,**kwargs):
                print(f"{fn.__name__} was called")
                print(f"args: {fn.__name__} kwargs: {kwargs}")
                result=fn(*args,**kwargs)
                print(f"Return value: {result}")
                return result
            return wrapper
        else:
            return fn
    return actual_decorator

@trace()
def func1(m,n):
    return m+n

@trace(True)
def func2(m,n):
    return m*n

@trace(active=False)
def func3(m,n):
    return m**n

x=func1(5,6)
y=func2(3,4)
z=func3(2,5)
print(x,y,z)

