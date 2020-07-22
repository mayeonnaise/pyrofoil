class Variable:

    def __init__(self, type_name: str, var_name: str):
        self.type_name = type_name
        self.var_name = var_name

    def __str__(self):
        return self.type_name + "(" + self.var_name + ")"