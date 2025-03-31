from bs4 import BeautifulSoup
import requests
import os
import zipfile

URL_SITE = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

REQ_SITE = requests.get(URL_SITE)

if REQ_SITE.status_code == 200:
    SITE_HTML = BeautifulSoup(REQ_SITE.text, 'html.parser')

    URL_ANEXO_I = SITE_HTML.find('a', string="Anexo I.")['href']
    URL_ANEXO_II = SITE_HTML.find('a', string="Anexo II.")['href']

    REQ_ANEXO_I = requests.get(URL_ANEXO_I)
    REQ_ANEXO_II = requests.get(URL_ANEXO_II)

    if REQ_ANEXO_I.status_code == 200 and REQ_ANEXO_II.status_code == 200:
        PATH_ATUAL = os.path.dirname(os.path.abspath(__file__))
        PATH_ANEXOS = os.path.normpath(os.path.join(PATH_ATUAL, "..", "anexos"))
        NOME_ARQUIVO_I = os.path.basename(URL_ANEXO_I)
        NOME_ARQUIVO_II = os.path.basename(URL_ANEXO_II)
        PATH_ARQUIVO_I = os.path.join(PATH_ANEXOS, NOME_ARQUIVO_I)
        PATH_ARQUIVO_II = os.path.join(PATH_ANEXOS, NOME_ARQUIVO_II)
        PATH_ZIP_FILES = os.path.normpath(os.path.join(PATH_ATUAL, "..", "zip_files"))
        PATH_ZIP = os.path.join(PATH_ZIP_FILES, 'Anexos.zip')

        with open(PATH_ARQUIVO_I, 'wb') as arquivo:
            arquivo.write(REQ_ANEXO_I.content)
        with open(PATH_ARQUIVO_II, 'wb') as arquivo:
            arquivo.write(REQ_ANEXO_II.content)

        with zipfile.ZipFile(PATH_ZIP, 'w', compression=zipfile.ZIP_DEFLATED) as arquivo_zip:
            arquivo_zip.write(PATH_ARQUIVO_I, arcname=NOME_ARQUIVO_I)
            arquivo_zip.write(PATH_ARQUIVO_II, arcname=NOME_ARQUIVO_II)

    elif REQ_ANEXO_I.status_code != 200 and REQ_ANEXO_II.status_code == 200:
        print(f'Erro ao obter resposta do Anexo I\nCódigo: {REQ_ANEXO_I.status_code}')
    elif REQ_ANEXO_I.status_code == 200 and REQ_ANEXO_II.status_code != 200:
        print(f'Erro ao obter resposta do Anexo II\nCódigo: {REQ_ANEXO_II.status_code}')
    else:
        print(f'Erro ao obter resposta do Anexo I e Anexo II\n'
                f'Código I: {REQ_ANEXO_I.status_code}\n'
                f'Código II: {REQ_ANEXO_II.status_code}')
else:
    print(f'Erro ao obter resposta do https://www.gov.br/\nCódigo: {REQ_SITE.status_code}')


