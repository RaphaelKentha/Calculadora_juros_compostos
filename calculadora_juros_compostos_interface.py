import tkinter as tk
from tkinter import messagebox

def calcular_valor_futuro():
    try:
        patrimonio = float(patrimonio_entry.get())
        aporte_mes = float(aporte_mes_entry.get())
        rentabilidade = (((float(rentabilidade_entry.get()) / 100) +1)**(1/12) - 1)
        tempo = int(tempo_entry.get()) * 12

        Fv = (aporte_mes * (((1 + rentabilidade) ** tempo - 1)) / rentabilidade) + patrimonio * (1 + rentabilidade) ** tempo
        messagebox.showinfo("Resultado", f"O valor futuro após {tempo} meses será de R${Fv:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

root = tk.Tk()
root.title("Calculadora de Juros Compostos")

tk.Label(root, text="Patrimônio inicial: R$").grid(row=0)
tk.Label(root, text="Aporte mensal: R$").grid(row=1)
tk.Label(root, text="Taxa de rentabilidade anual (%):").grid(row=2)
tk.Label(root, text="Tempo de investimento (anos):").grid(row=3)

patrimonio_entry = tk.Entry(root)
aporte_mes_entry = tk.Entry(root)
rentabilidade_entry = tk.Entry(root)
tempo_entry = tk.Entry(root)

patrimonio_entry.grid(row=0, column=1)
aporte_mes_entry.grid(row=1, column=1)
rentabilidade_entry.grid(row=2, column=1)
tempo_entry.grid(row=3, column=1)

tk.Button(root, text="Calcular", command=calcular_valor_futuro).grid(row=4, column=1, pady=10)

root.mainloop()
