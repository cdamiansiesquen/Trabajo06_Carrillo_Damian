import os
precio_de_pantalones, precio_de_polos, precio_de_vestido= 0 , 0 , 0
#INPUT
precio_de_pantalones = int (os.sys.argv[ 1 ])
precio_de_polos = int (os.sys.argv[ 2 ])
precio_de_vestido = int(os.sys.argv[ 3 ])
# Processing
total = (precio_de_pantalones + precio_de_polos + precio_de_vestido)
#Verificador
comprobando = (total >= 100)
#OUPUT
print( "#####################################")
print( "#  Venta de ropa GAMARRITA           ")
print( "#####################################")
print( "#")
print( "#variables:   cantidad")
print( "precio de pantalones:", precio_de_pantalones)
print( "precio de vestido:", precio_de_vestido)
print( "precio de polos:", precio_de_polos)
print( "precio total: s/. ", total)
print( "#####################################")

#condicion simple
# Si el total supera los 100, se lleva un prenda gratis
if ( comprobando == True ):
    print(" usted gano un prenda")
#fin_if
