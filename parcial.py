
contraseña = ""

while True:

    print("\n========= MENÚ =========")
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

    # =========================
    # OPCION 1
    # =========================
    if opcion == "1":
        contraseña = input("Ingrese una contraseña: ")
        print("Contraseña guardada correctamente.")

    # =========================
    # OPCION 2
    # =========================
    elif opcion == "2":

        if contraseña == "":
            print("Primero debe ingresar una contraseña.")

        else:
            tiene_mayus = False
            tiene_minus = False
            tiene_num = False
            tiene_especial = False

            for caracter in contraseña:

                if caracter.isupper():
                    tiene_mayus = True

                elif caracter.islower():
                    tiene_minus = True

                elif caracter.isdigit():
                    tiene_num = True

                else:
                    tiene_especial = True

            if (
                len(contraseña) >= 8
                and tiene_mayus
                and tiene_minus
                and tiene_num
                and tiene_especial
            ):
                print("Contraseña SEGURA")

            else:
                print("Contraseña INSEGURA")

    # =========================
    # OPCION 3
    # =========================
    elif opcion == "3":

        if contraseña == "":
            print("Primero debe ingresar una contraseña.")

        else:

            mayus = 0
            minus = 0
            numeros = 0
            especiales = 0

            for caracter in contraseña:

                if caracter.isupper():
                    mayus += 1

                elif caracter.islower():
                    minus += 1

                elif caracter.isdigit():
                    numeros += 1

                else:
                    especiales += 1

            print("Mayúsculas:", mayus)
            print("Minúsculas:", minus)
            print("Números:", numeros)
            print("Especiales:", especiales)

    # =========================
    # OPCION 4
    # =========================
    elif opcion == "4":

        if contraseña == "":
            print("Primero debe ingresar una contraseña.")

        else:
            buscar = input("Ingrese el carácter a buscar: ")

            cantidad = contraseña.count(buscar)

            print("El carácter aparece", cantidad, "veces.")

    # =========================
    # OPCION 5
    # =========================
    elif opcion == "5":

        if contraseña == "":
            print("Primero debe ingresar una contraseña.")

        else:
            invertida = contraseña[::-1]
            print("Contraseña invertida:", invertida)

    # =========================
    # OPCION 6
    # =========================
    elif opcion == "6":

        if contraseña == "":
            print("Primero debe ingresar una contraseña.")

        else:
            longitud = len(contraseña)

            print("\n===== REPORTE =====")
            print("Longitud:", longitud)

            letras = 0

            for caracter in contraseña:
                if caracter.isalpha():
                    letras += 1

            print("Cantidad de letras:", letras)

    # =========================
    # OPCION 7
    # =========================
    elif opcion == "7":

        if contraseña == "":
            print("Primero debe ingresar una contraseña.")

        else:

            if contraseña == contraseña[::-1]:
                print("La contraseña ES palíndromo")

            else:
                print("La contraseña NO es palíndromo")

    # =========================
    # OPCION 8
    # =========================
    elif opcion == "8":

        if contraseña == "":
            print("Primero debe ingresar una contraseña.")

        else:

            ordenada = "".join(sorted(contraseña))

            print("Contraseña ordenada:", ordenada)

    # =========================
    # OPCION 9
    # =========================
    elif opcion == "9":

        print("Programa finalizado.")
        break

    # =========================
    # OPCION INVALIDA
    # =========================
    else:
        print("Opción inválida.")