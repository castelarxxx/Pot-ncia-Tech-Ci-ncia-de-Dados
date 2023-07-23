#PARA CRIAR UMA ESTRUTURA CONDICIONAL SIMPLES, COM UM ÚNICO DESVIO, UTILIZAMOS IF. O COMANDO I´RA TESTAR A EXPRESSÃO LÓGICA, E EM CASO DE RETORNO VERDADEIRO AS AÇÕES SÃO EXECUTADAS

saldo = 2000.0
saque = float(input("informe o valor do saque:"))

if saldo >= saque: 
    print("realizando saque")
 
if saldo < saque: 
    print ("saldo insuficiente")    
    
    
    
 #para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas if e else. Como sabemos se a expressão testada no if é verdadeira, então o bloco if é executado, caso contrário o bloco de código do else é executado. 
 

#IF/ELIF/ELSE, em alguns cenarios queremos criar mais de dois desvios, para isso podemos utilizar elif. O elif é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro o bloco de código elif é executado.

opcao = int(input("Informe uma opção: [1]Sacar \n[2]Extrato:"))

if opcao == 1:
    valor = float(input("Informe a quantia para saque:"))

elif opcao == 2:
    print ("Exibindo extrato...")
else:
    sys.exit("opção inválida")
    
    
    
    
#Exemplo, estrutura condicional para maior de idade poder tirar CNH

MAIOR_IDADE = 18
IDADE_ESPECIAL = 12
idade = int(input("Informe a sua idade:"))

if idade >= MAIOR_IDADE:
    print ("Maior de idade, pode tirar a CNH.")
    
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar CNH.")
    
    
if idade >= MAIOR_IDADE:
        print ("Maior de idade, pode tirar a CNH.")   
elif idade == IDADE_ESPECIAL:
    print ("Pode fazer aulas teóricas, mas não as práticas ")
else:
    print("Ainda não pode tirar CNH")
    
    
#exemplo de saque 

conta_normal = true
conta_universitaria = false


saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print( "Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print ("Saque realizado com uso do cheque especial")
    else: 
        print( "Não foi possível realizar o saque!")
elif conta_universitaria:
        if saldo >= saque:
            print("Saque realizado com sucesso!")
        else:
            print("Saldo Insuficiente")
            
            
  # IF TERNÁRIO permite escrever uma condição de uma única linha. Ele é composto por tres parte, a primeira é o retorno caso a expressão retorne verdadeira, a segunda é a expressão lógica e a terceira é o retorno caso a expressão não seja atendida.          
saldo = 2000
saque = 500
status = "Sucesso" if saldo >= saque else "Falha"
print (f"{status} ao realizar o saque")      
            