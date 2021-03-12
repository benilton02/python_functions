#executar este código com ipython3 para melhor compreensão
#ipython3 -i main.py



def soma_posicional(x, y):
    """X e Y são parâmentros posicionais, não importa a ordem dos valores"""
    print(f'x:{x}, y:{y}')
    return x + y

def soma_nomeada(x = 0, y = 1):
    """
    X e Y são parâmentros nomeados
    na falta de x ou y, o valor 7 será usado
    """
    print(f'x:{x}, y:{y}')
    return x + y

def soma_explicitamente_nomeada(*, x = 0, y = 1 ):
    """
    X e Y são parâmetros nomeados.
    É preciso explicitar os valores de X e Y na chamada da função.
    a ordem do asteristico (*) importa e tudo que estiver a direita do '*' deve ser explicicitamente nomeado
    exemplo de chamada da função : soma_explicitamente_nomeada(x = 10, y = 5)
    """
    print(f'x:{x}, y:{y}')
    return x + y

def soma_explicitamente_nomeada2(x = 0, *, y = 1):
    """
    X é um parâmetro posicioanl e Y é um parâmetro nomeado.
    O valor de Y dever ser explicito na chamda da função.
    """
    print(f'x:{x}, y:{y}')
    return x + y

def soma_explicitamente_posicional(x, y, /):
    """
    O caractere '/' no final indica que os argumrtnos são explicitamente posicionais (disponível a partir dos python3.8)
    sendo assim, basta passar os valores desejados na chamda da função.
    Caso algum parâmetro seja nomeado não funcionará
    """
    print(f'x:{x}, y:{y}')
    return x + y

def soma_posicional_nomeada(x, y, /, z, *, w):
    """
    X e Y:  explicitamente posicionais
    z: posicional ou nomeado
    w: explicitmante nomeado
    """
    print(f' x:{x}, y:{y}, z:{z}, w:{w}')
    return sum((x, y, z, w))


# Exemplos para: soma_posicional
# print(soma_posicional(10, 20))
# print(soma_posicional(20, 10))
# print(soma_posicional(x = 10, y = 20))
# print(soma_posicional(y = 20, x = 10))

# Exemplos para: soma_nomeada
# print(soma_nomeada()) # mantem os valores padrões das variáveis
# print(soma_nomeada(x = 10, y = 20)) # a ordem não altera o retorno da função 
# print(soma_nomeada(y = 20, x = 10)) # a ordem não altera o retorno da função 

# Exemplos para: soma_explicitamente_nomeada
# print(soma_explicitamente_nomeada())
# print(soma_explicitamente_nomeada(x = 10, y = 20))
# print(soma_explicitamente_nomeada(10, 20)) # (contraexemplo) não funcionará já que X e Y não foram explicitamente definidos



# Exemplos para: soma_explicitamente_nomeada2 
# print(soma_explicitamente_nomeada2(9)) # X recebe 9  e Y continua com seu valor inicial de 1
# print(soma_explicitamente_nomeada2(y = 9)) # Y recebe e X continua com seu valor inicial de 0
# print(soma_explicitamente_nomeada2( 10, 20)) # (contraexemplo)Note que o valor de Y não foi explicitado, logo não funcionará

# Exemplo para: soma_explicitamente_posicional
# print(soma_explicitamente_posicional(10, 20))
# print(soma_explicitamente_posicional(x = 10, 20)) # (contraexemplo) não funcionará, pois os parâmetros foram nomeados
# print(soma_explicitamente_posicional(10, y = 20)) # (contraexemplo) não funcionará, pois os parâmetros foram nomeados

# Exemplo para: soma_posicional_nomeada
print(soma_posicional_nomeada(1, 2, 3, w = 4)) # o parâmetro z é posicional
print(soma_posicional_nomeada(1, 2, z = 3, w = 4)) # o parâmetro z é nomeado
