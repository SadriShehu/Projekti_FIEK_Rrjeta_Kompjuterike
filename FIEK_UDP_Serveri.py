from socket import *

port = 9000

serverSocket = socket(AF_INET, SOCK_DGRAM)

try:
    serverSocket.bind(('',port))
    kondita = True
except:
    print("Vetem nje instance e serverit eshte e lejuar!")
    kondita = False
    pass

if kondita:
    print("FIEK UDP Serveri eshte i gatshem...\n")

while kondita:
    try:
        kerkesa, clientAddress = serverSocket.recvfrom(2048)
        kushti = kerkesa.decode("ASCII")
        socketName = socket.getsockname(serverSocket)
        print(str(clientAddress[0]) + ":" + str(clientAddress[1]) + " Kerkesa " + kushti.split(" ")[0] + " eshte pranuar...")
    except:
        continue
        pass

    if kushti == "IP":
        pergjigja =  "IP adresa e klientit eshte " + str(clientAddress[0])
    elif kushti == "PORT":
        pergjigja = "Klienti eshte duke perdorur portin " + str(socketName[1])
    elif kushti[0:6] == "ZANORE":
        if kushti[0:7] == "ZANORE ":
            string = kushti[7:len(kushti)]
            string = string.replace(" ", "")
            numri_zanoreve = 0
            for i in string:
                if i == 'A' or i == 'E' or i == 'U' or i == 'O' or i == 'Y' or i == 'I':
                     numri_zanoreve += 1

            pergjigja = " Teksti derguar permban " + str(numri_zanoreve) + " zanore.  "
        else:
            pergjigja = "Formati: ZANORE [teksti]";
    elif kushti[0:6] == "PRINTO":
        if kushti[0:7] == "PRINTO ":
            pergjigja = kushti[7:len(kushti)].lower().capitalize()
        else:
            pergjigja = "Formati: PRINTO [teksti]";
            
            
            
            
    elif kushti[0:8] == "KONVERTO":
        if kushti[8:9] == " ":
            string = kushti.split(" ")
            if string[1] == '1':
                pergjigja = str(float(string[2]) + 273.15)
            elif string[1] == '2':
                pergjigja = str(float(string[2]) * 1.8 + 32)
            elif string[1] == '3':
                pergjigja = str(float(string[2]) * 9 / 5 - 459.67)
            elif string[1] == '4':
                pergjigja = str(float(string[2]) - 273.15)
            elif string[1] == '5':
                pergjigja = str((float(string[2]) - 32) / 1.8)
            elif string[1] == '6':
                pergjigja = str(float(string[2]) + 459.67)
            elif string[1] == '7':
                pergjigja = str(float(string[2]) / 2.2046)
            elif string[1] == '8':
                pergjigja = str(float(string[2]) * 2.2046)
        else:
            pergjigja = "Formati: KONVERTO [NUMRI I OPERACIONI] [VLERA PER KONVERTIM]"
            pergjigja += "\nZgjedh njerin nga OPERACIONET:"
            pergjigja += "\n1 - CelsiusToKelvin"
            pergjigja += "\n2 - CelsiusToFahrenheit" 
            pergjigja += "\n3 - KelvinToFahrenheit" 
            pergjigja += "\n4 - KelvinToCelsius"
            pergjigja += "\n5 - FahrenheitToCelsius"
            pergjigja += "\n6 - FahrenheitToKelvin"
            pergjigja += "\n7 - PoundToKilogram"
            pergjigja += "\n8 - KilogramToPound"

    elif kushti[0:9] == "FAKTORIEL":
        if kushti[9:10] == " ":
            pergjigja = str(math.factorial(int(kushti[10:len(kushti)])))
        else:
            pergjigja = "Formati: FAKTORIEL [numri]";

    elif kushti[0:9] == "ARMSTRONG":
        if kushti[9:10] == " ":
            shuma = 0
            i = int(kushti[10:len(kushti)])
            while i>0:
                mod10 = i % 10
                shuma += math.pow(mod10, 3)
                i //= 10
            if shuma == int(kushti[10:len(kushti)]):
                pergjigja = "Numri i dhene eshte numer ARMSTRONG"
            else:
                pergjigja = "Numri i dhene nuk eshte numer ARMSTRONG"
        else:
            pergjigja = "Formati: ARMSTRONG [numri]";

    elif kushti[0:9] =="FIBONNACI":
        ardhshme = 1 
        paraprake = -1
        if kushti[9:10] == " ":
            for i in range(0, int(kushti[10:len(kushti)])):
                shuma = ardhshme + paraprake
                paraprake = ardhshme
                ardhshme = shuma
            pergjigja = str(shuma)
        else:
            pergjigja = "Formati: FIBONNACI [numri]";

    else:
        pergjigja = "Shenoni njeren nga sherbimet tona: IP, PORT, ZANORE, PRINTO, HOST, TIME, KENO, FAKTORIEL, KONVERTO, ARMSTRONG, FIBONNACI."
    
    
    try:
        serverSocket.sendto(pergjigja.encode("ASCII"), clientAddress)
        print( clientAddress[0] + ":" + str(clientAddress[1]) + " Pergjigja " + kushti.split(" ")[0] + " eshte derguar...")
    except:
        print(clientAddress[0] + ":" + str(clientAddress[1]) + " Pergjigja nuk mund te dergohet!")
        pass
