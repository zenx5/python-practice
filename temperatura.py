# Determinar si hace frio o calor
# Frio: menor a 10º grados
# Poco Frio: 10º a 17º grados
# Agradable: 17º a 25º grados
# Calor: 25º a 30º grados
# Ola Calor: mas de 30º grados

temperatura = int( input( 'Que temperatura tenemos? ' ) )

if temperatura<10:
    print('Hace mucho frio')
elif temperatura>10 and temperatura<17:
    print('Hace poco frio')
elif temperatura>17 and temperatura<25:
    print('La temperatura es agradable')
elif temperatura>25 and temperatura<30:
    print('Hace Calor')
elif temperatura>30:
    print('Hace Demasiado Calor')
