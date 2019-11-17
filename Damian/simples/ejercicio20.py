import os
precio_de_king_kong, precio_de_galletas, precio_chifles= 0 , 0 , 0
#INPUT
precio_de_king_kong=int(os.sys.argv[1])
precio_de_galletas=int(os.sys.argv[2])
precio_chifles=int(os.sys.argv[3])
# Processing
total=(precio_de_king_kong+precio_de_galletas+precio_chifles)
#Verificador
comprobando=(total>=150)
#OUPUT
print("#####################################")
print("#      San roque                     ")
print("#####################################")
print("#")
print("#variables:   cantidad")
print("precio de king kong:", precio_de_king_kong)
print("precio de galletas:", precio_de_galletas)
print("precio de chifles:", precio_chifles)
print("precio total: s/. ", total)
print("#####################################")

#condicion simple
# Si el total supera los 150, se lleva un king kong a 50% de descuento
if (comprobando == True ):
    print(" usted se llevo el 50% de descuento ")
#fin_if
