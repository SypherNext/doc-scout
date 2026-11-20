# a.py
from b import bar

def foo():
    print("foo")
    bar()

# b.py
from a import foo

def bar():
    print("bar")
    foo()
