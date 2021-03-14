#executar este código com ipython3 para melhor compreensão
#ipython3 -i main.py


def packing_args(*args):
    """
    *args -> trabalha com multiplos argumentos explicitamente posicionais;
    contraexemplo: my_args(a = 0, b = 1) -> não funcionará, pois os argumentos são nomeados
    """
    print(type(args))# '*args' é do tipo 'tuple'
    return args


def packing_kwargs(**kwargs):
    """
    **kwargs -> trabalha com argumentos explicitamente nomeados.
    contraexemplo: my_kwargs(1, 2) -> não funcionará, pois or argumentos não foram explicitamente nomeados
    """
    print(type(kwargs))# '**kwargs' é do tipo 'dict'
    return kwargs


def packing_mix(*args, **kwargs):
    """PACKING"""
    print(type(args),type(kwargs))
    return args, kwargs


my_list = [-2, -1, 100, 1, 2, 5, 19, 8]
def unpacking_list(*args):
    return max(args), min(args) #retorna o maior e o menor valor da lista


my_dict = {
    'q': 10,
    'w': -200,
    'e': -50,
    'r': -40
}
def unpacking_dict(q, w, e, r):
    return max((q, w, e, r)), min((q, w, e, r)) #retorna o maior e o menor valor do dicionário


def unpacking_mix(*args, q, w, e, r):
    return (args,(q, w, e, r))

print(packing_args(1, 2, 3),"\n\n") # argumentos explicitamente posicionais 
print(packing_kwargs(a = 1, b = 2, c = 3),"\n\n") # argumentos explicitamente nomeados
print(packing_mix(1, 2, 3, a = 1, b = 2, c = 3),"\n\n") # mesclagem de arguemtos explicitamente posicionais e explicitamente nomeados

print("list unpacked ->",unpacking_list(*my_list)) # unpacking da lista declarada
print("dictionary unpacked ->",unpacking_dict(**my_dict)) # unpacking do dicionário declarado
print(unpacking_mix(*my_list, **my_dict)) # unpacking da lista e do dicionário