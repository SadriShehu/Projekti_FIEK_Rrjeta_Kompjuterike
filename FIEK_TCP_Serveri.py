from socket import *
import platform  
from time import gmtime, strftime 
import random 
port = 9000

serverSocket = socket(AF_INET, SOCK_STREAM)

try:
    serverSocket.bind(('',port))
    serverSocket.listen()
    kondita = True
except:
    print("Vetem nje instance e serverit eshte e lejuar!")
    kondita = False
    pass

if kondita:
    print("FIEK TCP Serveri eshte i gatshem...\n")
else:
    print("FIEK TCP Serveri nuk mund te starohet!")

while kondita:
    try:
        connectionSocket, adresa = serverSocket.accept()
        kerkesa = connectionSocket.recv(2048)

        kushti = kerkesa.decode("ASCII")

        socketName = socket.getsockname(connectionSocket)
        print( socketName[0] + ":" + str(socketName[1]) + " Kerkesa " + kushti.split(" ")[0] + " eshte pranuar...")
    except:
        continue
        pass


    if kushti == "IP":
        pergjigja =  "IP adresa e klientit eshte " + socketName[0]
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
        elif kushti[0:11] == "NUMERPRIMAR":
        if kushti[11:12] == " ":
            pergjigja = ""
            for i in range(0,int(kushti[12:len(kushti)])):
                if i > 1:
                     for j in range(2,i):
                            if (i % j) == 0:
                            break
                        else:
                        pergjigja += "\n" + str(i)
        else:
            pergjigja = "Formati: NUMERPRIMAR [Numri deri te i cili do te gjenerohen N.P.]"
             elif kushti[0:8] == "CONSTANT":
        if kushti[8:9] == " ":
            if kushti[9:len(kushti)] == "PI":
                pergjigja = str(math.pi)
            elif kushti[9:len(kushti)] == "E":
                pergjigja = str(math.e)
            elif kushti[9:len(kushti)] == "TAU":
                pergjigja = str(math.tau)
            elif kushti[9:len(kushti)] == "SQRT2":
                pergjigja = str(math.sqrt(2))
            elif kushti[9:len(kushti)] == "SQRT3":
                pergjigja = str(math.sqrt(3))
        else:
            pergjigja = "Formati: CONSTANT [KONSTANTA]\n TE NJOHURA: \nPI \n E \n TAU \n SQRT2 \n SQRT3"
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
        else:
        pergjigja = "Shenoni njeren nga sherbimet tona: IP, PORT, ZANORE, PRINTO, HOST, TIME, KENO, FAKTORIEL, KONVERTO, ARMSTRONG, FIBONNACI."

        
        
        
    
    try:
        connectionSocket.send(pergjigja.encode("ASCII"))
        print( socketName[0] + ":" + str(socketName[1]) + " Pergjigja " + kushti.split(" ")[0] + " eshte derguar...")
    except:
        print(socketName[0] + ":" + str(socketName[1]) + " Pergjigja nuk mund te dergohet!")
        pass        
