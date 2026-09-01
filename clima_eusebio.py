import tkinter as tk
from tkinter import font as tkfont
import urllib.request
import json
import threading
import time
from datetime import datetime


class ClimaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clima em Tempo Real - Eusébio/CE")
        self.root.geometry("600x750")
        self.root.configure(bg="#1a1a2e")
        self.root.minsize(580, 720)

        self.rodando = True
        self.dados = None

        self._construir_ui()
        self._buscar_clima()

    def _construir_ui(self):
        FONTE_TITULO = ("Segoe UI", 18, "bold")
        FONTE_LOCAL = ("Segoe UI", 11)
        FONTE_TEMP = ("Segoe UI", 52, "bold")
        FONTE_DESC = ("Segoe UI", 13)
        FONTE_INFO = ("Segoe UI", 11)
        FONTE_INFO_BOLD = ("Segoe UI", 11, "bold")
        FONTE_HORA = ("Segoe UI", 9)

        # header
        self.lbl_titulo = tk.Label(
            root, text="Previsão do Tempo", font=FONTE_TITULO,
            bg="#1a1a2e", fg="#e0e0e0"
        )
        self.lbl_titulo.pack(pady=(18, 0))

        self.lbl_local = tk.Label(
            root, text="Carregando...", font=FONTE_LOCAL,
            bg="#1a1a2e", fg="#888"
        )
        self.lbl_local.pack()

        # card principal
        self.card = tk.Frame(root, bg="#16213e", bd=0, highlightthickness=0)
        self.card.pack(padx=30, pady=15, fill="x")

        self.lbl_icone = tk.Label(self.card, text="", font=("Segoe UI Emoji", 40), bg="#16213e", fg="#fff")
        self.lbl_icone.pack(pady=(15, 0))

        self.lbl_temp = tk.Label(self.card, text="--°C", font=FONTE_TEMP, bg="#16213e", fg="#ffffff")
        self.lbl_temp.pack()

        self.lbl_desc = tk.Label(self.card, text="", font=FONTE_DESC, bg="#16213e", fg="#a0c4ff")
        self.lbl_desc.pack(pady=(0, 15))

        # grid de informações
        self.info_frame = tk.Frame(root, bg="#1a1a2e")
        self.info_frame.pack(padx=30, fill="x")

        self.labels_info = {}
        infos = [
            ("sensacao", "Sensação Térmica", "🌡️"),
            ("umidade", "Umidade", "💧"),
            ("vento", "Vento", "🌬️"),
            ("pressao", "Pressão", "🔽"),
            ("visibilidade", "Visibilidade", "👁️"),
            ("uv", "Índice UV", "☀️"),
            ("nascer", "Nascer do Sol", "🌅"),
            ("por", "Pôr do Sol", "🌇"),
        ]

        for i, (chave, texto, icone) in enumerate(infos):
            row = i // 2
            col = i % 2
            f = tk.Frame(self.info_frame, bg="#16213e", bd=0)
            f.grid(row=row, column=col, padx=6, pady=6, sticky="nsew")
            self.info_frame.columnconfigure(col, weight=1)

            tk.Label(f, text=f"{icone} {texto}", font=FONTE_INFO, bg="#16213e", fg="#888").pack(anchor="w", padx=12, pady=(10, 0))
            lbl = tk.Label(f, text="--", font=FONTE_INFO_BOLD, bg="#16213e", fg="#e0e0e0")
            lbl.pack(anchor="w", padx=12, pady=(2, 10))
            self.labels_info[chave] = lbl

        # rodapé
        self.lbl_atualizacao = tk.Label(
            root, text="", font=FONTE_HORA,
            bg="#1a1a2e", fg="#555"
        )
        self.lbl_atualizacao.pack(side="bottom", pady=8)

        self.lbl_status = tk.Label(
            root, text="● Atualizando...", font=FONTE_HORA,
            bg="#1a1a2e", fg="#4ecca3"
        )
        self.lbl_status.pack(side="bottom")

        self.root.protocol("WM_DELETE_CLOSE", self._fechar)

    def _buscar_clima(self):
        def _worker():
            while self.rodando:
                try:
                    url = "https://wttr.in/Eusebio,CE,Brazil?format=j1"
                    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                    with urllib.request.urlopen(req, timeout=15) as resp:
                        dados = json.loads(resp.read().decode())
                    self.root.after(0, self._atualizar_ui, dados)
                except Exception as e:
                    self.root.after(0, self._mostrar_erro, str(e))
                time.sleep(300)  # atualiza a cada 5 minutos

        t = threading.Thread(target=_worker, daemon=True)
        t.start()

    def _mostrar_erro(self, msg):
        self.lbl_status.config(text=f"● Erro: {msg}", fg="#e74c3c")
        self.lbl_atualizacao.config(text=f"Última tentativa: {datetime.now().strftime('%H:%M:%S')}")

    def _atualizar_ui(self, dados):
        self.dados = dados
        atual = dados["current_condition"][0]
        local = dados["nearest_area"][0]

        cidade = local.get("areaName", [{}])[0].get("value", "Eusébio")
        estado = local.get("region", [{}])[0].get("value", "CE")
        pais = local.get("country", [{}])[0].get("value", "Brasil")

        self.lbl_local.config(text=f"{cidade}, {estado} - {pais}")

        temp_c = atual.get("temp_C", "--")
        desc_pt = atual.get("lang_pt", [{}])
        if desc_pt and isinstance(desc_pt, list):
            desc_texto = desc_pt[0].get("value", "")
        else:
            desc_texto = atual.get("weatherDesc", [{}])[0].get("value", "")

        icone_map = {
            "Sol": "☀️", "Parcialmente nublado": "⛅", "Nublado": "☁️",
            "Chuvoso": "🌧️", "Chuva": "🌧️", "Tempestade": "⛈️",
            "Nevoeiro": "🌫️", "Neve": "❄️", "Granizo": "🌨️",
        }
        icone = "🌤️"
        for chave, ico in icone_map.items():
            if chave.lower() in desc_texto.lower():
                icone = ico
                break

        self.lbl_icone.config(text=icone)
        self.lbl_temp.config(text=f"{temp_c}°C")
        self.lbl_desc.config(text=desc_texto)

        # informações extras
        self.labels_info["sensacao"].config(text=f"{atual.get('FeelsLikeC', '--')}°C")
        self.labels_info["umidade"].config(text=f"{atual.get('humidity', '--')}%")
        self.labels_info["vento"].config(text=f"{atual.get('windspeedKmph', '--')} km/h {atual.get('winddir16Point', '')}")
        self.labels_info["pressao"].config(text=f"{atual.get('pressure', '--')} hPa")
        self.labels_info["visibilidade"].config(text=f"{atual.get('visibility', '--')} km")
        self.labels_info["uv"].config(text=f"{atual.get('uvIndex', '--')}")

        previsao_hoje = dados.get("weather", [{}])[0]
        astro = previsao_hoje.get("astronomy", [{}])[0] if previsao_hoje else {}
        self.labels_info["nascer"].config(text=astro.get("sunrise", "--"))
        self.labels_info["por"].config(text=astro.get("sunset", "--"))

        agora = datetime.now().strftime("%H:%M:%S")
        self.lbl_atualizacao.config(text=f"Atualizado às {agora} · Próxima em 5 min")
        self.lbl_status.config(text="● Ao vivo", fg="#4ecca3")

    def _fechar(self):
        self.rodando = False
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ClimaApp(root)
    root.mainloop()
