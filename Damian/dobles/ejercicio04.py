import os
galletas ,  caramelos , bombones = 0 , 0 , 0

# imput
galletas = int (os.sys.argv [ 1 ])
caramelos = int (os.sys.argv [ 2 ])
bombones = int (os.sys.argv [ 3 ])

# processing
total = ( galletas + caramelos + bombones )

# verificador
comprobando = (total >= 50 )

# output
print ( " ############################## " )
print ( " # Tienda Lucia " )
print ( " #variables: cantidad: " )
print ( " # galletasl: " ,galletas )
print ( " # caramelos: " , caramelos )
print ( " # bombones: " , bombones )
print ( " total: " , total)
print ( " ############################## " )

# condicion simple
# si supera los 50 soles regalar una canasta
if (comprobando ==  True ):
    print ( " se ha ganado una canasta " )
else :
    print ( " siga intentando " )
# fin_if
