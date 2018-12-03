import time
import sys


def shutdown_message():
    print ("Thank you for using my converter, I will proceed to shut down now!")
    time.sleep (2)
    sys.exit (0)
def read_carefully_message():
    print ("Please read this carefully !")
    time.sleep (1)
    main_menu_ask = str (
        input ("\nDo you want to back to Main Menu or would you like to shut down?(type Main or shutdown) : "))
    if (main_menu_ask == "Main" or main_menu_ask == "main"):
        return main_menu ()
    else:
        shutdown_message()
def distance_converter():
    cls ()
    print ("\nYou've selected Distance converter.")
    time.sleep (1)
    ##Gives user multiple choice to pick
    distance_pick=input("Please pick one of the current convertions : \n \n1.Meters to X \n2.Inches to X \n3.Feets to X  \n\nYour choice : ")
    if(distance_pick=="1"):
        cls()
        distance_choice = input ("Please select which converter would you like to use ! \n \n1.Meter to Foot \n2.Meter to Yard \n3.Meters to Inches \n\nYour choice : ")
        if(distance_choice=="1"):
            meters_input = float (input ("Make sure to enter distance in Meters ! : "))
            meters_to_foot = (meters_input / 0.3048)
            print( "\nYou entered", meters_input, "Meters, which is equal to", meters_to_foot, "Foots.")
            time.sleep (3)
            cls ()
            read_carefully_message ()

        elif (distance_choice == "2"):
            meters_input = float (input ("Make sure to enter distance in Meters ! : "))
            meters_to_yard = (meters_input * 1.0936)
            print ("\nYou entered", meters_input, "Meters, which is equal to", meters_to_yard, "Yards.")
            time.sleep (3)
            cls ()
            read_carefully_message ()

        elif(distance_choice=="3"):
            meters_input=float(input("Make sure to enter distance in Meters ! : "))
            meters_to_inches=(meters_input/0.0254)
            print ("\nYou entered", meters_input, "Meters, which is equal to", meters_to_inches, "Inches.")
            time.sleep(3)
            cls()
            read_carefully_message()

        else:
            shutdown_message()

    elif(distance_pick=="2"):
        cls()
        distance_choice = input("Please select which converter would you like to use ! \n \n1.Inches to Feet \n2.Inches to Centimeters \n3.Inches to Yard \n\nYour choice : ")
        if(distance_choice=="1"):
            cls()
            inches_input=float(input("Make sure to enter distance in Inches ! : "))
            inches_to_feet = (inches_input/12)
            print("\nYou entered", inches_input, "Inches, which is equal to",inches_to_feet,"Feets.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif(distance_choice=="2"):
            cls()
            inch_input=float(input("Make sure to enter distance in Inches ! : "))
            inch_to_centimeter= inch_input*(2.54/1)
            print("\nYou entered",inch_input,"Inches, which is equal to",inch_to_centimeter,"Centimeters.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif(distance_choice=="3"):
            cls()
            inches_input=float(input("Make sure to enter distance in Inches ! : "))
            inches_to_yard=(inches_input*0.027778)
            print("\nYou entered",inches_input,"Inches, which is equal to",inches_to_yard,"Yards.")
            time.sleep(3)
            cls()
            read_carefully_message()

    elif(distance_pick=="3"):
        cls()
        distance_choice = input("Please select which converter would you like to use ! \n \n1.Feet to Meter \n2.Feet to Inches \n3.Feet to Miles \n\nYour choice : ")
        if (distance_choice == "1") :
            cls()
            feet_input = float(input("Make sure to enter distance in Feet ! : "))
            feet_to_meter = (feet_input/3.2808)
            print("\nYou entered",feet_input,"Feets, which is equal to ",feet_to_meter,"Meters.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif (distance_choice == "2"):
            cls()
            feet_input = float(input("Make sure to enter distance in Feet ! : "))
            feet_to_inches = (feet_input*12.000)
            print("\nYou entered",feet_input,"Feets, which is equal to",feet_to_inches,"Inches.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif (distance_choice == "3") :
            cls()
            feet_input = float(input("Make sure to enter distance in Feet ! : "))
            feet_to_miles = (feet_input*0.00018939)
            print("\nYou entered",feet_input,"Feets, which is equal to",feet_to_miles,"Miles.")
            time.sleep(3)
            cls()
            read_carefully_message()

    else:
        shutdown_message()
def cls():
    print ("\n" * 50)
def main_menu():
    cls()
    print('Here are three options to choose from :\n \n1.Weight \n2.Distance \n3.Volume ')
    user_choice1=(input("\nPlease enter number in front of unit that you wish to use or type shutdown to exit: "))

    if(user_choice1=="1"):
        cls()
        weight_converter()

    elif(user_choice1=="2"):
        cls()
        distance_converter()

    elif(user_choice1=="3"):
        cls()
        volume_converter()

    else:
        cls()
        shutdown_message()
def weight_converter():
    cls()
    print("\nYou've selected Weight converter.")
    time.sleep(1)

    weight_pick = input("Please pick one of the current convertions ! \n \n1.Grams to X \n2.Decagrams to X \n3.Kilograms to X \n\nYour choice : ")
    if(weight_pick=="1"):
        cls()
        weight_choice=input("Please select which converter would you like to use ! \n1.Grams to Kilograms \n2.Grams to Decagrams \n3.Grams to Oz \n\nYour choice :  ")
        if(weight_choice=="1"):
            grams_input=float(input("Make sure to enter weight in Grams ! : "))
            grams_converted_to_kilos = (1 * (grams_input / 1000))
            print("\nYou entered",grams_input,"Grams, which is equal to",grams_converted_to_kilos,"Kilograms.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif(weight_choice=="2"):
            grams_input=float(input("Make sure to enter weight in Grams ! : "))
            grams_converted_to_decas = (1* (grams_input/10))
            print ("\nYou entered", grams_input, "Grams, which is equal to", grams_converted_to_decas, "Decagrams.")
            time.sleep (3)
            cls ()
            read_carefully_message()

        elif(weight_choice=="3"):
            gram_input=float(input("Make sure to enter weight in grams ! : "))
            grams_to_oz = (gram_input* (1/28.34952313))
            print ("\nYou entered", gram_input, "Grams, which is equal to", grams_to_oz, "Oz.")
            time.sleep(3)
            cls ()
            read_carefully_message()

    elif(weight_pick=="2"):
        cls()
        weight_choice = input("Please select which converter would you like to use ! \n \n1.Decagrams to Grams \n2.Decagrams to Pounds \n3.Decagram to Oz \n\nYour choice :  ")
        if(weight_choice=="1"):
            decagram_input=float(input("Make sure to enter weight in decagrams ! : "))
            decagram_to_grams= (1*(10/decagram_input))
            print ("\nYou entered", decagram_input, "Decagrams, which is equal to", decagram_to_grams, "Grams.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif(weight_choice=="2"):
            decagram_input=float(input("Make sure to enter weight in decagrams ! : "))
            decagram_to_pounds=(decagram_input*(1/45.359237))
            print("\nYou entered",decagram_input,"Decagrams, which is equal to",decagram_to_pounds,"Pounds.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif(weight_choice=="3"):
            decagram_input=float(input("Make sure to enter weight in decagrams ! : "))
            decagram_to_oz=(decagram_input*(1/2.83495231))
            print("\nYou entered",decagram_input,"Decagrams, which is equal to",decagram_to_oz,"Oz.")
            time.sleep(3)
            cls()
            read_carefully_message()

    elif(weight_pick=="3"):
        cls()
        weight_choice=input("Please select which converter would you like to use ! \n  \n1.Kilograms to Grams \n2.Kilogram to Pounds \n3.Kilogram to Oz \n\nYour choice : ")
        if(weight_choice=="1"):
            kilogram_input=float(input("Make sure to enter weight in kilogram ! : "))
            kilo_to_gram=(kilogram_input*1000)
            print("\nYou entered",kilogram_input,"Kilograms, which is equal to",kilo_to_gram,"Grams.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif(weight_choice=="2"):
            kilogram_input=float(input("Make sure to enter weight in kilogram ! : "))
            kilo_to_pounds=(kilogram_input*2.2046)
            print("\nYou entered",kilogram_input,"Kilograms, which is equal to",kilo_to_pounds,"Pounds")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif(weight_choice=="3"):
            kilogram_input=float(input("Make sure to enter weight in kilogram ! : "))
            kilo_to_oz=(kilogram_input*35.274)
            print("\nYou entered",kilogram_input,"Kilograms, which is equal to",kilo_to_oz,"Oz.")
            time.sleep(3)
            cls()
            read_carefully_message()

    else:
        shutdown_message()


def volume_converter():
    cls ()
    print ("\nYou've selected Weight converter.")
    time.sleep (1)

    volume_pick=input("Please pick one of the current convertions !\n  \n1.Liters to X \n2.Cubic Meter to X \n3.Cubic Yards to X \n\nYour choice : ")
    if(volume_pick=="1"):
        cls()
        volume_choice=input("Please select which converter would you like to use ! \n  \n1.Liter to US Gallon \n2.Liter to US Barrels \n3.Liter to UK Gallon \n\nYour choice : ")
        if(volume_choice=="1"):
            liters_input=float(input("Make sure to enter volume in Liters ! : "))
            liter_2_usgallon=(liters_input*0.26417)
            print("\nYou entered",liters_input,"Liters, which is equal to",liter_2_usgallon,"US Gallons.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif(volume_choice=="2"):
            liters_input=float(input("Make sure to enter volume in Liters ! : "))
            liters_to_usbarrel=(liters_input*0.0062898)
            print("\nYou entered",liters_input,"Liters, which is equal to",liters_to_usbarrel,"US Barrels.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif(volume_choice=="3"):
            liters_input=float(input("Make sure to enter volume in Liters ! : "))
            liters_to_ukgallon=(liters_input*0.21997)
            print("\nYou entered",liters_input,"Liters, which is equal to",liters_to_ukgallon,"UK Gallons.")
            time.sleep(3)
            cls()
            read_carefully_message()

    elif(volume_pick=="2"):
        cls()
        volume_choice=input("Please select which converter would you like to use ! \n \n1.Cubic Meter to Liter \n2.Cubic Meter to Cubic Feet \n3.Cubic Meter to Cubic Centimeters")
        if(volume_choice=="1"):
            cubic_input=float(input("Make sure to enter volume in Cubic Meters ! : "))
            cubicM_to_liter=((cubic_input**3)/0.0010000)
            print("\nYou entered",cubic_input,"Cubic Meters, which is equal to",cubicM_to_liter,"Liters.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif(volume_choice=="2"):
            cubic_input=float (input ("Make sure to enter volume in Cubic Meters ! : "))
            cubicM_to_cubicF=((cubic_input**3)*35.315)
            print("\nYou entered",cubic_input,"Cubic Meters, which is equal to",cubicM_to_cubicF,"Cubic Feets.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif(volume_choice=="3"):
            cubic_input=float(input("Make sure to enter volume in Cubic Meters ! : "))
            cubicM_to_cubicC=((cubic_input)/0.0000010000)
            print("\nYou entered",cubic_input,"Cubic Meters, which is equal to",cubicM_to_cubicC,"Cubic Centimeters.")
            time.sleep(3)
            cls()
            read_carefully_message()

    elif(volume_pick=="3") :
        cls()
        volume_choice=input("Please select which converter would you like to use ! \n \n1.Cubic Yards to Liter \n2.Cubic Yards Cubic Feet \n3.Cubic Yards to Cubic Meters")
        if(volume_choice=="1"):
            cubicY_input=float(input("Make sure to enter volume in Cubic Yards ! : "))
            cubicY_to_liter=cubicY_input/0.0013080
            print("\nYou entered",cubicY_input,"Cubic Yards, which is equal to",cubicY_to_liter,"Liters.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif(volume_choice=="2"):
            cubicY_input=float(input("Make sure to enter volume in Cubic Yards ! : "))
            cubicY_to_cubicC=((cubicY_input**3)*27.000)
            print("\nYou entered",cubicY_input,"Cubic Yards, which is equal to",cubicY_to_cubicC,"Cubic Feets.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif(volume_choice=="3"):
            cubicY_input=float(input("Make sure to enter volume in Cubic Yards ! :"))
            cubicY_to_cubicM=((cubicY_input**3)/1.3080)
            print("\nYou entered",cubicY_input,"Cubic Yards, which is equal to",cubicY_to_cubicM,"Cubic Meters.")
            time.sleep(3)
            cls()
            read_carefully_message()


print("--------------------------------------------------")
print("|Simple unit converter made by github.com/shad0ow|")
print("--------------------------------------------------")
time.sleep(2)
print("Version 1.0")
print("\nTell me if you are ready to start, OK?")

user_choice=input("Type YES if you agree to start or NO to stop : ")

if(user_choice=="YES" or user_choice=="yes"):
    print("Good, we can start now !")
    time.sleep(3)
    main_menu ()
else:
    shutdown_message()
