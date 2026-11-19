from stack import Stack


class BoundedStack(Stack):
    def __init__(self, limit):
        if limit < 1:
            raise ValueError("limit must be 1 or more")
        super().__init__()
        self.limit = limit

    def push(self, item):
        if len(self) >= self.limit:
            raise OverflowError("bounded stack is full")
        super().push(item)
