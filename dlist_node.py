class DListNode:
    def __init__(self, val):
        self._next = None
        self._prev = None
        self._head = None
        self._val = val

    def get_val(self):
        return self._val

    def get_prev(self):
        return self._prev

    def get_next(self):
        return self._next

    def set_val(self, val):
        self._val = val

    def set_prev(self, val):
        self._prev = val

    def set_next(self, val):
        self._next = val

    def __str__(self):
        vals = []
        objs = set()
        cur = self
        while cur is not None:
            cur_str = str(cur._val)
            if cur in objs:
                vals.append("{} ->".format(str(cur._val)))
                break
            else:
                vals.append(str(cur._val))
                objs.add(cur)
            cur = cur._next
        return " -> ".join(vals)


