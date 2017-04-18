from socket import *

server = "localhost"
port = 9000

print("Per te zgjedhur sherbimin shkruani fjalet:")
print("IP, PORT, PRINT, HOST, TIME, ZANORE, KENO, FAKTORIEL, KONVERTO ARMSTRONG, FIBONACCI, MAX, MIN, SUBNET, IPCLASS, FIZZBUZZ, VALUTA, CONSTANT dhe NUMERPRIMAR\n")

while True:
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((server,port))
    except :
        print("Lidhja nuk mund te realizohet!")
        break
    pass
    
    
    kerkesa = input("Kerkesa: ").upper()
    
    while kerkesa == "":
        print("IP, PORT, ZANORE, PRINTO, HOST, TIME, KENO, FAKTORIEL, KONVERTO, ARMSTRONG, FIBONNACI.")
        kerkesa = input("Kerkesa: ").upper()
        
    try:
        clientSocket.send(kerkesa.encode("ASCII"))
    except:
        print("Kerkesa nuk mund te dergohet!")
    pass
    

    pergjigja = clientSocket.recv(2048)

    print("Pergjigja: " + pergjigja.decode("ASCII"))
    
clientSocket.close()
