import os
from docplex.mp.model import Model

print("CPLEX_STUDIO_DIR:", os.environ.get('CPLEX_STUDIO_DIR'))
print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
mdl = Model("Test")
print("CPLEX is configured correctly!")