import os
pastillas, jarabes, shampoo = 0 , 0 , 0

# imput
pastillas = int (os.sys.argv [1])
jarabes = int (os.sys.argv [2])
shampoo = int (os.sys.argv [3])

# processing
total = (pastillas + jarabes + shampoo)

# verificador
descuento = (total >= 20 )

# output
print ( " ############################## " )
print ( " #MIFARMA " )
print ( " #variables: cantidad: " )
print ( " #pastillas: " , pastillas)
print ( " #jarabe: " , jarabes)
print ( " # shampoo: " , shampoo)
print ( " total: " , total)
print ( " ############################## " )

# condicion simple
# si el total supera los 20 soles dar descuento
if (descuento ==  True ):
    print ( " siga intentando " )
# fin_if
