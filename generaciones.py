print("Hola!")
name = input("¿Cómo te llamas? ")
print("Buen día,", name)
year = int(input("¿En qué año naciste? "))
age = 2024 - year
if year>= 1930 and year <=1948:
    print(name,", tienes", age ,"años y perteneces a la generación de los Niños de la Posguerra")
elif year>= 1949 and year <=1968:
    print(", tienes", age ,"años y perteneces a la generación de los Boomers")
elif year>= 1969 and year <=1980:
    print(name,", tienes", age ,"años y perteneces a la generación X")
elif year>= 1981 and year <=1993:
    print(name,", tienes", age ,"años y perteneces a la generación de los Millennials")
elif year>= 1994 and year <=2010:
       print(name,", tienes", age ,"años y perteneces a la generación Z")
elif year>= 2011:
       print(name,", tienes", age ,"años y perteneces a la generación Alfa")