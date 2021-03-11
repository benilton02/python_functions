#a função recebe um nome que a define
def funcao_nomeada():
    return "hello"

#a função não recebe um nome
anonima = lambda : 'hi'

#funcao em forma de classe
class FuncaoClasse():
    def __call__(self) :
        return 'hi and hello'

print(funcao_nomeada())
print(anonima())
print(FuncaoClasse()())