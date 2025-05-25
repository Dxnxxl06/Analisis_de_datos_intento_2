# 4 numeros donde se pueda
#La longitud del número (cantidad de dígitos)., 
# La suma de todos sus dígitos., 
# La cantidad de dígitos pares.,
# La cantidad de dígitos impares.





def analizar_numero():
    while True:
        print ("--------BIENVENIDO--------")
        print ("""Este programa esta diseñado unicamente para hacer los siguientes procesos 
           1. Mostrar la longitud del numero digitado
           2. Mostrar la zuma de todos los digitos 
           3. Mostrar la cantidad de digitos pares
           4. Mostrar la cantidad de digtos impares""")
        entrada= input("""Ingrese los numeros con los que desea realizar este proceso: 
""")
        if entrada.isdigit() and len(entrada) >= 4:
            break
        else:
            print("Entrada no valida, ingrese unicamente digitos numericos, y recuerde que minimo son 4 digitos.")

    longitud= len(entrada)
    suma_digitos=0
    cant_pares=0
    cant_impares=0

    for digito in entrada: # type: ignore
        valor=int(digito)
        suma_digitos += valor
        if valor % 2 == 0:
            cant_pares += 1
        else:
            cant_impares += 1

    print ("La longitud de tu numero es ",longitud) 
    print ("La suma de los ditos de su numero es: ",suma_digitos)
    print ("Los numeros pares de su numero son: ",cant_pares)
    print ( "Los numeros impares de su numero son: ",cant_impares)

analizar_numero()
#Profe me queria morir haciendo esta vaina, buen dia/tarde/noche :D   
# Al menos aprendi a usar el .isdigit y el len


   



