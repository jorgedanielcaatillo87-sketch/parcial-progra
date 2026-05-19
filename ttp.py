# ==========================================
# PARCIAL - ANALISIS DE CONTRASEÑAS
# ==========================================
# ==========================================
# FUNCION LETRA
# ==========================================
def es_letra(caracter: str) -> bool:
    """
    Verifica si un caracter es una letra.
    """

    retorno = False

    if ("a" <= caracter <= "z") or ("A" <= caracter <= "Z"):
        retorno = True

    return retorno

# ==========================================
# FUNCION NUMERO
# ==========================================
def es_numero(caracter: str) -> bool:
    """
    Verifica si un caracter es un numero.
    """

    retorno = False

    if "0" <= caracter <= "9":
        retorno = True

    return retorno

# =========================================
# FUNCION SIMBOLO
# ==========================================
def es_simbolo(caracter: str) -> bool:
    """
    Verifica si un caracter es un simbolo permitido.
    """

    simbolos = "!\"#$%&'()*+,-./"

    indice = 0

    retorno = False

    while indice < len(simbolos):

        if caracter == simbolos[indice]:
            retorno = True

        indice += 1

    return retorno


# ==========================================
# VALIDAR CONTRASEÑA
# ==========================================
def validar_contraseña(contraseña: str) -> bool:
    """
    Valida si la contraseña cumple
    los requisitos obligatorios.
    """

    tiene_letra = False

    if contraseña == "":
        retorno = False

    elif len(contraseña) < 8:
        retorno = False

    elif contraseña[0] == " ":
        retorno = False

    else:

        indice = 0

        while indice < len(contraseña):

            if es_letra(contraseña[indice]):
                tiene_letra = True

            indice += 1

        if tiene_letra:
            retorno = True

        else:
            retorno = False

    return retorno


# ==========================================
# NIVEL SEGURIDAD
# ==========================================
def nivel_seguridad(contraseña: str) -> str:
    """
    Determina el nivel de seguridad
    de la contraseña.
    """

    letras = False
    numeros = False
    simbolos = False

    indice = 0

    while indice < len(contraseña):

        caracter = contraseña[indice]

        if es_letra(caracter):
            letras = True

        elif es_numero(caracter):
            numeros = True

        elif es_simbolo(caracter):
            simbolos = True

        indice += 1

    # DEBIL
    if (
        len(contraseña) >= 8
        and len(contraseña) <= 9
        and letras
        and numeros == False
        and simbolos == False
    ):

        retorno = "DEBIL"

    # MEDIA
    elif (
        letras
        and numeros
        and simbolos == False
    ):

        retorno = "MEDIA"

    # FUERTE
    elif (
        len(contraseña) >= 12
        and letras
        and numeros
        and simbolos
    ):

        retorno = "FUERTE"

    else:

        retorno = "NO VALIDA"

    return retorno


# ==========================================
# CONTAR CARACTERES
# ==========================================
def contar_caracteres(contraseña: str) -> tuple:
    """
    Cuenta letras, numeros,
    simbolos y espacios.
    """

    letras = 0
    numeros = 0
    simbolos = 0
    espacios = 0

    indice = 0

    while indice < len(contraseña):

        caracter = contraseña[indice]

        if es_letra(caracter):
            letras += 1

        elif es_numero(caracter):
            numeros += 1

        elif caracter == " ":
            espacios += 1

        elif es_simbolo(caracter):
            simbolos += 1

        indice += 1

    return letras, numeros, simbolos, espacios


# ==========================================
# BUSCAR CARACTER
# ==========================================
def buscar_caracter(
    contraseña: str,
    buscar: str
) -> None:
    """
    Busca un caracter y muestra
    cantidad y posiciones.
    """

    cantidad = 0
    indice = 0

    print("Posiciones:")

    while indice < len(contraseña):

        if contraseña[indice] == buscar:

            print(indice)

            cantidad += 1

        indice += 1

    print("Cantidad:", cantidad)


# ==========================================
# INVERTIR CONTRASEÑA
# ==========================================
def invertir_contraseña(contraseña: str) -> str:
    """
    Invierte manualmente
    una contraseña.
    """

    invertida = ""

    indice = len(contraseña) - 1

    while indice >= 0:

        invertida += contraseña[indice]

        indice -= 1

    return invertida


# ==========================================
# REPORTE ESTADISTICO
# ==========================================
def reporte_estadistico(
    contraseña: str
) -> None:
    """
    Genera estadisticas
    de la contraseña.
    """

    letras = 0
    numeros = 0
    simbolos = 0

    indice = 0

    while indice < len(contraseña):

        caracter = contraseña[indice]

        if es_letra(caracter):
            letras += 1

        elif es_numero(caracter):
            numeros += 1

        elif es_simbolo(caracter):
            simbolos += 1

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
    print("Longitud:", len(contraseña))
    print("Porcentaje letras:", porcentaje_letras)
    print("Porcentaje numeros:", porcentaje_numeros)
    print("Porcentaje simbolos:", porcentaje_simbolos)
    print("Repetidos consecutivos:", repetidos)


# ==========================================
# PALINDROMO
# ==========================================
def es_palindromo(contraseña: str) -> bool:
    """
    Determina si una contraseña
    es palindromo.
    """

    invertida = invertir_contraseña(contraseña)

    retorno = False

    if contraseña == invertida:
        retorno = True

    return retorno


# ==========================================
# ORDENAR CONTRASEÑA
# ==========================================
def ordenar_contraseña(
    contraseña: str,
    orden: str
) -> str:
    """
    Ordena manualmente
    una contraseña.
    """

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

            # ASCENDENTE
            if orden == "1":

                if caracteres[j] > caracteres[j + 1]:

                    aux = caracteres[j]

                    caracteres[j] = caracteres[j + 1]

                    caracteres[j + 1] = aux

            # DESCENDENTE
            elif orden == "2":

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

    return ordenada


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

contraseña = ""

while True:

    print("\n========= MENU =========")
    print("1. Ingresar contraseña")
    print("2. Validar nivel seguridad")
    print("3. Contar caracteres")
    print("4. Buscar caracter")
    print("5. Invertir contraseña")
    print("6. Reporte estadistico")
    print("7. Verificar palindromo")
    print("8. Ordenar contraseña")
    print("9. Salir")

    opcion = input("Seleccione opcion: ")

    # ==========================================
    # INGRESAR
    # ==========================================
    if opcion == "1":

        nueva = input("Ingrese contraseña: ")

        if validar_contraseña(nueva):

            contraseña = nueva

            print("Contraseña guardada")

        else:

            print("Contraseña invalida")

    # ==========================================
    # SEGURIDAD
    # ==========================================
    elif opcion == "2":

        if contraseña == "":
            print("Primero ingrese contraseña")

        else:
            print("Nivel:", nivel_seguridad(contraseña))

    # ==========================================
    # CONTAR
    # ==========================================
    elif opcion == "3":

        if contraseña == "":
            print("Primero ingrese contraseña")

        else:

            letras, numeros, simbolos, espacios = contar_caracteres(
                contraseña
            )

            print("Letras:", letras)
            print("Numeros:", numeros)
            print("Simbolos:", simbolos)
            print("Espacios:", espacios)

    # ==========================================
    # BUSCAR
    # ==========================================
    elif opcion == "4":

        if contraseña == "":
            print("Primero ingrese contraseña")

        else:

            buscar = input("Ingrese caracter: ")

            buscar_caracter(contraseña, buscar)

    # ==========================================
    # INVERTIR
    # ==========================================
    elif opcion == "5":

        if contraseña == "":
            print("Primero ingrese contraseña")

        else:

            print(
                "Invertida:",
                invertir_contraseña(contraseña)
            )

    # ==========================================
    # REPORTE
    # ==========================================
    elif opcion == "6":

        if contraseña == "":
            print("Primero ingrese contraseña")

        else:

            reporte_estadistico(contraseña)

    # ==========================================
    # PALINDROMO
    # ==========================================
    elif opcion == "7":

        if contraseña == "":
            print("Primero ingrese contraseña")

        else:

            if es_palindromo(contraseña):
                print("La contraseña ES palindromo")

            else:
                print("La contraseña NO es palindromo")

    # ==========================================
    # ORDENAR
    # ==========================================
    elif opcion == "8":

        if contraseña == "":
            print("Primero ingrese contraseña")

        else:

            print("1. Ascendente")
            print("2. Descendente")

            orden = input("Seleccione: ")

            print(
                "Ordenada:",
                ordenar_contraseña(
                    contraseña,
                    orden
                )
            )

    # ==========================================
    # SALIR
    # ==========================================
    elif opcion == "9":

        print("Programa finalizado")

        break

    # ==========================================
    # INVALIDA
    # ==========================================
    else:

        print("Opcion invalida")