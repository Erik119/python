'''def deco(func):
    def wrapper():
        print('before')
        func()
        print('after')
    return wrapper()

@deco
def name():
    print('Erik')
'''

#=======================================

def deco(func):
    def wrapper(*args, **kwargs):
        print('before')
        func(*args, **kwargs)
        print('after')
    return wrapper

@deco
def say_name(name):
    print(name)

say_name('Erik')

 