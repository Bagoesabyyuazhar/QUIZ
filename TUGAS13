import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import os

window = tk.Tk()
window.configure(bg="Purple")
window.geometry("450x500")


class Plant:
    frm = ttk.Frame(window, padding="50")
    frm.pack(padx=70, fil="x", expand=True)

    def __init__(self):
        self.status = 0
        self.jumlahAir = 0
        self.jumlahPupuk = 0
        self.statusTumbuh = "Benih"

    @property
    def getJumlahAir(self):
        return self.jumlahAir

    @property
    def getJumlahPupuk(self):
        return self.jumlahPupuk

    @property
    def getStatusTumbuh(self):
        return self.statusTumbuh

    @property
    def setStatusberbunga(self):
        self.statusTumbuh = "Berbunga"

    @property
    def tampil(self):
        return "Status Tanaman : berhasil ".format(self.statusTumbuh, self.jumlahAir, self.jumlahPupuk)

    def beriAir(self):
        self.jumlahAir += 1
        self.cek_kondisi_tumbuh()

    def beriPupuk(self):
        self.jumlahPupuk += 1
        self.cek_kondisi_tumbuh()

    def cek_kondisi_tumbuh(self):
        if self.status < 4:
            if self.jumlahAir >= 3 and self.jumlahPupuk >= 1:
                self.tumbuh()

    def tumbuh(self):
        self.jumlahAir -= 3
        self.jumlahPupuk -= 1
        self.status += 1
        self.statusTumbuh = self.getStatusTumbuhText()

    def getStatusTumbuhText(self):
        if self.status == 0:
            return "Benih"
        elif self.status == 1:
            return "Tunas"
        elif self.status == 2:
            return "Tanaman Kecil"
        elif self.status == 3:
            return "Tanaman Besar"
        return "Berbunga"


class Anggrek(Plant):
    def __init__(self, jenis_bunga):
        super().__init__()
        self.jenis = jenis_bunga

    def getJenis(self):
        return self.jenis


class Mawar(Plant):
    def __init__(self, jenis_bunga):
        super().__init__()
        self.jenis = jenis_bunga

    def getJenis(self):
        return self.jenis


class Melati(Plant):
    def __init__(self, jenis_bunga):
        super().__init__()
        self.jenis = jenis_bunga

    def getJenis(self):
        return self.jenis


anggrek = Anggrek("Anggrek")
mawar = Mawar("Mawar")
melati = Melati("Melati")


def akhir(dataShow, jenis, btn, info):
    if jenis.getStatusTumbuh != "Tanaman Besar" and jenis.getStatusTumbuh != "Berbunga":
        if "1.Beri Air" in btn["text"]:
            if jenis.getJumlahAir < 3:
                jenis.beriAir()
                info["text"] = ""
            else:
                info["text"] = "Info : berhasil!"

        elif "2.Beri Pupuk" in btn["text"]:
            if jenis.getJumlahPupuk < 1:
                jenis.beriPupuk()
                info["text"] = ""
            else:
                info["text"] = "Info : berhasil"
    else:
        info["text"] = f"{jenis.getJenis()} Tanaman Behasil"
        jenis.setStatusberbunga

    dataShow["text"] = f"{jenis.tampil}"


def pilih(jenis, *args):
    for i in args:
        i.destroy()

    frm = Plant.frm

    judul2 = ttk.Label(frm, text=f" Eksekusi Tanaman {jenis.getJenis()} ")
    judul2.pack(padx="10", pady="10", fil="x", expand=True)

    info = ttk.Label(frm, text="")
    info.pack(padx="10", pady="5", fil="x", expand=True)

    dataShow = ttk.Label(frm, text=f"{jenis.tampil}")
    dataShow.pack(padx="10", pady="5", fil="x", expand=True)

    btn_beriAir = ttk.Button(frm, text="1.Beri Air", command=lambda: [
                             akhir(dataShow, jenis, btn_beriAir, info)])
    btn_beriAir.pack(padx=10, pady=5, fil="x", expand=True)

    btn_beriPupuk = ttk.Button(frm, text="2.Beri Pupuk", command=lambda: akhir(
        dataShow, jenis, btn_beriPupuk, info))
    btn_beriPupuk.pack(padx=10, pady=5, fil="x", expand=True)

    btn_exit2 = ttk.Button(frm, text="3.Exit", command=lambda: [main(
        judul2, btn_beriAir, btn_beriPupuk, btn_exit2, info, dataShow)])
    btn_exit2.pack(padx=10, pady=5, fill="x", expand=True)


def main(*args):
    if args:
        for i in args:
            i.destroy()

    frm = Plant.frm

    judul = ttk.Label(frm, text="Pilih Bunga")
    judul.pack(padx="10", pady="10", fil="x", expand=True)

    btn_a = ttk.Button(frm, text="1.Anggrek", command=lambda: [
                       pilih(anggrek, judul, btn_a, btn_m, btn_mel, btn_exit)])
    btn_a.pack(padx=10, pady=5, fil="x", expand=True)

    btn_m = ttk.Button(frm, text="2.Mawar", command=lambda: [
                       pilih(mawar, judul, btn_a, btn_m, btn_mel, btn_exit)])
    btn_m.pack(padx=10, pady=5, fil="x", expand=True)

    btn_mel = ttk.Button(frm, text="3.Melati", command=lambda: [
                         pilih(melati, judul, btn_a, btn_m, btn_mel, btn_exit)])
    btn_mel.pack(padx=10, pady=5, fil="x", expand=True)

    btn_exit = ttk.Button(frm, text="4.Exit", command=window.destroy)
    btn_exit.pack(padx=10, pady=5, fill="x", expand=True)

    window.mainloop()


if __name__ == "__main__":
    main()
