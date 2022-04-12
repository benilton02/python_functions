import re


regexes = [
    r'p.r', # . - Entende qualquer valor exceto uma linha nova
    r'^p',  # ^ - Irá testar se o início da string é igual ao que está sendo buscado
    r'[^p ^l]', # [^string] - Irá testar se o valor não é igual ao que está sendo buscado, buscar valores que não sejam a
    r'\d', # \d - Irá buscar um dígito (de 0 a 9)
    r'\D', # \D - Irá buscar um caracter que não seja um dígito (a, b, c...)
    r'\s', # \s - Irá buscar um espaço em branco 
    r'\S', # \S - Irá buscar um caracter que não seja um espaço em branco
    ]


def result(regex):
    text = 'paralelepipedo  0123456789'
    result = re.compile(regex)
    check = result.findall(text)
    regex = f" - r\'{regex}\'"
    print(check, regex)



if __name__ == '__main__':
    for regex in regexes:
        result(regex)
