saldo = 1000
saque = 200
limite = 100

saldo <= saque #retorna true
saldo <= limite #retorna false


#Operador E
saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite
#expressão retorna False
 
 
 #Operador OR
saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite
#expressão retorna True
 
 
 #Operador de negação 

contatos_emergencia = []
not 1000 > 15000 #true
 
not contatos_emergencia #true
 
not "saque 1500;"
 #false
not ""
 #true
 
 
 
 #Parenteses
 
saldo = 1000
saque = 200
limite = 100
conta_especial = true
saldo >= saque and saque <= limite or conta_especial and saldo >= saque #true
#melhorando para a resolução de expressões com parenteses
(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) #true


#resumo
#AND = PARA SER TRUE TUDO TEM QUE SER TRUE
#OR = PARA SER TRUE APENAS UM TEM QUE SER TRUE
#