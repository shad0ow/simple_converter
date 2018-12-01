import time
import sys
import os
import math



##Msg hat is show before quiting program
def shutdown_message():
    print ("Thank you for using my converter, I will proceed to shut down now!")
    time.sleep (2)
    sys.exit (0)
##Msg that asks user if he wants to quit
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
    distance_pick=input("Please pick one of the current convertions : \n \n1.Meters to X \n2.Inches to X \n3.Feets to X ")
    if(distance_pick=="1"):
        cls()
        distance_choice = input ("Please select which converter would you like to use ! : \n \n1.Meter to Foot \n2.Meter to Yard \n3.Meters to Inches ")
        if(distance_choice=="1"):
            meters_input=float(input("Make sure to enter distance in Meters ! : "))
            meters_to_foot = (meters_input/0.3048)
            print ("\nYou entered", meters_input , "meters, which is equal to",meters_to_foot,"foots.")
            time.sleep (3)
            cls ()
            read_carefully_message()

        elif (distance_choice == "2"):
            meters_input = float (input ("Make sure to enter distance in Meters ! : "))
            meters_to_yard = (meters_input * 1.0936)
            print ("\nYou entered", meters_input, "meters, which is equal to", meters_to_yard, "yards.")
            time.sleep (3)
            cls ()
            read_carefully_message ()

        elif(distance_choice=="3"):
            meters_input=float(input("Make sure to enter distance in Meters ! : "))
            meters_to_inches=(meters_input/0.0254)
            print ("\nYou entered", meters_input, "meters, which is equal to", meters_to_inches, "inches.")
            time.sleep(3)
            cls()
            read_carefully_message()

        else:
            shutdown_message()

    elif(distance_pick=="2"):
        cls()
        distance_choice = input("Please select which converter would you like to use ! : \n1.Inches to Feet \n2.Inches to Centimeters \n3.Inches to Yard ")
        if(distance_choice=="1"):
            cls()
            inches_input=float(input("Make sure to enter distance in Inches ! : "))
            inches_to_feet = (inches_input/12)
            print("\nYou entered", inches_input, "inches, which is equal to",inches_to_feet,"feet.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif(distance_choice=="2"):
            cls()
            inch_input=float(input("Make sure to enter distance in Inches ! : "))
            inch_to_centimeter= inch_input*(2.54/1)
            print("\nYou entered",inch_input,"inches, which is equal to",inch_to_centimeter,"centimeters.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif(distance_choice=="3"):
            cls()
            inches_input=float(input("Make sure to enter distance in Inches ! : "))
            inches_to_yard=(inches_input*0.027778)
            print("\nYou entered",inches_input,"which is equal to",inches_to_yard,"yards.")
            time.sleep(3)
            cls()
            read_carefully_message()

    elif(distance_pick=="3"):
        cls()
        distance_choice = input("Please select which converter would you like to use ! : \n1.Feet to Meter \n2.Feet to Inches \n3.Feet to Miles ")
        if (distance_choice == "1") :
            cls()
            feet_input = float(input("Make sure to enter distance in Feet ! : "))
            feet_to_meter = (feet_input/3.2808)
            print("\nYou entered",feet_input,"which is equal to ",feet_to_meter,"meters.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif (distance_choice == "2"):
            cls()
            feet_input = float(input("Make sure to enter distance in Feet ! : "))
            feet_to_inches = (feet_input*12.000)
            print("\nYou entered",feet_input,"which is equal to",feet_to_inches,"inches.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif (distance_choice == "3") :
            cls()
            feet_input = float(input("Make sure to enter distance in Feet ! : "))
            feet_to_miles = (feet_input*0.00018939)
            print("\nYou entered",feet_input,"which is equal to",feet_to_miles,"miles.")
            time.sleep(3)
            cls()
            read_carefully_message()

    else:
        shutdown_message()
##Clears screen
def cls():
    print ("\n" * 50)
def main_menu():
    cls()
    print('Here are three options to choose from :\n \n1.Weight \n2.Distance')
    user_choice1=(input("\nPlease enter number in front of unit that you wish to use or type shutdown to exit: "))

    if(user_choice1=="1"):
        cls()
        weight_converter()

    elif(user_choice1=="2"):
        cls()
        distance_converter()
    else:
        shutdown_message()
def weight_converter():
    cls()
    print("\nYou've selected Weight converter.")
    time.sleep(1)

    weight_pick=input("Please pick one of the current convertions ! : \n \n1.Grams to X \n2.Decagrams to X \n3.Kilograms to X ")
    if(weight_pick=="1"):
        cls()
        weight_choice=input("Please select which converter would you like to use ! : \n \n1.Grams to Kilograms \n2.Grams to Decagrams \n3.Grams to Oz ")
        if(weight_choice=="1"):
            grams_input=float(input("Make sure to enter weight in Grams ! : "))
            grams_converted_to_kilos = (1 * (grams_input / 1000))
            print("\nYou entered",grams_input,"grams which is equal to",grams_converted_to_kilos,"kilograms.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif(weight_choice=="2"):
            grams_input=float(input("Make sure to enter weight in Grams ! : "))
            grams_converted_to_decas = (1* (grams_input/10))
            print ("\nYou entered", grams_input, "grams which is equal to", grams_converted_to_decas, "decagrams.")
            time.sleep (3)
            cls ()
            read_carefully_message()

        elif(weight_choice=="3"):
            gram_input=float(input("Make sure to enter weight in grams ! : "))
            grams_to_oz = (gram_input* (1/28.34952313))
            print ("\nYou entered", gram_input, "grams which is equal to", grams_to_oz, "Oz.")
            time.sleep(3)
            cls ()
            read_carefully_message()


    elif(weight_pick=="2"):
        cls()
        weight_choice = input("Please select which converter would you like to use ! : \n \n1.Decagrams to Grams \n2.Decagrams to Pounds \n3.Decagram to Oz ")
        if(weight_choice=="1"):
            decagram_input=float(input("Make sure to enter weight in decagrams ! : "))
            decagram_to_grams= (1*(10/decagram_input))
            print ("\nYou entered", decagram_input, "decagram which is equal to", decagram_to_grams, "grams.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif(weight_choice=="2"):
            decagram_input=float(input("Make sure to enter weight in decagrams ! : "))
            decagram_to_pounds=(decagram_input*(1/45.359237))
            print("\nYou entered",decagram_input,"which is equal to",decagram_to_pounds,"pounds.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif(weight_choice=="3"):
            decagram_input=float(input("Make sure to enter weight in decagrams ! : "))
            decagram_to_oz=(decagram_input*(1/2.83495231))
            print("\nYou entered",decagram_input,"which is equal to",decagram_to_oz,"Oz.")
            time.sleep(3)
            cls()
            read_carefully_message()

    elif(weight_pick=="3"):
        cls()
        weight_choice=input("Please select which converter would you like to use ! : \n \n1.Kilograms to Grams \n2.Kilogram to Pounds \n3.Kilogram to Oz ")
        if(weight_choice=="1"):
            kilogram_input=float(input("Make sure to enter weight in kilogram ! : "))
            kilo_to_gram=(kilogram_input*1000)
            print("\nYou entered",kilogram_input,"which is equal to",kilo_to_gram,"grams.")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif(weight_choice=="2"):
            kilogram_input=float(input("Make sure to enter weight in kilogram ! : "))
            kilo_to_pounds=(kilogram_input*2.2046)
            print("\nYou entered",kilogram_input,"which is equal to",kilo_to_pounds,"pounds")
            time.sleep(3)
            cls()
            read_carefully_message()

        elif(weight_choice=="3"):
            kilogram_input=float(input("Make sure to enter weight in kilogram ! : "))
            kilo_to_oz=(kilogram_input*35.274)
            print("\nYou entered",kilogram_input,"which is equal to",kilo_to_oz,"Oz.")
            time.sleep(3)
            cls()
            read_carefully_message()
    else:
        shutdown_message()


print("-------------------------------------------------")
print("Simple unit converter made by github.com/shad0ow")
print("-------------------------------------------------")
time.sleep(2)
print("More items will be added later.")
print("\nTell me if you are ready to start, OK?")

user_choice=input("Type YES if you agree to start or NO to stop : ")

if(user_choice=="YES" or user_choice=="yes"):
    print("Good, we can start now !")
    time.sleep(3)
    main_menu ()
else:
    shutdown_message()
