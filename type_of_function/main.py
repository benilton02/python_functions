def funcao_nomeada():
    return "hello"

anonima = lambda : 'hi'

#funcao em forma de classe
class FuncaoClasse():
    def __call__(self) :
        return 'hi and hello'

print(funcao_nomeada())
print(anonima())
print(FuncaoClasse()())