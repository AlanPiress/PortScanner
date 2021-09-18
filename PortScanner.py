import socket
import sys

print ("\n\nO Escaneamento pode levar \nalguns minutos, Aguarde!\n")

print ("========================")

#Caso queira fazer uma varredura geral,utilize:
for porta in range (0, 50000):

#Caso queira fazer uma varredura de portas epecíficas, utilize:
#portas= [21, 22, 23, 80, 587]
#for porta in portas:
    sr= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sr.settimeout(0.0001)
    if sr.connect_ex((sys.argv[1], porta))== 0:
        print ("Porta",porta,"--> aberta!")
        sr.close()

print ("========================") 
print ("\nEscaneamento Finalizado!\n\n")