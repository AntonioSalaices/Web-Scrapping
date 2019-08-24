from bs4 import BeautifulSoup
import tkinter as tk 
from googlesearch import search
import threading
import time
import urllib


root = tk.Tk()
photo = tk.PhotoImage(file='Filosoft-01.png')
def retrieve_input(textBox):
    time.sleep(2)
    inputValue=textBox.get("1.0","end-1c")
    Buscar(inputValue)

root.title('Buscador de Torrents')
root.geometry("400x400")
tk.Label(root, text="Nombre del torrent:").grid(row=0)
textBox= tk.Text(root, height=1, width=10)
textBox.grid(row=0, column=8)

tk.Button(root, text='Buscar', command= lambda: Hilos() ).grid(row=0, column=12)


def Hilos():
    Res = threading.Thread(target=retrieve_input, args=(textBox,))
    Res.start()


def Buscar(Enter):
    num = 0
    for url in search(Enter + "Torrent gratis", stop=5):
        time.sleep(2)
        content = urllib.request.urlopen(url).read()
        contentHTML = BeautifulSoup(content, "html.parser")
        for link in contentHTML.select('a[href*=".torrent"]'):
            href = BeautifulSoup(str(link), "html.parser")
            downloadLink = href.a['href']
            Descargar(downloadLink)

def Descargar(url):
    url = "https:" + url
    Directorio = "C:/Users/AntonioSalaices/Downloads/Torrents"
    nameRar = "Torrent.torrent"
    urllib.request.urlretrieve(url, filename= Directorio + "/" + nameRar)

root.mainloop()


    
