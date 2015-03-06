# -*- coding: utf-8 -*-
"""
Show equivalency of object code with same source code 
but different language specification.
"""


from accc.compiler import Compiler
from accc.langspec import ada_spec, cpp_spec, python_spec as pyh_spec
from functools     import partial
import random, time
            
ALPHABET = '01'

# curry Compiler constructor
Compiler = partial(Compiler, 
        alphabet    = ALPHABET,
        comparables = ('comparable1', 'comparable2'),
        predicats   = ('predicat1', 'predicat2',),
        actions     = ('action1', 'action2'),
        operators   = ('>', '==', '<')
)

# creat compilers
ccs = [
    ('ADA',    Compiler(target_language_spec = ada_spec)),
    ('C++',    Compiler(target_language_spec = cpp_spec)),
    ('PYTHON', Compiler(target_language_spec = pyh_spec)),
]


# print source code, compile it, modify it, and loop ad vitam eternam
src = '1100000000001011000000001001011110111100'
print('SOURCE CODE:', src)
for name, cc in ccs:
    print('==========================================================')
    print('\t\t' + name)
    print('==========================================================')
    print(cc.compile(src))
    print('\n')








