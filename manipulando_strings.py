# MAIUSCULA MINUSCULA E TITULO

curso = "pYthon"

print (curso.upper())
#PYTHON

print (curso.lower())
#python

print (curso.title())
#Python 



#Eliminando espaços em branco

curso = "python"

print (curso.strip())
#"python"

print (curso.lstrip())
 #"python "
 
print (curso.rstrip())
 #"  python "
 
 
 #Junções e centralização de strings
 
curso = "Python"

print (curso.center(10,"#"))
#"##Python##"
print(".".join(curso))
#"p.y.t.h.o.n"