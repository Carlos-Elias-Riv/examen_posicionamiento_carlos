def solidifyText(text, shift):
    # la idea de hacer tantos hashmaps es poder hacer operaciones en tiempo constante

    # un diccionario que tiene como llave letra mayuscula y como valor la minuscula
    mays2mins = {chr(i): chr(i+32) for i in range(65, 91)}


    # otro diccionario que tiene como llave letra minuscula y como valor la mayuscula
    mins2mays = {chr(i+32): chr(i) for i in range(65,91)}



    # hacemos lo mismo para el complemento a 9
    comp9 = {str(i): str(9-i) for i in range(0,10)}
    # iniciamos el arreglo donde irá la respuesta
    pila = []
    # ponemos todo el texto en maysuculas
    text = text.upper()
    # loopeamos sobre todos los caracteres del texto
    for i in range(len(text)):
        # condiciones para transformar el texto
        if text[i] in mays2mins or text[i] in comp9:
            # letra y en posicion par, entonces guardamos como mayuscula
            if text[i] in mays2mins and i%2== 0:
                # hacemos el circular shift con un numero dado shift
                if ord(text[i]) + shift%25 > 90:
                    val = (ord(text[i]) + (shift%25))%91 + 65

                else:
                    val = ord(text[i]) + shift%25
                finalval = chr(val)
                # metemos el valor al arreglo, donde esta nuestra respuesta final
                pila.append(finalval)
            # letra y en posicion impar, entonces cuardamos como minuscula
            elif text[i] in mays2mins and i%2 == 1:
                # hacemos el circular shift
                if ord(text[i]) + shift%25 > 90:
                    val = (ord(text[i]) + (shift%25))%91 + 65

                else:
                    val = ord(text[i]) + shift%25
                finalval = chr(val)
                # metemos el valor a nuestra respuesta 
                pila.append(finalval.lower())
            # si es numero ponemos su complemento a 9
            if text[i] in comp9:
                pila.append(comp9[text[i]])

        else: 
            # si fue cualquier otro caracter diferente a numeros o letras
            pila.append(text[i])

    # la respuesta se pide al reves
    pila.reverse()
    # pegamos todos los caracteres de la respuesta, para que quede como string
    return "".join(pila)


# texto propuesto y la respuesta
texto = "Wardell Stephen Curry II (Akron, Ohio; 14 de marzo de 1988), mas conocido como Stephen Curry, es un jugador estadounidense de baloncesto que pertenece a la plantilla de los Golden State Warriors de la NBA. Con 1,88 metros de altura, juega en la posicion de base."

print(solidifyText(texto, 5))








