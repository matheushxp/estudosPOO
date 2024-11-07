class ClasseQualquer:
    def fazer(self) -> None:
        print('estou fazendo algo')


class OutraCoisa(ClasseQualquer):
    def preparar(self) -> None:
        print('estou preparando algo')

def fazer_func() -> None:
        print('estou fazendo outra coisa')


ob1 = ClasseQualquer()
ob2 = OutraCoisa()
ob2.fazer = fazer_func

ob1.fazer()
ob2.fazer()
