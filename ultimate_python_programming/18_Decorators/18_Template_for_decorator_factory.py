from functools import wraps
def checking_return_value(lower_limit,upper_limit):
    def actual_decorator(fn):
        @wraps(fn)
        def wrapper(*args,**kwargs):
            # Place code to be executed before function call here
            print('Starting Execution........')
            result=fn(*args,**kwargs)
            if result<lower_limit or result>upper_limit:
                    raise ValueError('Return value is not within specific range')
            # Place code to be executed after function call here
            print(f'Return value is: {result}')
            print('Ending Execution........')
            return result
        return wrapper
    return actual_decorator

@checking_return_value(0,500)
def func1(m,n):
    return m*n

@checking_return_value(0,500)
def func2(m,n):
    return m**n

func1(5,10)
func2(5,10)
