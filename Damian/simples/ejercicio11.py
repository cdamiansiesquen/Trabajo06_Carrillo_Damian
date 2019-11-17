import os
# Declarar variables
precio_galletas, precio_de_empanadas, precio_de_pan= 0 , 0 , 0
#INPUT
precio_de_pan = int(os.sys.argv [ 1 ])
precio_de_empanadas = int(os.sys.argv [ 2 ])
precio_galletas = int(os.sys.argv [ 3 ])
# Processing
total = ( precio_de_empanadas + precio_de_pan + precio_galletas )
#verificador
Comprobando = ( total >= 70 )
#OUPUT
print("#####################################")
print("#       PANADERIA-SANTIAGO           ")
print("#####################################")
print("#")
print("#varibles:   cantidad:")
print("precio de pan:", precio_de_pan)
print("precio de empanadas:", precio_de_empanadas)
print("precio galletas:", precio_galletas)
print("precio total: s/. ", total)
print("#####################################")

#condicion simple
# Si el total supera los 75 soles, dar un cupon de 20 soles
if (Comprobando >= True):
    print( " usted se gano un cupon de 20 soles" )
#fin_if

