# 1-15 dias: dia = 3$
# 16-30 dias: dia = 5$
# 30+ dias: dia = 10$

# juancito 12 dias => 12*3 = 36$
# pedrito 18 dias => 18*5 = 90$
# tomacito 35 dias => 35*10 = 350$

dias = int( input("Ingrese cantidad de dias trabajados: ") )

if dias<0:
    sueldo = 0
elif dias < 15 :
    sueldo = dias*3
elif dias > 15 and dias<30:
    sueldo = dias*5
else:
    sueldo = dias*10

print('Usted trabajo %s dias y su sueldo es: %s $ ' % (dias, sueldo))



