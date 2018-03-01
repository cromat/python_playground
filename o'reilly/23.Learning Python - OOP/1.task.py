class Adder:
    def add(self, x, y):
        print('Not Implemented')


class ListAdder(Adder):
    def add(self, x, y):
        return x + y


class DictAdder(Adder):
    def add(self, x, y):
        x.update(y)
        return x

la = ListAdder()
lst = la.add([1, 2, 3], [2])
print(lst)

da = DictAdder()
dct = da.add({'a': 1}, {'b': 2})
print(dct)
