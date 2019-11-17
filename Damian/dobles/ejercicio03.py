import os
shampoo, acondicionador, jabon = 0 , 0 , 0

# imput
shampoo = int (os.sys.argv [ 1 ])
acondicionador = int (os.sys.argv [ 2 ])
jabon = int (os.sys.argv [ 3 ])

# processing
total = (shampoo + acondicionador + jabon)

# verificador
comprobando = (total >= 80 )

# output
print ( " ############################## " )
print ( " # Real plaza chiclayo " )
print ( " #variables: cantidad: " )
print ( " # shampoo: " , shampoo )
print ( " # acondicionador: " , acondicionador)
print ( " # jabon: " , jabon)
print ( " total: " , total)
print ( " ############################## " )

# condicion simple
# si supera los 80 soles regalar un descuento
if (comprobando ==  True ):
    print ( " se ha ganado un descuento " )
else :
    print ( " vuelva pronto " )
# fin_if
