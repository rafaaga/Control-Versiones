parcial1 = input("¿Cual fue su nota en el primer parcial?")
parcial2 = input("¿Cual fue su nota en el segundo parcial?")
taller = input("¿Cual fue su nota en el taller?")
proyect = input("¿Cual fue su nota en el proyecto?")
parc1= float(parcial1)*0.25
parc2= float(parcial2)*0.25
tal= float(taller)*0.20
pro= float(proyect)*0.30
final = float(parc1+parc2+tal+pro)
round(final,2)
print("Su nota es: "+str(final))

# 2 Parciales (25% c/u)
# Taller (20%)
# Proyecto (30%)
