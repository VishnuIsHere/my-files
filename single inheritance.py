class A:
    def func(self):
        print('hello')
class B(A):
    def func2(self):
        super().func()
        print('world')
B=B()
B.func2()