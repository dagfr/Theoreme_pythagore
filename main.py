import math
import sys

units = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
unit = input("entrez l'unité de longueur du triangle" : ) 

if unit not in units:
    print("veuillez n'entrer une des unités de longueur valides : {} ".format(units)) 
    sys.exit()

name_triangle = input("entrez le nom du triangle (ex. ABC) : ").upper()  

if len(name_triangle) != 3 or not name_triangle.isalpha():
    print("veuillez entrer un nom valide (ex. ABC)") 
    sys.exit()

right_angle = input("entrer le sommet de l'angle droit (ex. A): ").upper()  

if len(right_angle) != 1 or right_angle not in name_triangle:
    print("veuillez entrez un sommet valide du triangle {} (ex. {}) ".format(name_triangle, name_triangle[0])) #typo and message
    sys.exit()

hypothenuse = "".join([a for a in name_triangle if a != right_angle]) 
side_triangle2,side_triangle3 = right_angle+hypothenuse[0], hypothenuse[1]+right_angle

length_side2 = input("entrer la longueur du coté {} en {}".format(side_triangle2,unit)) 
length_side3 = input("entrer la longueur du coté {} en {}".format(side_triangle3,unit))

if not length_side2.isdigit() or not length_side3.isdigit():
    print("Vous ne devez entrer que des nombres, pas de lettre ni de caractere speciaux")
    sys.exit()


print("le triangle {} est rectangle en {} d'hypothenuse {}".format(name_triangle,right_angle,hypothenuse)
print("d'après le théoreme de phytagore:")
print("on a: {}² = {}² + {}²".format(hypothenuse,side_triangle2,side_triangle3))
print("      {}² = {}² + {}²".format(hypothenuse,length_side2,length_side3))

side2_length_squared = int(length_side2) ** 2
side3_length_squared = int(length_side3) ** 2
hypo = math.sqrt(side2_length_squared + side3_length_squared)      

print(f"      {hypothenuse}² = {side2_length_squared} + {side2_length_squared}")
print(f"      {hypothenuse}² = {side2_length_squared + side3_length_squared}")
print(f"      {hypothenuse} = √{side2_length_squared + side3_length_squared}")
print(f"      {hypothenuse} = {hypo}")
print(f"      {hypothenuse} = {math.floor(hypo)}")

print(f"      L'hypothénuse {hypothenuse} mesure {math.floor(hypo)} {unit}")





