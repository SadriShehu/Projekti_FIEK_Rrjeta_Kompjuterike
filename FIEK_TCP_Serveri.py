from socket import *

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
        
        
        
        
        
    
    try:
        connectionSocket.send(pergjigja.encode("ASCII"))
        print( socketName[0] + ":" + str(socketName[1]) + " Pergjigja " + kushti.split(" ")[0] + " eshte derguar...")
    except:
        print(socketName[0] + ":" + str(socketName[1]) + " Pergjigja nuk mund te dergohet!")
        pass        
