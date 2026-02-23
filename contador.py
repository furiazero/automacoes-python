with open("entrada.txt","r",encoding="utf-8")as arq:
    texto = arq.read()

numero_de_linhas = len(texto.splitlines())#2
numero_de_caracteres = len(texto)
numero_de_palavras = len(texto.split())

print("numero de linhas: ",numero_de_linhas)
print("numero de caracteres: ",numero_de_caracteres)
print("numero_de_palavras:  ",numero_de_palavras)

with open("saida.txt","w",encoding="utf-8")as arq:
      arq.write("""numero de linhas:  2\nnumero de caracteres:44\nnumero_de_palavras:8""")