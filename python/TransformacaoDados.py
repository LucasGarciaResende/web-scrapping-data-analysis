import pdfplumber
import pandas as pd
import os
import zipfile

NOME_ARQUIVO = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
PATH_ATUAL = os.path.dirname(os.path.abspath(__file__))
PATH_ANEXOS = os.path.normpath(os.path.join(PATH_ATUAL, "..", "anexos"))
PATH_ARQUIVO = os.path.join(PATH_ANEXOS, NOME_ARQUIVO)

tabelas = []
with pdfplumber.open(PATH_ARQUIVO) as arquivo:
    for counter, pagina in enumerate(arquivo.pages, 1):
        tabela = pagina.extract_table()
        if tabela:
            dataframe = pd.DataFrame(tabela[1:], columns=tabela[0])
            tabelas.append(dataframe)
            print(f'Tabela da página {counter} adicionada.')
        else:
            print(f'Não foi encontrada uma tabela na página {counter}!')

dataframe_completo = pd.concat(tabelas, ignore_index=True)

SUBSTITUIR = {
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulatorial"
}

dataframe_completo = dataframe_completo.replace(SUBSTITUIR)

PATH_TABELAS = os.path.normpath(os.path.join(PATH_ATUAL, "..", "tabelas"))
NOME_CSV = "Tabelas_Anexo_I.csv"
PATH_CSV = os.path.join(PATH_TABELAS, NOME_CSV)
PATH_ZIP_FILES = os.path.normpath(os.path.join(PATH_ATUAL, "..", "zip_files"))
PATH_ZIP = os.path.join(PATH_ZIP_FILES, "Teste_Lucas_Garcia_Resende.zip")

dataframe_completo.to_csv(PATH_CSV, index=False)

with zipfile.ZipFile(PATH_ZIP, 'w', compression=zipfile.ZIP_DEFLATED) as arquivo_zip:
    arquivo_zip.write(PATH_CSV, arcname=NOME_CSV)