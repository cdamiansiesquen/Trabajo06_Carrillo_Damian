import os
cable, tv , pelicula =  0 , 0 , 0

# imput
cable = int (os.sys.argv [ 1 ])
tv = int (os.sys.argv [ 2 ])
pelicula = int (os.sys.argv [ 3 ])

# processing
total = ( cable + tv + pelicula )

# verificador
comprador = (total >= 100 )

# output
print ( " ############################## " )
print ( " # Feria Balta" )
print ( " #variables: cantidad: " )
print ( " #cable: " , cable )
print ( " #tv: " , tv)
print ( " #pelicula: " , pelicula )
print ( " total: " , total )
print ( " ############################## " )

# condicion simple
# si es comprador  tenga 50% de descuento
if (comprador ==  True ):
    print ( " se ha ganado un descuento " )
if ( 50 < comprador < 100 ):
    print ( " siga intentando " )
if (comprador < 49 ):
    print ( " Gracias por su compra" )
# fin_if
