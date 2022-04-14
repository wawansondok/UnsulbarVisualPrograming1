from functools import partial
import tkinter as tk

   

class applikasiKalkulator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Kalkulator Wawan sondok_D0219414") 
        self.geometry('400x200')
        self.membuatTombol()
        self.penentu = False

    def membuatTombol(self):
        self.layar = tk.Entry(self, width=25)
        self.layar.grid(row=0, column=0, columnspan=5)

        btn_list = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '0', '+', '-',
            'Hapus', '/', '*',
            '='
        ]
        baris = 3
        kolom = 0
        for penampung in btn_list:
            perintah = partial(self.hitung, penampung)
            if penampung == '=':
                tk.Button(self, text='=', width=22, command=perintah).grid(row=baris, column=kolom, columnspan=5)
            else :
                tk.Button(self, text=penampung, width=5, command=perintah).grid(row=baris, column=kolom)
            kolom += 1
            if kolom > 2:
                kolom = 0
                baris += 1

    def hitung(self, key):
        if key == '=':
            self.penentu = True
            try:
                result = eval(self.layar.get())
                self.layar.delete(0, tk.END)
                self.layar.insert(tk.END, str(result))
            except:
                self.layar.insert(tk.END, "-> Error!")
        elif key == 'Hapus':
            self.layar.delete(0, tk.END)
        else:
            if self.penentu :
                self.layar.delete(0, tk.END)
                self.penentu = False
            self.layar.insert(tk.END, key)

wawan = applikasiKalkulator()
wawan.mainloop()