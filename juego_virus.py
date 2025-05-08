import random
print("BIENVENIDO A CALCULO 1")
respuesta1 = int(input("Hola, ¡presiona 1 para pasar calculo 1!"))
if respuesta1 == 1:
    respuesta2 = int(input(("Has sido engañado, esto es un virus informatico, si quieres sobrevivir deberas jugar conmigo, presiona 1 para continuar")))
    if respuesta2 == 1:
        prueba1 = input(("Bienvenido, tu primera pregunta es: ¿Cuanto es el limite de 2x-1/x-3 cuando X=3? (Responde en palabras)"))
        if prueba1 == "infinito" or prueba1 == "Infinito":
            resultado = random.randint(1,2)
            if resultado == 1:
                moneda = "cara"
            else:
                moneda = "sello"
            prueba2 = input("Correcto, has tardado tanto en responder que aproveche de lanzar una moneda, tu siguiente pregunta es: ¿Ha salido cara o sello?")
            if prueba2 == moneda:
                print("Correcto, ahora preparate para la ultima prueba")
                prueba3 = int(input("¿Que numero del 1 al 10 tiene la misma cantidad de letras que el numero que representa? (¡RESPONDE CON UN NUMERO O TU PC MORIRA!)"))
                if prueba3 == 5:
                    print("¡¿Acertaste?!, ¡imposible!")
                    print("Virus eliminado, PC salvado, pero no has salvado calculo 1 ya que usaste tiempo valioso en eliminar el virus")
                    X = random.randint(1,7)
                    if X >= 4:
                        print(f"Tu nota final fue un {X}, Mala mia, has pasado, FELICIDADES")
                    else:
                        print(f"Tu nota final fue un {X}, WAJAJA")
                else:
                    print("Respuesta incorrecta, el virus ha tomado el control.")
            else:
                print("Respuesta incorrecta, el virus ha tomado el control.")
        else:
            print("Respuesta incorrecta, el virus ha tomado el control.")
            
    else:
        print(" Has decidido no jugar... SYSTEM  FAILURE")
else:
    print("Calculo 1 reprobado :(")