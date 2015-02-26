# -*- coding: utf-8 -*-
#########################
# IMPORTS               #
#########################
from accc.compiler import Compiler
from accc.compiler import LEXEM_TYPE_COMPARISON, LEXEM_TYPE_PREDICAT  
from accc.compiler import LEXEM_TYPE_ACTION    , LEXEM_TYPE_OPERATOR  

import random, time



#########################
# PRE-DECLARATIONS      #
#########################


#########################
# MAIN                  #
#########################
if __name__ == '__main__':
    def mutated(source_code, alphabet):
        """return an imperfect copy of source_code, modified at a random index"""
        source_code = list(source_code)
        index = random.randrange(0, len(source_code))
        old = source_code[index]
        while source_code[index] is old:
            source_code[index] = random.choice(alphabet)
        return ''.join(source_code)

    # create compiler
    alphabet = '01'
    source_code_size = 60
    cc  = Compiler(alphabet,
                    ('parameter1', 'parameter2', 'parameter3', 'parameter4', 'int_value'),
                    ('have_that', 'is_this', 'have_many_things', 'know_that'),
                    ('do_that', 'say_this', 'do_it'),
                    ('>', '==', '<', 'is', '!='),
                  )

    # print source code, compile it, modify it, and loop ad vitam eternam
    source = ''.join((random.choice(alphabet) for _ in range(source_code_size)))
    while True:
        print(source)
        msource = mutated(source, alphabet)
        print(''.join([' ' if n == m else m for n, m in zip(source, msource)]))
        print(cc.compile(msource))
        print(cc.header(msource), cc.structure(msource), cc.values(msource), 
              sep='|', end='\n'+source_code_size*'-'+'\n'+source_code_size*'-'+'\n'
             )
        source = msource
        time.sleep(0.1)





