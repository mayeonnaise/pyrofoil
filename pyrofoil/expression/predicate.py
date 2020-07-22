from typing import Iterable

from pyrofoil.expression.variable import Variable
from pyrofoil.expression.constant import Constant


class Predicate:

    def __init__(self, name: str, variables: Iterable[Variable, Constant]):
        self.name = name
        self.variables = variables

    def __str__(self):
        return self.name + "(" + \
               ",".join([str(var) for var in self.variables]) + ")"
