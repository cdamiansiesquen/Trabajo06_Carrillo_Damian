import os
zapatos, polos , casaca =  0 , 0 , 0

# imput
zapatos = int (os.sys.argv [ 1 ])
polos = int (os.sys.argv [ 2 ])
casaca = int (os.sys.argv [ 3 ])

# processing
total = ( zapatos + polos + casaca )

# verificador
comprador = (total >= 120 )

# output
print ( " ############################## " )
print ( " # Real Plaza Chiclayo" )
print ( " #variables: cantidad: " )
print ( " #zapatos: " , zapatos)
print ( " #polos: " , polos)
print ( " #casaca: " , casaca)
print ( " total: " , total)
print ( " ############################## " )

# condicion simple
# si es comprador  tenga 70% de descuento
if (comprador ==  True ):
    print ( " se ha ganado un descuento " )
if ( 50 < comprador < 120 ):
    print ( " siga intentando " )
if (comprador < 49 ):
    print ( " Gracias por su compra" )
# fin_if
