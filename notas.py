# Notas de Alumnos 
# Notas 0 - 9: Reprobados
# Notas 10 - 15: Aprobados
# Notas 16 - 20: Eximidos
# Pedir al usuario la nota:

notas = int( input("Ingrese Nota: ") )

if notas < 9:
    print("Reprobado")
elif notas > 10 and notas < 15 :
    print("Aprobado") 
elif notas > 16 and notas < 20:
    print("Eximido")
