import requests
from tkinter import *



import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)
print(lista_arquivos)

locais =  {
    "imagens": [".png", ".jpg"],
    "planilhas": [".xlsx"],
    "pdfs": [".pdf"],
    "csv": [".csv"],
    "xlsm": [".xlsm"],
    "jpeg": [".jpeg"],
    "zip": [".zip"],
    "mp4": [".mp4"],
    "mp3": [".mp3"],
    "txt": [".txt"]
}

for arquivo in lista_arquivos:
#01 Arquivo.pdf
  nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
  for pasta in locais:
      if extensao in locais[pasta]:
         if not os.path.exists(f"{caminho}/{pasta}"):
             os.mkdir(f"{caminho}/{pasta}")
         os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")



 



