def blah(func):
    def inner(*args,**kwars):
        result=func(*args,**kwars)
        return result
    return inner
@blah
def add(a,b):
    return a+b
@blah
def mul(a,b):
    return a+b
