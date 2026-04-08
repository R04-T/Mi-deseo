
import tkinter as tk
from datetime import datetime

# --- CONFIGURACIÓN ---
FECHA_LIMITE = datetime(2026, 4, 30, 23, 59)  # Cambia esto a la fecha real
MI_DESEO = "Que mis papás consigan empleo en Medellín para quedarnos"
# ---------------------

def actualizar_tiempo():
    ahora = datetime.now()
    diferencia = FECHA_LIMITE - ahora
    
    if diferencia.total_seconds() > 0:
        dias = diferencia.days
        horas, residuo = divmod(diferencia.seconds, 3600)
        minutos, segundos = divmod(residuo, 60)
        
        texto = f"{dias}d {horas}h {minutos}m {segundos}s"
        label_contador.config(text=texto)
        label_contador.after(1000, actualizar_tiempo)
    else:
        label_contador.config(text="El tiempo se ha cumplido. ¡Fe y esperanza!")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Mi Meta - Medellín")
ventana.geometry("500x300")
ventana.configure(bg="#1e1e1e") # Color oscuro como VS Code

# Título del deseo
label_deseo = tk.Label(ventana, text=MI_DESEO, font=("Helvetica", 14, "bold"), 
                       fg="white", bg="#1e1e1e", wraplength=400, pady=20)
label_deseo.pack()

# El contador
label_contador = tk.Label(ventana, text="", font=("Helvetica", 30), 
                          fg="#00ff00", bg="#1e1e1e")
label_contador.pack(expand=True)

actualizar_tiempo()
ventana.mainloop()
