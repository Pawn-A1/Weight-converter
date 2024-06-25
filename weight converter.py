print("What are you converting?")
print("1. kg")
print("2. g")
print("3. oz")
print("4. lb")

a = input("")

print("What do you want the end result to be in?")

print("1. kg")
print("2. g")
print("3. oz")
print("4. lb")

b = input("")

if a == "1":
    print("How many Kg do you want to convert")
    kg = float(input(""))
    if b == "1":
        print(str(kg)+" kilograms is "+str(kg)+" kilograms.")
    elif b =="2":
        kg_to_g = kg*1000
        print(str(kg)+" kilograms is "+str(kg_to_g)+" grams.")
    elif b == "3":
        kg_to_oz = kg*35.27
        print(str(kg)+" kilograms is "+str(kg_to_oz)+" ounces")
    elif b == "4":
        kg_to_lb = kg*2.2   
        print(str(kg)+"kilograms is "+str(kg_to_lb)+"pounds")
    else:
        print("Invalid number, press enter to exit")
elif a == "2":
    print("How many g do you want to convert")
    g = float(input(""))
    if b == "1":
        g_to_kg = g/1000
        print(str(g)+" grams is "+str(g_to_kg)+" kilograms ")
    elif b =="2":
        print(str(g)+" grams is "+str(g)+" grams ")
    elif b == "3":
        g_to_oz = g/28.34
        print(str(g)+" grams is "+str(g_to_oz)+" ounces")
    elif b == "4":
        g_to_lb = g/453.59
        print(str(g)+" grams is "+g_to_lb+" pounds")
    else:
        print("Invalid number, press enter to exit")
elif a == "3":
    print("How many oz do you want to convert?")
    oz = float(input(""))
    if b == "1":
        oz_to_kg = oz*0.02
        print(str(oz)+" ounces is "+str(oz_to_kg)+" kilograms")
    elif b =="2":
        oz_to_g = oz*28.34
        print(str(oz)+" ounces is "+str(oz_to_g)+" grams")
    elif b == "3":
        print(str(oz)+" ounces is "+str(oz)+" ounces")
    elif b == "4":
        oz_to_lb = oz/16
        print(str(oz)+" ounces is "+str(oz_to_lb)+" pounds")
    else:
        print("Invalid number, press enter to exit") 
elif a == "4":
    print("How many lb do you want to convert?")
    lb = float(input(""))
    if b == "1":
        lb_to_kg = lb/2.2
        print(str(lb)+" pounds is "+str(lb_to_kg)+" kilograms")
    elif b =="2":
        lb_to_g= lb*453.59
        print(str(lb)+" pounds is "+str(lb_to_g)+" grams")
    elif b == "3":
        lb_to_oz = lb*16
        print(str(lb)+" pounds is "+str(lb_to_oz)+" ounces")
    elif b == "4":
        #
        print(str(lb)+" pounds is "+str(lb)+" pounds")
    else:
        print("Invalid number, press enter to exit") 
else:
    print("Invalid number, press enter to exit")
input("Press enter to exit")
