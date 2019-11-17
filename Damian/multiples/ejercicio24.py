import os
aro, llantas , camaras_llantas =  0 , 0 , 0

# imput
aro = int (os.sys.argv [ 1 ])
llantas = int (os.sys.argv [ 2 ])
camaras_llantas = int (os.sys.argv [ 3 ])

# processing
total = ( aro + llantas + camaras_llantas )

# verificador
comprador = (total >= 270 )

# output
print ( " ############################## " )
print ( " # cherokee motos " )
print ( " #variables: cantidad: " )
print ( " #aro: " , aro)
print ( " #llantas: " , llantas)
print ( " #camaras_llantas: " , camaras_llantas)
print ( " total: " , total)
print ( " ############################## " )

# condicion simple
# si es comprador  tenga 50% de descuento
if (comprador ==  True ):
    print ( " se ha ganado un descuento " )
if ( 150 < comprador < 270 ):
    print ( " siga intentando " )
if (comprador < 149 ):
    print ( " Gracias por su compra" )
# fin_if
