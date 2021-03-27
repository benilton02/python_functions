#executar este código com ipython3 para melhor compreensão
#ipython3 -i main.py

from myMap import Mymap
import pprint

pp = pprint

def main():
    pp.pprint(Mymap().show())
    pp.pprint(Mymap().name())
    pp.pprint(Mymap().price())
    pp.pprint(Mymap().kg())

if __name__== "__main__":
    main()