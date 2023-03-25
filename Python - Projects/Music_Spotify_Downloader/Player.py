from spotdl import Spotdl

clientId = str(input('Digite seu endereço de Client_Local: '))
clientSecret = str(input('Digite seu endereço de Client_Secreto: '))

lista = []

link = str(input('Digite o link da musica: '))
lista.append(link)

client = Spotdl(client_id=clientId, client_secret=clientSecret)

musica = client.search(lista)

musica = client.download(musica[0])
