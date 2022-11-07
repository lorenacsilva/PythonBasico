frase = "Oi, tudo bem?"
lista_nomes = ["Joao","Maria","Guilherme","Diego"]

print(lista_nomes[0:3:2]) #vai da posicao 0 ate 3 pulando de 2 em 2

lista_nomes.append("Geralda") #adiciona sempre no ultimo lugar da lista
print(lista_nomes)

lista_nomes.insert(1,"Lorena") #Define onde quero incluir o nome
print(lista_nomes)

lista_nomes.remove("Joao") #remove nome da lista
print(lista_nomes)

lista_nomes[0] = "Roberta" #Muda o valor do indice 0
print(lista_nomes)

contador_roberta = lista_nomes.count("Roberta") #Conta quantas veze "Roberta" aparece na lista
print(contador_roberta)

lista_nomes.clear() #limpa todos os nomes da lista
print(lista_nomes)

#Atributos de string

print(len(frase)) #Conta qualquer objeto de coleção (13 caracteres)

print(frase.lower()) #frase minuscula
print(frase.upper()) #frase maiuscula
print(frase.split(",")) #separa a frase onde a gente quer (transforma lista)



