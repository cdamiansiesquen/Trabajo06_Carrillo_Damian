import os
perfume, shampoo, toallas  =  0 , 0 , 0

# imput
perfume = int (os.sys.argv [ 1 ])
shampoo = int (os.sys.argv [ 2 ])
toallas = int (os.sys.argv [ 3 ])

# processing
total = ( perfume + shampoo + toallas )

# verificador
comprador = (total >= 75 )

# output
print ( " ############################## " )
print ( " # tienda lucy" )
print ( " #variables: cantidad: " )
print ( " #perfume: " , perfume)
print ( " #shampoo: " , shampoo)
print ( " #toallas: " , toallas)
print ( " total: " , total)
print ( " ############################## " )

# condicion simple
# si es comprador  tenga 50% de descuento
if (comprador ==  True ):
    print ( " se ha ganado un descuento " )
if ( 60 < comprador < 75 ):
    print ( " siga intentando " )
if (comprador < 30 ):
    print ( " Gracias por su compra" )
# fin_if
