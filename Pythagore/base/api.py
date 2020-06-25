import math

unit = input("entrer l'unité des longueur du triangle")
name_triangle = input("entrer le nom du triangle")  # nom du triangle

right_angle = input("entrer le sommet de l'angle droit")  # sommet de l'angle droit

hypothenuse = input("entrer la nom du coté de l'hypothenuse")

side_triangle2 = input("entrer la nom du coté du 2eme coté")
length_side2 = input("entrer la longueur du 2eme coté")

side_triangle3 = input("entrer la nom du coté du 3eme coté")
length_side3 = input("entrer la longueur du 3eme coté")


print(f"le triangle {name_triangle} est rectangle en {right_angle} d'hypothenuse {hypothenuse}")
print("déprès le théoreme de phytagore:")
print(f"on a: {hypothenuse}² = {side_triangle2}² + {side_triangle3}²")
print(f"      {hypothenuse}² = {length_side2}² + {length_side3}²")

side2_length_squared = int(length_side2) ** 2
side3_length_squared = int(length_side3) ** 2

print(f"      {hypothenuse}² = {side2_length_squared} + {side2_length_squared}")
print(f"      {hypothenuse}² = {side2_length_squared + side3_length_squared}")
print(f"      {hypothenuse}² = √{side2_length_squared + side3_length_squared}")
print(f"      {hypothenuse} = {math.sqrt(side2_length_squared + side3_length_squared)}")
print(f"      {hypothenuse} = {math.floor(math.sqrt(side2_length_squared + side3_length_squared))}")

print(f"      L'ypothénuse mesure {math.floor(math.sqrt(side2_length_squared + side3_length_squared))} {unit}")





