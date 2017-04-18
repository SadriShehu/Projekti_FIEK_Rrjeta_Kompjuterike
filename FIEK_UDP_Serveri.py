from socket import *
import platform 
from time import gmtime, strftime
import random 
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
                elif kushti == "HOST":
        try:
            h = platform.uname()[1]
            pergjigja = "Emri i klientit eshte " + h
        except:
            pergjigja = "Emri i klientit nuk dihet"
    elif kushti == "TIME":
        pergjigja = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    elif kushti == "KENO": 
        array = []
        for i in range(0, 20):
            array.append(random.randint(1,80))
        array.sort()
        pergjigja = str(array)[1:-1]
    elif kushti[0:8] == "FIZZBUZZ":
        if kushti[8:9] == " ":
            numri = int(kushti[9:len(kushti)])
        if numri % 5 == 0 and numri % 3 == 0:
            pergjigja = "FizzBuzz"
        elif numri % 3 == 0:
            pergjigja = "Fizz"
        elif numri % 5 == 0:
            pergjigja = "Buzz"
        else:
            pergjigja = "Nuk keni japur numer te vlefshem!"
    elif kushti[0:6] == "VALUTA":
        if kushti[6:7] == " ":
            string = kushti.split(" ")
            if string[1] == '1':
                pergjigja = str(round(float(string[2]) * 1.06, 2))
            elif string[1] == '2':
                pergjigja = str(round(float(string[2]) * 0.94, 2))
            elif string[1] == '3':
                pergjigja = str(round(float(string[2]) * 1.07, 2))
            elif string[1] == '4':
                pergjigja = str(round(float(string[2]) * 0.94, 2))
            elif string[1] == '5':
                pergjigja = str(round(float(string[2]) * 0.85, 2))
            elif string[1] == '6':
                pergjigja = str(round(float(string[2]) * 1.18, 2))
        else:
            pergjigja = "Formati: VALUTA [NUMRI I OPERACIONI] [VLERA PER KONVERTIM]"
            pergjigja += "\nZgjedh njerin nga OPERACIONET:"
            pergjigja += "\n1 - EurToUSD"
            pergjigja += "\n2 - USDToEur" 
            pergjigja += "\n3 - EurToCHF" 
            pergjigja += "\n4 - CHFToEur"
            pergjigja += "\n5 - EurToGBP"
            pergjigja += "\n6 - GBPToEur"
    
    
    try:
        serverSocket.sendto(pergjigja.encode("ASCII"), clientAddress)
        print( clientAddress[0] + ":" + str(clientAddress[1]) + " Pergjigja " + kushti.split(" ")[0] + " eshte derguar...")
    except:
        print(clientAddress[0] + ":" + str(clientAddress[1]) + " Pergjigja nuk mund te dergohet!")
        pass
