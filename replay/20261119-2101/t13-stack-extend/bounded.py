from stack import Stack


class BoundedStack(Stack):
    def __init__(self, limit):
        if limit < 1:
            raise ValueError("limit must be at least 1")
        super().__init__()
        self._limit = limit

    @property
    def limit(self):
        return self._limit

    def push(self, item):
        if len(self) >= self._limit:
            raise OverflowError("bounded stack limit reached")
        super().push(item)
