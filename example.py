import math

def foo(a, b):
    return a + b

def bar():
    print("foo")

def feh(a, b):
    return a * b

class Foo(object):
    def __init__(self):
        self.feh = 0
    def inc_feh(self):
        self.feh = self.feh + 1
    def restart_feh(self):
        self.feh = 0
    def show_feh(self):
        print(self.feh)

bar()
bar = Foo()
print(bar.feh)
bar.inc_feh
bar.inc_feh
bar.show_feh
