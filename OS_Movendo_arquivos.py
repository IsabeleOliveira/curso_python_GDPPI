import os
import shutil


caminho_original = input('Digite um caminho: ')
caminho_novo = input('Digite o novo caminho: ')


try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta: {caminho_novo} já exite')

for raizes, diretorios, arquivos1 in os.walk(caminho_novo):
    for arquivos in arquivos1:
        caminho_antigo = os.path.join(raizes, arquivos1)
        caminho_new = os.path.join(caminho_novo, arquivos1)


        # Como mover um arquivo de uma pasta pra outra
        """if '.str' in arquivos:
            shutil.move(caminho_antigo, caminho_new)
            print(f'Arquivo {arquivos1} movido com sucesso')
        """

        # Como apagar os arquivos de uma pasta
        """if '.str' in arquivos:
            os.remove(caminho_new)
        """