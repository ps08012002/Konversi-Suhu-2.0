#Program Konversi 

import os


jawab = "y" or "Y"


while jawab == "y" or jawab == "Y" :
    

    os.system('cls')

    import Menu
    
    #INPUT DARI USER

    User = input("\nMasukkan Pilihan : ")

    if User == "1" :

        os.system('cls')

        import Teori

    # Koversi Celcius

    elif User == "2" :

        os.system('cls')

        Celcius = float (input("Suhu Dalam Celcius = "))

        print ("\nHASIL  \n")

        #Celcius Ke Reamur
        Reamur = (4/5) * Celcius
        print ("1. Reamur = ",Reamur)
    
        #Celcius Ke Fahrenheit
        Fahrenheit = (9/5) * Celcius + 32
        print ("2. Fahrenheit = ",Fahrenheit)
    
        #Celcius Ke Kelvin
        Kelvin = Celcius + 273
        print ("3. Kelvin = ",Kelvin)



    # Konversi Reamur

    elif User == "3" :

        os.system('cls')

        Reamur = float (input("Suhu Dalam Reamur = "))
    
        print ("\nHASIL  \n")
    
        #Reamur Ke Celcius
        Celcius = (5/4) * Reamur
        print ("1. Celcius = ",Celcius)
    
        #Reamur Ke Fahrenheit
        Fahrenheit = (9/4) * Reamur + 32
        print ("2. Fahrenheit = ",Fahrenheit)
    
        #Reamur Ke Kelvin
        Kelvin = (5/4) * Reamur + 273
        print ("3. Kelvin = ",Kelvin)


    # Konversi Fahrenheit

    elif User == "4" :

        os.system('cls')

        Fahrenheit = float (input("Suhu Dalam Fahrenheit = "))
    
        print ("\nHASIL  \n")
    
        #Fahrenheit Ke Celcius
        Celcius = 5/9 * (Fahrenheit - 32)
        print ("1. Celcius = ",Celcius)
    
        #Fahrenheit Ke Reamur
        Reamur = 4/9 * (Fahrenheit - 32)
        print ("2. Reamur = ",Reamur)
    
        #Fahrenheit Ke Kelvin
        Kelvin = (Fahrenheit - 32) * 5/9 + 273.15
        print ("3. Kelvin = ",Kelvin)


    # Konversi Kelvin

    elif User == "5" :

        os.system('cls')

        Kelvin = float (input("Suhu Dalam Kelvin = "))
    
        print ("\nHASIL  \n")
    
        #Kelvin Ke Celcius
        Celcius = Kelvin - 273
        print ("1. Celcius = ",Celcius)
    
        #Kelvin Ke Reamur
        Reamur = 4/5 * (Kelvin - 273)
        print ("2. Reamur = ",Reamur)
    
        #Kelvin Ke Fahrenheit
        Fahrenheit = (Kelvin - 273.15) * 9/5 + 32
        print ("3. Fahrenheit = ",Fahrenheit)

    elif User == "6" :

        print ("Makasih Udah Pakai Tools ini")

    else :
        print ("Pilihan Mu Tidak Ada Dalam Daftar")


    jawab = input ("\nMulai Lagi ? (y / t) = ")
    os.system ('cls')