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
    
    
    try:
        serverSocket.sendto(pergjigja.encode("ASCII"), clientAddress)
        print( clientAddress[0] + ":" + str(clientAddress[1]) + " Pergjigja " + kushti.split(" ")[0] + " eshte derguar...")
    except:
        print(clientAddress[0] + ":" + str(clientAddress[1]) + " Pergjigja nuk mund te dergohet!")
        pass
