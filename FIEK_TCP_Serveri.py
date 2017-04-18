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

        
        
        
    
    try:
        connectionSocket.send(pergjigja.encode("ASCII"))
        print( socketName[0] + ":" + str(socketName[1]) + " Pergjigja " + kushti.split(" ")[0] + " eshte derguar...")
    except:
        print(socketName[0] + ":" + str(socketName[1]) + " Pergjigja nuk mund te dergohet!")
        pass        
