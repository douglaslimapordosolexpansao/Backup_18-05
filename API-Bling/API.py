import pandas as pd
import os

# Defina o diretório onde os arquivos estão armazenados
diretorio = "C:/Users/DELL/Desktop/VisãoGeral/Venda - 01.02"

# Crie um dataframe vazio para armazenar os dados consolidados
df_consolidado = pd.DataFrame()

# Percorra todos os arquivos na pasta especificada
for nome_arquivo in os.listdir("VisaoGeralVenda"):
    # Verifique se o arquivo é um arquivo Excel
    if nome_arquivo.endswith(".xlsx"):
        # Faça a leitura do arquivo Excel e adicione os dados ao dataframe consolidado
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        df = pd.read_excel(caminho_arquivo)
        df_consolidado = pd.concat([df_consolidado, df])

# Salve o dataframe consolidado em um novo arquivo Excel
caminho_novo_arquivo = "C:/Users/DELL/Desktop/VisãoGeral - 01.02/VisaoGeralVenda.xlsx"
df_consolidado.to_excel(caminho_novo_arquivo, index=False)
