class Indenter:

    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, val):
        return print('    ' * self.level + val)

with Indenter() as indent:
    indent.print('Hi')
    with indent:
        indent.print('Erik')

        



