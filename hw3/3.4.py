class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next: Node = next
class List:
    def __init__(self) -> None:
        self.head = Node(0)
    def insert(self, data, position: int = 0) -> None:
        if position > self.head.data:
            return
        node = Node(data)
        now = self.head.next
        pre = self.head
        for i in range(0, position):
            pre = now
            now = now.next
        self.head.data += 1
        pre.next = node
        node.next = now
        return
    def add(self, data) -> None:
        self.insert(data, self.size())
    def erase(self, position: int = 0) -> None:
        if position >= self.head.data:
            return
        now = self.head.next
        pre = self.head
        for i in range(0, position):
            pre = now
            now = now.next
        self.head.data -= 1
        pre.next = now.next
        return
    def size(self):
        return self.head.data
    def find(self,position:int=0):
        if position>=self.head.data:
            pass
            # return Node().data
        now=self.head.next
        for i in range(0,position):
            now=now.next
        return now
    def all(self):
        arr = [self.find(i).data for i in range(self.size())]
        return arr
a = List()
print("添加字符串\"DS\"")
a.add("DS")
print(a.all())

print("添加字符串\"homework\"")
a.add("homework")
print(a.all())

print("在第二个位置插入字符串\"第三周\"")
a.insert("第三周", 1)
print(a.all())

print("默认在头部插入数字3")
a.insert(3)
print(a.all())

print("删除在头位置的块")
a.erase(0)
print(a.all())




