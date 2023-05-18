import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados do arquivo CSV
df = pd.read_csv('C:\Users\DELL\Desktop\teste_fat.csv', parse_dates=['data'])

# Filtrando os dados por status 'Enviado'
df = df[df['status'] == 'Enviado']

# Agrupando os dados por mês e calculando o faturamento total
df_mes = df.groupby(pd.Grouper(key='data', freq='M')).sum()

# Separando os valores por ano
ano_passado = df_mes['2021']['faturamento']
este_ano = df_mes['2022']['faturamento']

# Configuração do gráfico
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
plt.figure(figsize=(10, 6))
plt.bar(meses, ano_passado, color='blue', alpha=0.5, label='Ano Passado')
plt.bar(meses, este_ano, color='red', alpha=0.5, label='Este Ano')
plt.xlabel('Mês')
plt.ylabel('Faturamento')
plt.title('Comparativo de Faturamento Mensal')
plt.legend()

# Exibição do gráfico
plt.show()
