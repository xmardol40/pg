import tkinter as tk
from tkinter import messagebox
from horoskop_scraper import ziskej_popis_znameni


# Základní Frame s metodou show()
class BaseFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

    def show(self):
        self.tkraise()


# Hlavní aplikace
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Znamení zvěrokruhu")
        self.geometry("600x550")
        self.vybrane_znameni = ""  # klíč bez diakritiky

        self.frames = {}
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        for F in (FrameOne, FrameTwo, FrameThree):
            name = F.__name__
            frame = F(container, self)
            self.frames[name] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame("FrameOne")

    def show_frame(self, name):
        frame = self.frames[name]
        if name == "FrameThree":
            frame.aktualizuj_text()
        frame.show()


# Frame 1 – Úvodní obrazovka
class FrameOne(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        label = tk.Label(self, text="Vítejte! Chcete znát svůj horoskop na dnešní den?.", font=("Helvetica", 14))
        label.pack(pady=40)

        btn_dalsi = tk.Button(self, text="Ano, pokračuj", width=15,
                              command=lambda: controller.show_frame("FrameTwo"))
        btn_dalsi.pack(pady=5)

        btn_konec = tk.Button(self, text="Ne", width=15, command=self.potvrdit_konec)
        btn_konec.pack(pady=5)

    def potvrdit_konec(self):
        if messagebox.askyesno("Ukončit", "Opravdu chcete aplikaci ukončit?"):
            self.controller.destroy()


# Frame 2 – Výběr znamení
class FrameTwo(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.seznam_znameni_s_diakr = [
            "Beran", "Býk", "Blíženci", "Rak", "Lev", "Panna",
            "Váhy", "Štír", "Střelec", "Kozoroh", "Vodnář", "Ryby"
        ]

        self.seznam_znameni = [
            "beran", "byk", "blizenci", "rak", "lev", "panna",
            "vahy", "stir", "strelec", "kozoroh", "vodnar", "ryby"
        ]

        # Slovník s popisy
        self.popisy = ziskej_popis_znameni()
      
        controller.popisy = self.popisy  # zpřístupnění pro FrameThree

        label = tk.Label(self, text="Zvolte znamení:", font=("Helvetica", 12))
        label.pack(pady=10)

        # Rámeček pro tlačítka
        btn_frame = tk.Frame(self)
        btn_frame.pack()

        # Vytvoření 12 tlačítek
        for i, (nazev, klic) in enumerate(zip(self.seznam_znameni_s_diakr, self.seznam_znameni)):
            btn = tk.Button(
                btn_frame, text=nazev, width=12,
                command=lambda k=klic: self.prejdi_na_vysledek(k)
            )
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)

         # Tlačítko "Konec" pro ukončení aplikace
        btn_konec = tk.Button(self, text="Konec", width=15, command=self.potvrdit_konec)
        btn_konec.pack(pady=20)

    def potvrdit_konec(self):
        if messagebox.askyesno("Ukončit", "Opravdu chcete aplikaci ukončit?"):
            self.controller.destroy()

    def prejdi_na_vysledek(self, klic):
        self.controller.vybrane_znameni = klic
        self.controller.show_frame("FrameThree")


# Frame 3 – Výsledek
class FrameThree(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.nazvy_znameni = {
            "beran": "Beran", "byk": "Býk", "blizenci": "Blíženci", "rak": "Rak",
            "lev": "Lev", "panna": "Panna", "vahy": "Váhy", "stir": "Štír",
            "strelec": "Střelec", "kozoroh": "Kozoroh", "vodnar": "Vodnář", "ryby": "Ryby"
        }

        self.nadpis_label = tk.Label(self, text="", font=("Helvetica", 16, "bold"))
        self.nadpis_label.pack(pady=(30, 10))

        self.popis_label = tk.Label(self, text="", wraplength=300, justify="center")
        self.popis_label.pack(pady=(0, 20))

        btn_zpet = tk.Button(self, text="Zpět", command=lambda: controller.show_frame("FrameTwo"))
        btn_zpet.pack()

    def aktualizuj_text(self):
        klic = self.controller.vybrane_znameni
        popis = self.controller.popisy.get(klic, "Popis nebyl nalezen.")
        nadpis = self.nazvy_znameni.get(klic, klic.capitalize())

        self.nadpis_label.config(text=nadpis)
        self.popis_label.config(text=popis)


# Spuštění aplikace
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()




