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
from accc.langspec    import python_spec




#########################
# PRE-DECLARATIONS      #
#########################
# SIMULATION PARAMETERS
POP_SIZE        = 30
KEEPED_BY_GEN   = 12
CRISIS_TIME     = 50
MUTATION_RATE   = 0.01
MUTATION_CHANCE = 0.7
PARENT_COUNT    = 2


# SIMULATION DEFINITION
DEFAULT_DNA_LEN = 40
NUCLEOTIDS      = 'ATGC'
FITNESS_ON_OFF  = True
FITNESS_SWITCH  = False
SCREEN_REFRESH  = 10
SCREEN_SHOWED   = 2

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
        #self.fitness = 0
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
    def from_pop(pop, parent_count, compiler, count=1):
        """Create a list of count Unit, by choosing parent_count parents in pop.
        High fitness improves probability of reproduction."""
        #from collections import defaultdict
        #stats = defaultdict(int)
        probs = tuple((u,u.abs_fitness) for u in pop)
        max_prob = sum(u.abs_fitness for u in pop)

        # get one parent
        def oneParent():
            """Return a unit, taked in pop. Higher is the fit, 
            higher is the chance to be selectionned."""
            if max_prob is 0: return pop[0]
            parent = None
            cur_prob = random.randrange(0, max_prob)
            for unit, fit in probs:
                cur_prob -= fit
                if cur_prob <= 0:
                    parent = unit
                    break
            #stats[parent] += 1
            assert(parent is not None)
            return parent

        # get count new unit
        new_units = []
        for _ in range(count):
            parents = (oneParent(), oneParent())
            new_units.append(
                Unit.from_parents(parents, compiler)
            )

        #print('\t'.join(str(u.abs_fitness) for u in pop))
        #print('\t'.join(str(stats[u]) for u in pop))
        #print('')
        return new_units







    @staticmethod
    def from_parents(parents, compiler):
        """Create a new Unit, result of given parent crossing."""
        #new_dna = sorted(parents, key=lambda x: x.fitness, reverse=True)[0].dna

        parent = random.choice(parents) 
        new_dna = ''
        for index in range(min(len(p.dna) for p in parents)):
            if random.randint(0, 100) == 0: 
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

    @property
    def abs_fitness(self):
        return abs(self.fitness)

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
def FITNESS_ON():  return     FITNESS_ON_OFF
def FITNESS_OFF(): return not FITNESS_ON_OFF


if __name__ == '__main__':
    bobby = DNACompiler(python_spec,
        ('random.randint(0,1)', '0', '1'),
        ('FITNESS_ON()', 'FITNESS_OFF()', 'FITNESS_ON_OFF', 'FITNESS_SWITCH', 'True', 'False'),
        ('self.fitness += 1', 'self.fitness -= 1', 'self.fitness *= -1', 'pass', 'self.fitness = 0'),
        ('==', '<'),
    )

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
            print('KEEPED          :', [u.fitness for u in pop][:KEEPED_BY_GEN])
            print('GENERATION_COUNT:', gen_count, end='\n\n\n')
            for i in range(SCREEN_SHOWED):
                print(i, ':', pop[i].dna, tuple(pop[i].dna == u.dna for u in pop).count(True))
                print(pop[i].python_code, end='\n\n\n')
        gen_count += 1

        # create new pop
        pop = pop[:KEEPED_BY_GEN]
        new_pop = list(pop)
        new_pop.extend(
            Unit.from_pop(pop, PARENT_COUNT, bobby, POP_SIZE - len(new_pop))
        )
        pop = new_pop
        assert(len(pop) == POP_SIZE)

        # Biological crisis ?
        FITNESS_SWITCH = False
        #if gen_count % CRISIS_TIME == 0:
        if random.randint(0, CRISIS_TIME) == 0:
            FITNESS_ON_OFF = not FITNESS_ON_OFF
            FITNESS_SWITCH = True

        time.sleep(0.01)






