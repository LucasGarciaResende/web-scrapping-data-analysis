import os
import pandas as pd
from http.server import SimpleHTTPRequestHandler, HTTPServer
import json

PATH_ATUAL = os.path.dirname(os.path.abspath(__file__))
PATH_TABELAS = os.path.normpath(os.path.join(PATH_ATUAL, "..", "tabelas"))
PATH_RELATORIO = os.path.join(PATH_TABELAS, "Relatorio_cadop.csv")

dataframe = pd.read_csv(PATH_RELATORIO, sep=";", encoding="utf-8")
colunas = ["DDD", "Telefone", "Fax", "Regiao_de_Comercializacao"]
dataframe[colunas] = dataframe[colunas].astype("Int64")
relatorio_json = dataframe.to_json(orient="records")

class Request(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(relatorio_json.encode("utf-8"))
        
    def do_POST(self):
        tamanho_pesquisa = int(self.headers["Content-Length"])
        try:
            post_pesquisa = json.loads(self.rfile.read(tamanho_pesquisa).decode("utf-8"))
            pesquisa = post_pesquisa.get("busca", "").strip().lower()
            filtered_data = dataframe[
                dataframe.astype(str).apply(lambda linha: linha.str.contains(pesquisa, case=False, na=False).any(), axis=1)
            ]   
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(filtered_data.to_json(orient="records").encode("utf-8"))
        
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        
HOST = "localhost"
PORT = 1250

server = HTTPServer((HOST, PORT), Request)
print(f'Servidor rodando no endereço http://{HOST}:{PORT}')
server.serve_forever()