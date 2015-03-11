# -*- coding: utf-8 -*-
#########################
#       PYCOMPILER      #
#########################


#########################
# IMPORTS               #
#########################
from accc.compiler import Compiler
from accc.langspec import python_spec




#########################
# PRE-DECLARATIONS      #
#########################



#########################
# PYCOMPILER CLASS      #
#########################
class PyCompiler(Compiler):
    """
    Compiler specialized in Python code.
    Provide simpler API (automatization of python specifications sending),
    and new tools (for call a code)
    """
# CONSTRUCTOR #################################################################
    def __init__(self, alphabet, comparables, predicats, actions, operators):
        """"""
        super().__init__(alphabet, python_spec, comparables, predicats, actions, operators)
        self.last_python_code = None

# PUBLIC METHODS ##############################################################
    def compile(self, source_code, post_treatment=''.join, source='<string>', target='exec'): 
        """Return ready-to-exec object code of compilation.
        Use python built-in compile function.
        Use exec(1) on returned object for execute it."""
        self.last_python_code = super().compile(source_code, post_treatment)
        return PyCompiler.executable(self.last_python_code, source, target)

# PRIVATE METHODS #############################################################
# CLASS METHODS ###############################################################
    @staticmethod
    def executable(python_code, source='<string>', target='exec'):
        return compile(python_code, source, target)

# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################



