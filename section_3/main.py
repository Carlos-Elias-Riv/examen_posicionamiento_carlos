# creamos una implementación básica pero muy útil de un stack
class Stack():
    def __init__(self):
        self.stack = []
        self.head = ""
        self.size = 0
        # este atributo es el que ayudara al resolver el problema, pues guarda las operaciones a imprimir
        self.operaciones = []

    
    # para crear una copia del stack, esto es útil para la parte recursiva del código de abajo
    def copy(self, pila):
        self.stack = pila.stack.copy()
        self.head = pila.head
        self.size = pila.size
        self.operaciones = pila.operaciones.copy()

    # meter un elemento a la pila
    def push(self, elem):
        self.head = elem
        self.stack.append(elem)
        self.size += 1
        self.operaciones.append("i")

    # revisa si la pila está vacía
    def isEmpty(self):
        return self.size == 0

    # regresa el head (FILO) si es que la pila no esta vacía
    def pop(self):
        if not self.isEmpty():
            self.operaciones.append("o")
            value = self.stack.pop(-1)
            self.size -= 1
            # siempre que se haga un pop se tiene que ajustar el head
            if not self.isEmpty():
                self.head = self.stack[-1]
            else:
                self.head = ""
            return value
        # es un error tratar de quitar el head si la pila esta vacía
        else: 
            raise Exception("Pila vacia")

    


# explicación a grandes rasgos del código: 
# En la parte no recursiva se va metiendo letras de word1 a la pila si el head != la letra en la que voy en word2
# No abro ramas hasta que el head == la letra en la que voy en word2 (word2[pos2])
#   |
#   |
#   v
# (*) [AQUI RECURSIVO] las ramas que abro son dos: 1. sacar la letra. 2. avanzar esperando encontrar otra igual
# [caso fracaso] si me termine el word1 regreso None
# tambien se va construyendo neword con las letras que van saliendo del stack, pues estas nunca regresan
# resp va acumulando las respuestas de casos base
# pos1 mantiene registro de en que letra se está de word1 y pos2 análogo pero para word2




# word1 –transformar--> word2 desde la posicion=pos
# neword es la palabra que se debe volver word2
def allposibleseqRec(word1, word2, pos1, pos2, neword, pila, resp):
    # caso base fracaso
    # puede ser tambien fracaso con pos2 >= len(word2)?
    if pos1 >= len(word1):
        if pos1 > len(word1):
            return 
        # lo unico que podría hacer es sacar de la pila e intentar a ver si armo la palabra
        else: 
            # intento ver si con lo que me queda en la pila logro armar la palabra
            while not pila.isEmpty():
                neword += pila.pop()
            # si pude es caso exito
            if neword == word2:
                resp.append(pila.operaciones)
                return 
            # si no pude es caso fracaso
            else: 
                return 

    # caso base exito
    if neword == word2:
        resp.append(pila.operaciones)
        return
    
    
    # mientras el head sea distinto de la letra en la que voy de la segunda meto al stack
    while pila.head != word2[pos2] and pos1 < len(word1):
        pila.push(word1[pos1])
        pos1 += 1

    # caso recursivo
    if pila.head == word2[pos2]:
        respuesta = None
        # dos opciones por lo que hacemos copia de la pila
        pila1 = Stack()
        pila1.copy(pila)


        # pop inmediatamente 
        neword1 = neword + pila1.pop()
        # si hago un pop avanzo en pos2
        respuesta = allposibleseqRec(word1, word2, pos1, pos2 +1, neword1, pila1, resp)
        if respuesta is not None:
            resp.append(respuesta)

        # espero encontrarme otra más adelante
        # por lo tanto hago push 
        if pos1 < len(word1):
            pila.push(word1[pos1])
            respuesta = (allposibleseqRec(word1, word2, pos1 + 1, pos2, neword, pila, resp))
            if respuesta is not None:
                resp.append(respuesta)

        

        
        return 
    else: 
        ## caso de fracaso 
        return 

    


def allposibleseq(word1, word2):
    pila = Stack()
    respuesta = []
    allposibleseqRec(word1, word2, 0, 0, "",pila, respuesta)
    
    return respuesta

print(allposibleseq("madam", "adamm"))
print("\n")
print(allposibleseq("bahama", "bahama"))
print("\n")
print(allposibleseq("eric", "rice"))
print("\n")
print(allposibleseq("aaaabbb", "ababaab"))





