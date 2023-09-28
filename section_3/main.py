class Stack():
    def __init__(self):
        self.stack = []
        self.head = ""
        self.size = 0
        self.operaciones = []

    
    # para crear una copia del stack
    def copy(self, pila):
        self.stack = pila.stack.copy()
        self.head = pila.head
        self.size = pila.size
        self.operaciones = pila.operaciones.copy()

    def push(self, elem):
        self.head = elem
        self.stack.append(elem)
        self.size += 1
        self.operaciones.append(1)

    def isEmpty(self):
        return self.size == 0

    def pop(self):
        if not self.isEmpty():
            self.operaciones.append(0)
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







# ideas: 
# podré hacer que el stack tenga memoria de las operaciones que se han hecho con ella? valdrá la pena?
# tener un dictionary que sepa las ocurrencias de cada letra para no tener que buscarla si ya no va a haber


# condiciones que sabemos:
# no abro ramas hasta que el head == la letra en la que voy en word2
#   |
#   |
#   v
# (*) [AQUI RECURSIVO] las ramas que abro son dos: 1. meter y sacar la letra. 2. avanzar esperando encontrar otra igual
# meto al stack SIEMPRE sin preguntar, a menos de que pase el caso de arriba
# [no hay recursividad] si el head != la letra en la que voy avanzo
# [caso base] si me termine el word1 regreso una lista vacia
# es posible que después de sacar una letra del stack tenga el caso (*)


# word1 –transformar--> word2 desde la posicion=pos
# neword es la palabra que se debe volver word2
# def allposibleseq(word1, word2, pos, neword, pila):
#     # caso base fracaso
#     if pos >= len(word1):
#         return []
#     # caso base exito
#     if neword== word2:
#         return pila.operaciones

#     pila.append(word1[pos])
 
#     # caso recursivo
#     if pila.head == word2[pos]:
#         # dos opciones por lo que hacemos copia de la pila

#         # pop inmediatamente 
#         neword += pila.pop()


#         return 0






