# -*- coding: utf-8 -*-
"""
Simple test of Compiler class.
"""


from accc.compiler import Compiler
from accc.langspec import ada_spec
import random, time
            

def mutated(src, mutation_rate=0.1):
    """Return a mutated version of given string"""
    new_src = ''
    for nuc in src:
        if random.random() < mutation_rate:
            new_src += random.choice(dc.alphabet)
        else:
            new_src += nuc
    return new_src



# creat compiler
dc = Compiler('BÉPO', ada_spec,
              ('speed', 'word_per_minute', 'int_value'),
              ('is_reachable', 'is_pressable',),
              ('miss', 'press'),
              ('>', '==', '<')
             )

# print source code, compile it, modify it, and loop ad vitam eternam
src = ''.join((random.choice(dc.alphabet) for _ in range(40)))
while True:
    print(src)
    msrc = mutated(src)
    print(''.join([' ' if n == m else '!' for n, m in zip(src, msrc)]))
    print(dc.compile(msrc))
    print('\n------------\n\n\n')

    time.sleep(0.4)








