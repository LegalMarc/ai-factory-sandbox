from stack import Stack


class BoundedStack(Stack):
    def __init__(self, limit):
        if limit < 1:
            raise ValueError("limit must be at least 1")
        super().__init__()
        self._limit = limit

    def push(self, item):
        if len(self) >= self._limit:
            raise OverflowError("bounded stack is full")
        super().push(item)
