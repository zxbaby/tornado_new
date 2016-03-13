__author__ = 'Administrator'

def decorator(f):
    def decoratored(*args, **kwargs):
        print 'inside decorator'
        return f(*args, **kwargs)
    return decoratored

@decorator
def test():
    print 'this is a test'


if __name__ == '__main__':
    test()
