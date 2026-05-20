
contraseña = ""
print("\n========= MENÚ =========")
while True:

    print("")
    print("1. Ingresar contraseña")
    print("2. Validar nivel de seguridad")
    print("3. Contar tipos de caracteres")
    print("4. Buscar carácter específico")
    print("5. Mostrar contraseña invertida")
    print("6. Generar reporte estadístico")
    print("7. Verificar si es palíndromo")
    print("8. Ordenar caracteres de la contraseña")
    print("9. Salir")

    opcion = input("Seleccione una opción: ")


    if opcion == "1":

        nueva = input("Ingrese una contraseña: ")

        tiene_letra = False

        for caracter in nueva:

            if (
                ("a" <= caracter <= "z")
                or
                ("A" <= caracter <= "Z")
            ):

                tiene_letra = True

        if nueva == "":

            print("Error: la contraseña no puede estar vacia")

        elif len(nueva) < 8:

            print("Error: debe tener al menos 8 caracteres")

        elif nueva[0] == " ":

            print("Error: no puede comenzar con espacios")

        elif tiene_letra == False:

            print("Error: debe contener al menos una letra")

        else:

            contraseña = nueva

            print("Contraseña guardada correctamente")


    elif opcion == "2":

        if contraseña == "":

            print("Primero debe ingresar una contraseña")

        else:

            tiene_letras = False
            tiene_numeros = False
            tiene_simbolos = False

            simbolos = "!\"#$%&'()*+,-./"

            indice = 0

            while indice < len(contraseña):

                caracter = contraseña[indice]

                if (
                    ("a" <= caracter <= "z")
                    or
                    ("A" <= caracter <= "Z")
                ):

                    tiene_letras = True

                elif "0" <= caracter <= "9":

                    tiene_numeros = True

                else:

                    indice_simbolo = 0

                    while indice_simbolo < len(simbolos):

                        if caracter == simbolos[indice_simbolo]:

                            tiene_simbolos = True

                        indice_simbolo += 1

                indice += 1

            if (
                len(contraseña) >= 8
                and len(contraseña) <= 9
                and tiene_letras
                and tiene_numeros == False
                and tiene_simbolos == False
            ):

                print("Nivel de seguridad: DEBIL")

            elif (
                tiene_letras
                and tiene_numeros
                and tiene_simbolos == False
            ):

                print("Nivel de seguridad: MEDIA")

            elif (
                len(contraseña) >= 12
                and tiene_letras
                and tiene_numeros
                and tiene_simbolos
            ):

                print("Nivel de seguridad: FUERTE")

            else:

                print("Contraseña no valida")


    elif opcion == "3":

        if contraseña == "":

            print("Primero debe ingresar una contraseña")

        else:

            letras = 0
            numeros = 0
            espacios = 0

            simbolos_validos = "!\"#$%&'()*+,-./"

            indice = 0

            while indice < len(contraseña):

                caracter = contraseña[indice]

                if (
                    ("a" <= caracter <= "z")
                    or
                    ("A" <= caracter <= "Z")
                ):

                    letras += 1

            
                elif "0" <= caracter <= "9":

                    numeros += 1


                elif caracter == " ":

                    espacios += 1

                else:

                    indice_simbolo = 0

                    while indice_simbolo < len(simbolos_validos):

                        if caracter == simbolos_validos[indice_simbolo]:

                            simbolos += 1

                        indice_simbolo += 1

                indice += 1

            print("Cantidad de letras:", letras)
            print("Cantidad de numeros:", numeros)
            print("Cantidad de simbolos:", simbolos)
            print("Cantidad de espacios:", espacios)


    elif opcion == "4":

        if contraseña == "":

            print("Primero debe ingresar una contraseña")

        else:

            buscar = input("Ingrese caracter: ")

            cantidad = 0
            posicion = 0

            print("Posiciones:")

            while posicion < len(contraseña):

                if contraseña[posicion] == buscar:

                    print(posicion)

                    cantidad += 1

                posicion += 1

            print("Cantidad de veces:", cantidad)


    elif opcion == "5":

        if contraseña == "":

            print("Primero debe ingresar una contraseña")

        else:

            invertida = ""

            indice = len(contraseña) - 1

            while indice >= 0:

                invertida += contraseña[indice]

                indice -= 1

            print("Contraseña invertida:", invertida)

    elif opcion == "6":

        if contraseña == "":

            print("Primero debe ingresar una contraseña")

        else:

            letras = 0
            numeros = 0
            simbolos = 0

            simbolos_validos = "!\"#$%&'()*+,-./"

            indice = 0

            while indice < len(contraseña):

                caracter = contraseña[indice]

                if (
                    ("a" <= caracter <= "z")
                    or
                    ("A" <= caracter <= "Z")
                ):

                    letras += 1

                elif "0" <= caracter <= "9":

                    numeros += 1

                else:

                    indice_simbolo = 0

                    while indice_simbolo < len(simbolos_validos):

                        if caracter == simbolos_validos[indice_simbolo]:

                            simbolos += 1

                        indice_simbolo += 1

                indice += 1

            porcentaje_letras = (letras * 100) / len(contraseña)
            porcentaje_numeros = (numeros * 100) / len(contraseña)
            porcentaje_simbolos = (simbolos * 100) / len(contraseña)

            repetidos = 0

            indice = 0

            while indice < len(contraseña) - 1:

                if contraseña[indice] == contraseña[indice + 1]:

                    repetidos += 1

                indice += 1

            print("\n===== REPORTE =====")
            print("Longitud total:", len(contraseña))
            print("Porcentaje letras:", porcentaje_letras)
            print("Porcentaje numeros:", porcentaje_numeros)
            print("Porcentaje simbolos:", porcentaje_simbolos)
            print("Cantidad repetidos consecutivos:", repetidos)

    elif opcion == "7":

        if contraseña == "":

            print("Primero debe ingresar una contraseña")

        else:

            invertida = ""

            indice = len(contraseña) - 1

            while indice >= 0:

                invertida += contraseña[indice]

                indice -= 1

            if contraseña == invertida:

                print("La contraseña ES palindromo")

            else:

                print("La contraseña NO es palindromo")

    elif opcion == "8":

        if contraseña == "":

            print("Primero debe ingresar una contraseña")

        else:

            print("1. Ascendente")
            print("2. Descendente")

            tipo = input("Seleccione opcion: ")

            caracteres = []

            indice = 0

            while indice < len(contraseña):

                caracteres += [contraseña[indice]]

                indice += 1

            largo = len(caracteres)

            i = 0

            while i < largo - 1:

                j = 0

                while j < largo - i - 1:

                    if tipo == "1":

                        if caracteres[j] > caracteres[j + 1]:

                            aux = caracteres[j]

                            caracteres[j] = caracteres[j + 1]

                            caracteres[j + 1] = aux

                    elif tipo == "2":

                        if caracteres[j] < caracteres[j + 1]:

                            aux = caracteres[j]

                            caracteres[j] = caracteres[j + 1]

                            caracteres[j + 1] = aux

                    j += 1

                i += 1


            ordenada = ""

            indice = 0

            while indice < len(caracteres):

                ordenada += caracteres[indice]

                indice += 1

            print("Contraseña ordenada:", ordenada)


    elif opcion == "9":

        print("Programa finalizado")

        break

    else:

        print("Opcion invalida")