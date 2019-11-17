import os
precio_de_carne, precio_de_cebolla, precio_sal= 0 , 0 , 0
#INPUT
precio_de_carne = int(os.sys.argv[ 1 ])
precio_de_cebolla = int(os.sys.argv[ 2 ])
precio_sal = int(os.sys.argv[ 3 ])
# Processing
total = ( precio_de_carne + precio_de_cebolla + precio_sal)
#Verificador
comprobando = ( total >= 15 )
#OUPUT
print( "#####################################")
print( "#      Tienda - Yolita               ")
print( "#####################################")
print( "#")
print( "#variables:   cantidad")
print( "precio de carne:", precio_de_carne)
print( "precio de cebolla:", precio_de_cebolla)
print( "precio de sal:", precio_sal)
print( "precio total: s/. ", total)
print( "#####################################")

#condicion simple
# Si el total supera los 15, se gana una canasta
if ( comprobando == True ):
    print(" usted gano la canasta ")
#fin_if
