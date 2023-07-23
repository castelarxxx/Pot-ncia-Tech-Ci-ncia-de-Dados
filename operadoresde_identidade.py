#operadores utilizados para comparar se os dois objetos testados ocupam o mesma posição na memória 

curso = "curso de python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso
#retorna true

curso is not nome_curso
#retorna false

saldo is limite 
#retorna true


#exemplo teste

saldo = 1000
limite = 1000
print (saldo is limite)
print (saldo is not limite)