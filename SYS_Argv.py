import sys
import os

argumento = sys.argv
qtd_argumentos = len(argumento)

if qtd_argumentos <= 1:
    print('Faltando agumentos:')
    print('-a', 'Para listar todos os arquivos nesta pasta', sep='\t')
    print('-d', 'Para listar todos os diretórios nesta paste', sep='\t')
    sys.exit()

so_arquivos = False
if '-a' in argumento:
    so_arquivos = True

so_diretorios = False
if '-d' in argumento:
    so_diretorios = True

for arquivo in os.listdir('.'):
    if so_arquivos:
        if os.path.isfile(arquivo):
            print(arquivo)

    if so_diretorios:
        if os.path.isdir(arquivo):
            print(arquivo)