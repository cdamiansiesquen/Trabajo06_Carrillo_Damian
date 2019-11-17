import os
pelotas_futbol, pelotas_basquet, pelotas_voley = 0 , 0 , 0

# imput
pelotas_futbol = int (os.sys.argv [ 1 ])
pelotas_basquet = int (os.sys.argv [ 2 ])
pelotas_voley = int (os.sys.argv [ 3 ])

# processing
total = (pelotas_futbol + pelotas_basquet + pelotas_voley)

# verificador
comprobando = (total >= 350 )

# output
print ( " ############################## " )
print ( " # MIKASA " )
print ( " #variables: cantidad: " )
print ( " # pelotas futbol: " , pelotas_futbol )
print ( " # pelotas basquet: " , pelotas_basquet )
print ( " # pelotas voley: " , pelotas_voley )
print ( " total: " , total)
print ( " ############################## " )

# condicion simple
# si supera los 350 soles regalar una pelota
if (comprobando ==  True ):
    print ( " se ha ganado una pelota " )
else :
    print ( " vuelva pronto " )
# fin_if
