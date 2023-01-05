  def __init__(self):
        self.item = []
        

    def push(self, x: int) -> None:
        self.item.append(x)
        

    def pop(self) -> int:
        if not self.empty():
            return self.item.pop(0)
        

    def peek(self) -> int:
        return self.item[0]
        

    def empty(self) -> bool:
        return self.item == []
