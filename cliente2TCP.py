import socket
from threading import Thread
HOST='localhost'
PORT = 6012       # Porta que o Servidor esta
tcp2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp2.connect(dest)



print(tcp2.getsockname())
voce=input("Digite seu nome:")

def envia():

    destinatario = input("Para:")
    assunto = input("assunto(opcional):")
    mensagem = input("mensagem:")
    if destinatario == '':
        print("faltou o destinatario")
        envia()
    msg = voce + '\n' + destinatario + '\n' + assunto + '\n' + mensagem +'\n'
    tcp2.send(bytes(msg,'utf-8'))

def recebe():
    tex,orig=tcp2.recvfrom(1024)
    tex = tex.decode('utf-8')
    texto = tex.split('\n')


    if texto[1] == voce:
        print(f"De:{texto[0]}\nPara:{voce}\nAssunto:{texto[2]}\nMensagem:{texto[3]}\n")
    elif len(texto)>5:
            if texto[5]==voce:
                print(f"De:{texto[4]}\nPara:{voce}\nAssunto:{texto[6]}\nMensagem:{texto[7]}\n")

while True:

    manda = Thread(target=envia())
    manda.start()


    chego = Thread(target=recebe())
    chego.start()

tcp2.close()