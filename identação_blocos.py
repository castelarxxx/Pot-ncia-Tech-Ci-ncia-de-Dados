#bloco em python
def sacar(self, valor: float):
    if self.saldo >= valor:
        self.saldo -= valor
        
        
#exemplo da identação 
# 
def sacar(valor):
     saldo = 500
     
     if saldo >= valor:
         print ("valor sacado")
         
         sacar (100)
         
         #EM PYTHON A IDENTAÇÃO E A IDENTIFICAÇÃO DO BLOCO É FEITA ATRAVÉS DOS ESPAÇOS, INDICADO UTILIZAR 4 ESPAÇOS EM BRANCO  POR NÍVEL DE IDENTAÇÃO, OU SEJA, A CADA NOVO BLOCO ADICIONAMOS 4 NOVOS ESPAÇOS