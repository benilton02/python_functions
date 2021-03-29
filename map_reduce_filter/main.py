#executar este código com ipython3 para melhor compreensão
#ipython3 -i main.py

from myMap import MyMap
from myFilter import MyFilter
import pprint

pp = pprint

def main():
    # pp.pprint(MyMap().show())
    # pp.pprint(MyMap().name())
    # pp.pprint(MyMap().price())
    # pp.pprint(MyMap().kg())

    pp.pprint(MyFilter().show())    
    pp.pprint(MyFilter().price())    
    pp.pprint(MyFilter().kg())

if __name__== "__main__":
    main()