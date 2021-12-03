from functools import wraps

def deco(*args,**kwargs):
    def parse_func(func,name=None):
        return func
    return parse_func

@deco(name='hello')
def test():
    print('hello')

test()
print(test,test.__name__)
