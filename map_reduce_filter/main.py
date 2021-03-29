#executar este código com ipython3 para melhor compreensão
#ipython3 -i main.py

from myReduce import MyReduce
from myFilter import MyFilter
from myMap import MyMap
import pprint

pp = pprint

def main():
    # pp.pprint(MyMap().show())
    # pp.pprint(MyMap().name())
    # pp.pprint(MyMap().price())
    # pp.pprint(MyMap().kg())

    # pp.pprint(MyFilter().show())    
    # pp.pprint(MyFilter().price())    
    # pp.pprint(MyFilter().kg())

    pp.pprint(MyReduce().total_price())
    pp.pprint(MyReduce().total_kg())    

if __name__== "__main__":
    main()