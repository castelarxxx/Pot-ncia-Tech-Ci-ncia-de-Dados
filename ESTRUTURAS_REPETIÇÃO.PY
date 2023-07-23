#SÃO ESTRUTURAS UTILIZADAS PARA REPETIR UM TRECHO DE CÓDIGO UM DETERMINADO NUMERO DE VEZES


#EXEMPLO SEM REPETIÇÃO

a = int(input("iNFORME UM NUMERO INTEIRO:"))
print (a)

a += 1
print(a)

a += 1
print(a)   


#COMANDO FOR É USADO PARA PERCORRER UM OBJETO ITERÁVEL FAZ SEBTIDO USAR QUANDO SABEMOS O NUMERO EXATO DE VEZES QUE NOSSO BLOCO VAI SER EXECUTADO, OU QUANDO QUERERMOS PERCORRER ESSE OBJETO
#exemplo de programa separando as vogais

texto = input("Informe um texto:")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
        
print()

#FOR/ELSE

texto = input("Informe um texto:")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
    else: 
print()
print("executa no final do laço")



#RANGE
#RANGE (STOP) -> RANGE OBJECT
# RANGE (START, STOP[, STEP])-> RANGE OBJECT

list(range(4))
#retorna a lista [0,1,2,3]



#Utilizando Range com FOR

#for numero in range (0, 11):
#print(numero, end=" ")


#exibindo a tabuada do 5

for numero in range (0, 51, 5):
    print(numero, end=" ")
    
    
#COMANDO WHILE É UTILIZADO PARA REPETIR UM BLOCO DE CODIGO VARIAS VEZES, FAZ SENTIDO UTILIZAR WHILE QUANDO NÃO SABEMOS O NUMERO EXATO DE VEZES QUE O NOSSO BLOCO SERA EXECUTADO 

opcao = -1

while opcao != 0:
    opcao = int(input("[1]SACAR \n[2]Extrato \n[3] Sair"))
    
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print ("Exibindo extrato...")
        
#break 
#programa que se o numero for maior que 10 ele para

while True:
    numero = int(input("Informe um numero:"))
    if numero ==10;
    break
print(numero)


#