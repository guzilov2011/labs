# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.data = iter(items)
        self.set = set()
        self.ignore_case = kwargs.get('ignore_case', False)



    def __next__(self):
        # Нужно реализовать __next__
        while( True ):
           nxt = next(self.data)
           tmp = nxt
           if self.ignore_case :
             tmp = nxt.lower()
           if tmp in self.set:
             continue
           else:
             break
        self.set.add(tmp)
        return nxt




    def __iter__(self):
        return self
