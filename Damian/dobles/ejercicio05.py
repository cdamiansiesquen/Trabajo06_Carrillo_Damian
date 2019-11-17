import os
perfume, talco, jabon = 0 , 0 , 0

# imput
perfume = int (os.sys.argv [ 1 ])
talco = int (os.sys.argv [ 2 ])
jabon = int (os.sys.argv [ 3 ])

# processing
total = (perfume +talco+ jabon)

# verificador
comprobando = (total >= 50 )

# output
print ( " ############################## " )
print ( " # Real plaza chiclayo " )
print ( " #variables: cantidad: " )
print ( " # perfume: " , perfume )
print ( " # talco: " , talco)
print ( " # jabon: " , jabon)
print ( " total: " , total)
print ( " ############################## " )

# condicion simple
# si supera los 50 soles regalar un shampoo
if (comprobando ==  True ):
    print ( " se ha ganado un shampoo " )
else :
    print ( " vuelva pronto " )
# fin_if


