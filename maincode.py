import pandas as pd
from pathlib import Path
diretorio_raiz = Path("C:\\Users\\dsv205\\Desktop\\ACDELCO")

for arquivo in diretorio_raiz.rglob('*ids*.csv'):
    
    if arquivo.parent.name == 'chevrolet':
        df = pd.read_csv(arquivo, sep=';', encoding='utf-8')
        df_sem = df[~df['conversao'].str.contains('chevrolet', case=False, na=False)]
        df_sem.to_csv(f"{diretorio_raiz}\\Chevrolet_ACDELCO.csv", sep=';', encoding='utf-8', index=False)

    else:
        try:
                nome_marca = arquivo.parent.name
                df = pd.read_csv(arquivo, sep=';', encoding='utf-8')
                df_processado = df[df['conversao'].str.contains(nome_marca, case=False, na=False)]
                nome_arquivo_saida = f"{nome_marca.title()}_originais_apenas.csv"
                df_processado.to_csv(f"{diretorio_raiz}\\{nome_arquivo_saida}", sep=';', encoding='utf-8', index=False)
        except:
                print(f"Erro ao processar o arquivo: {arquivo.name}")

