#Metodo 1 old style utilizando %
nome = "Hilary"
idade = 19
profissao = "programador"
linguagem = "Python"

print ( "Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou fazendo curso de %s" %(nome, idade, profissao, linguagem))

#S para string, D para numero flutuante, chama as variaveis na ordem .
#Metodo Format 
nome = "Hilary"
idade = 19
profissao = "programador"
linguagem = "Python"
print ("Olá, me chamo {}. Eu tenho {} de idae. Trabalho como {} e estou fazendo o curso de {}".format(nome, idade, profissao, linguagem)) 
#ou pode colocar a forma da oordem da variavel 
nome = "Hilary"
idade = 19
profissao = "programador"
linguagem = "Python"
print ("Olá, me chamo {3} Eu tenho {2} de idae. Trabalho como {1} e estou fazendo o curso de {0}".format(nome, idade, profissao, linguagem).format(linguagem,profissao, idade, nome)) 
#metodo f-string
nome = "Hilary"
idade = 19
profissao = "programador"
linguagem = "Python"
print(f"Olá, me chamo {nome} Eu tenho {idade} de idae. Trabalho como {profissao} e estou fazendo o curso de {linguagem}.")
#formatar strings com f-string
PI = 3.14159
print(f"valor de PI{PI:2f}")
# 2 f para exibir apenas duas casas por ser um numero grande