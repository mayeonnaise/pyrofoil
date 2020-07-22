from typing import Iterable

from pyrofoil.expression.predicate import Predicate


class HornClause:

    def __init__(self, head: Predicate, body: Iterable[Predicate]):
        self.head = head
        self.body = body

    def __str__(self):
        return str(self.head) + ":-" + ",".join(str(pred) for pred in self.body)
