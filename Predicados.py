
#   Universo
Estudiante = {
    "Eric":["23760307", "Calculo", "Futbol", "HP VICTUS","Sistemas", "Claude", "Memo","Vigente"],
    #NoContro, Materia que toma, Deporte, Compu, Carrera, IA que USA, Profe, estatus
    "Angel":["23760339", "Programación","", "Asus", "Sistemas", "Chatgpt", "Bladimir", "Vigente"]
}

Maestro = {
    "Bladimir": ["Programación","Lenovo", 132],
    #Materia , Laptop,  NoEmpleado
    "Memo":["Calculo","", 141]
}


#Predicados

def enseña_a(x,y):
    for nombre_estudiante, datos in Estudiante.items():

        if nombre_estudiante == y and datos[6] == x:
            return True
    else:
        return False

#caso real
#print(enseña_a("Memo", "Eric"))
#caso falso
#print(enseña_a("Memo", "Angel"))




def estudia_carrera(x,y):
    for nombre_estudiante, datos in Estudiante.items():

        if nombre_estudiante == x and datos[4] == y:
            return True
    else:
        return False

#caso real
#print(estudia_carrera("Eric", "Sistemas"))
#caso falso
#print(estudia_carrera("Eric", "Gestión"))



def estudiante(x):
    for nombre_estudiante in Estudiante:
        if nombre_estudiante == x:
            return True
    else:
        return False

#caso real
#print (estudiante("Eric"))
#caso falso
#print (estudiante("Pepe"))




def maestro(x):
    for nombre_maestro in Maestro:
        if nombre_maestro == x:
            return True
    else:
        return False

# caso real
# print (maestro("Bladimir"))
# caso falso
# print (maestro("Jose"))


def deportista(x):
    for nombre_estudiante, datos in Estudiante.items():

        if nombre_estudiante == x and datos[2] == "":
            return False
    else:
        return True

# caso real
# print (deportista("Eric"))
# caso falso
# print (deportista("Angel"))


def tieneNoControl (x,y):
    for nombre_estudiante, datos in Estudiante.items():
         if nombre_estudiante == x and datos[0] == y:
                    return True
    else:
        return False

# caso real
# print(tieneNoControl("Eric", "23760307"))
# caso falso
# print(tieneNoControl("Eric", "23760310"))


def tiene_Computadora(x,y):
    for nombre_maestro, datos in Maestro.items():

        if nombre_maestro == x and datos[1] == y:
            return True
    else:
        return False

#caso real
print(tiene_Computadora("Bladimir", "Lenovo"))
print(tiene_Computadora("Bladimir", "Asus"))