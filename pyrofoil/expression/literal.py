from pyrofoil.expression.predicate import Predicate

class Literal:

    def __init__(self, pred: Predicate, neg: bool = False):
        self.pred = pred
        self.neg = neg


    def __str__(self):
        return "~" if self.neg else "" + str(self.pred)
