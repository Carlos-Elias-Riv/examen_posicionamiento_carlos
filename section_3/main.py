# pila = []
# cad = "carlos"

# for c in cad: 
#     pila.append(c)
# newcad = ""
# while len(pila) > 0 :
#     newcad += pila.pop(-1)

# print(newcad)


class Stack():
    def __init__(self):
        self.stack = []
        self.head = ""
        self.size = 0

    def push(self, elem):
        self.head = elem
        self.stack.append(elem)
        self.size += 1

    def isEmpty(self):
        return self.size == 0

    def pop(self):
        if not self.isEmpty():
            value = self.stack.pop(-1)
            self.size -= 1
            if not self.isEmpty():
                self.head = self.stack[-1]
            return value

        else: 
            raise Exception("Pila vacia")

    

pila = Stack()

cad = "carlos"

for c in cad: 
    pila.push(c)
newcad = ""

while not pila.isEmpty():
    print(f'El elemento hasta arriba de la pila es: {pila.head}')
    newcad += pila.pop()

print(newcad)




