
# la idea de hacer tantos hashmaps es poder hacer operaciones en tiempo constante

# un diccionario que tiene como llave letra mayuscula y como valor la minuscula
mays2mins = {chr(i): chr(i+32) for i in range(65, 91)}


# otro diccionario que tiene como llave letra minuscula y como valor la mayuscula
mins2mays = {chr(i+32): chr(i) for i in range(65,91)}

# para el caso de las vocales con acentos podemos hacer lo siguiente
vocales = ["á", "é", "í", "ó", "ú"]
for vocal in vocales:
    mins2mays[vocal] = vocal.upper()
    # y viceversa
    mays2mins[vocal.upper()] = vocal

# hacemos lo mismo para el complemento a 9
comp9 = {str(i): str(9-i) for i in range(0,10)}

def solidifyText(text, shift):
    pila = []
    text = text.upper()
    for i in range(len(text)):
        if text[i] in mays2mins or text[i] in comp9:
            if text[i] in mays2mins and i%2== 0:
                if ord(text[i]) + shift%25 > 90:
                    val = (ord(text[i]) + (shift%25))%91 + 65

                else:
                    val = ord(text[i]) + shift%25
                finalval = chr(val)
                pila.append(finalval)
            elif text[i] in mays2mins and i%2 == 1:
                if ord(text[i]) + shift%25 > 90:
                    val = (ord(text[i]) + (shift%25))%91 + 65

                else:
                    val = ord(text[i]) + shift%25
                finalval = chr(val)
                pila.append(finalval.lower())
            if text[i] in comp9:
                pila.append(comp9[text[i]])

        else: 
            pila.append(text[i])
    pila.reverse()
    return "".join(pila)


print(solidifyText("BORN IN 2015!", 1))








