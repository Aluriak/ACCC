# -*- coding: utf-8 -*-
#########################
#    DNACOMPILATION     #
#########################


#########################
# IMPORTS               #
#########################
import os
import random

from accc.dnacompiler import DNACompiler




#########################
# PRE-DECLARATIONS      #
#########################
# SIMULATION PARAMETERS
POP_SIZE        = 24
KEEPED_BY_GEN   = 16
CRISIS_TIME     = 50
MUTATION_RATE   = 0.001
MUTATION_CHANCE = 0.4
PARENT_COUNT    = 2


# SIMULATION DEFINITION
DEFAULT_DNA_LEN = 60
NUCLEOTIDS      = 'ATGC'
FITNESS_ON_OFF  = True
FITNESS_SWITCH  = False
SCREEN_REFRESH  = 10

# HELPS
clear = lambda: os.system('clear')

# COMPILER VOCABULARY
#def function1(unit):
    #unit.fitness += 10
#def function2(unit):
    #unit.fitness -= 10
#def function3(unit):
    #unit.fitness *= -1
#def fitness_on_off():
    #return FITNESS_ON_OFF
#def fitness_switch():
    #return FITNESS_SWITCH



#########################
# UNIT                  #
#########################
class Unit():
    
    def __init__(self, dc, *, dna=None, len_dna=DEFAULT_DNA_LEN):
        if dna is None:
            self.dna = ''.join((random.choice(NUCLEOTIDS) for _ in range(len_dna)))
        else:
            self.dna = dna

        self.python_code = dc.compile(self.dna)
        self.code        = compile(self._decorate(self.python_code), '<string>', 'exec')
        self.fitness = 0


# CONSTRUCTOR #################################################################
# PUBLIC METHODS ##############################################################
    def exec_fun(self):
        self.fitness = 0
        exec(self.code)

# PRIVATE METHODS #############################################################
    def _decorate(self, code):
        objc = code
        #objc = "def func_dna(self):\n"
        #for line in code.split('\n'):
            #objc += "\t" + line + "\n"
        return objc
    
# CLASS METHODS ###############################################################
    @staticmethod
    def from_parents(parents, compiler):
        """Create a new Unit, result of given parent crossing."""
        parent = random.choice(parents) 
        new_dna = ''
        for index in range(min(len(p.dna) for p in parents)):
            if random.randint(0, 100): 
                parent = random.choice(parents) 
            new_dna += parent.dna[index]
        return Unit.mutated(compiler, new_dna)

    @staticmethod
    def mutated(compiler, dna):
        """Return a mutated version of given string"""
        # Create DNA
        src = dna
        if random.random() < MUTATION_CHANCE:
            src = ''
            for nuc in dna:
                if random.random() < MUTATION_RATE:
                    src += random.choice(NUCLEOTIDS)
                else:
                    src += nuc
        # Create unit
        return Unit(compiler, dna=src)

            

# PREDICATS ###################################################################
# ACCESSORS ###################################################################
    @property
    def dna_len(self):
        return len(self.dna)

# CONVERSION ##################################################################
    def __str__(self):
        return str(self.fitness)
    def __repr__(self):
        return str(self)
# OPERATORS ###################################################################
    #def __lt__(self, othr): # <
        #return self.fitness < othr.fitness





#########################
# FUNCTIONS             #
#########################
if __name__ == '__main__':
    bobby = DNACompiler(
        ('random.randint(0,1)', '0'),
        ('FITNESS_ON_OFF', 'FITNESS_SWITCH'),
        ('self.fitness += 10', 'self.fitness -= 10', 'self.fitness *= 10', 'self.fitness *= -1'),
        ('==', '<'),
    )

    #u = Unit(bobby)
    #print(u.code)
    #print(u.dna)
    #print(bobby.compile(u.dna))
    #print(u.fitness)
    #u.exec_fun()
    #print(u.fitness)
    #exit(0)

    # create population
    pop = [Unit(bobby) for _ in range(POP_SIZE)]
    import time

    gen_count = 0
    while True:
        # update fitness
        [u.exec_fun() for u in pop]
        pop = sorted(pop, key=lambda x: x.fitness, reverse=FITNESS_ON_OFF)

        # printing 
        if gen_count % SCREEN_REFRESH == 0:
            clear()
            print('FITNESS_ON_OFF  :', FITNESS_ON_OFF)
            print('FITNESSES       :', [u.fitness for u in pop])
            print('GENERATION_COUNT:', gen_count, end='\n\n\n')
            print(pop[0].dna)
            print(pop[0].python_code)
        gen_count += 1

        # create new pop
        pop = pop[KEEPED_BY_GEN:]
        new_pop = list(pop)
        while len(new_pop) < POP_SIZE:
            new_pop.append(
                Unit.from_parents(random.sample(pop, PARENT_COUNT), bobby)
            )
        pop = new_pop

        # Biological crisis ?
        if gen_count % CRISIS_TIME == 0:
            FITNESS_ON_OFF = not FITNESS_ON_OFF
            FITNESS_SWITCH = True
        else:
            FITNESS_SWITCH = False

        time.sleep(0.01)






