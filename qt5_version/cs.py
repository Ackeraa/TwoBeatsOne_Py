class A():
    def __init__(self):
        self.a = 1
        self.b = 1
    def delete(self):
        del self.b

a = A()
a.delete()
print(a.b)
