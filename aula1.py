class MyClass:

    estatico = 'sanicxp'

    def __init__(self, estado):
        self.__estado = estado
        
    def print_estatico(self):
        print(self.estatico)

    @classmethod
    def altera_estatico(cls):
        cls.estatico = 'ganegro'

ob1 = MyClass(True)
ob2 = MyClass(True) 

ob1.altera_estatico()

print(ob1.estatico)
print(ob2.estatico)
print(MyClass.estatico)