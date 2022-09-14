# Menos de 100€       	=>          5%
# Entre 100€ y 200€	    =>          15%
# Entre 200€ y 350€	    =>          20%
# Entre 350€ y 600€	    =>          30%
# Más de 600€	        =>          45%

# algoritmo
# 1. guardar el impuesto en una variable llamada impuesto
# 2. multiplicar ese impuesto por el sueldo y dividirlo entre 100
# 3. guardar ese resultado en una variable llamada descuento
# 4. Mostrar la variable descuento usando print

sueldo = int( input( 'Cuál es el sueldo? ') )


if sueldo<100:
   print('Su impuesto es de 5%')
elif sueldo>=100 and sueldo<=200:
   print('Su impuesto es de 15%')
elif sueldo>=200 and sueldo<=350:
   print('Su impuesto es de 20%')
elif sueldo>=350 and sueldo<=600:
   print('Su impuesto es de 30%')
elif sueldo>=600:
   print('Su impuesto es de 45%')

