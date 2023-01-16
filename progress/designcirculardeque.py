class MyCircularDeque:

    def __init__(self, k: int):
        self.head = 0
        self.tail = 0
        self.size = 0
        self.maxSize = k
        self.arr = [0]*k        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.arr[self.head] = value 
        else:    
            self.head = (self.head-1)%self.maxSize
            self.arr[self.head] = value
        self.size += 1
        return True        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.arr[self.tail] = value 
        else:
            self.tail = (self.tail+1)%self.maxSize
            self.arr[self.tail] = value
        self.size += 1
        return True


    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.arr[self.head] = 0
        if self.size != 1:
            self.head = (self.head+1)%self.maxSize
        self.size -= 1
        return True        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        self.arr[self.tail] = 0
        if self.size != 1: 
            self.tail = (self.tail-1)%self.maxSize
        self.size -= 1
        return True 
        

    def getFront(self) -> int:
        return self.arr[self.head] if not self.isEmpty() else -1

    def getRear(self) -> int:
         return self.arr[self.tail] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.size == 0        

    def isFull(self) -> bool:
        return self.size == len(self.arr)
