import os
galletas, caramelos , chupetines =  0 , 0 , 0

# imput
galletas = int (os.sys.argv [ 1 ])
caramelos = int (os.sys.argv [ 2 ])
chupetines = int (os.sys.argv [ 3 ])

# processing
total = (galletas + caramelos + chupetines)

# verificador
comprador = (total >= 70 )

# output
print ( " ############################## " )
print ( " # tienda lucy" )
print ( " #variables: cantidad: " )
print ( " #galletos: " , galletas)
print ( " #caramelos: " , caramelos)
print ( " #chupetines: " , chupetines)
print ( " total: " , total)
print ( " ############################## " )

# condicion simple
# si es comprador  tenga 50% de descuento
if (comprador ==  True ):
    print ( " se ha ganado un descuento " )
if ( 50 < comprador < 70 ):
    print ( " siga intentando " )
if (comprador < 40 ):
    print ( " Gracias por su compra" )
# fin_if
