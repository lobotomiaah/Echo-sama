import os
import importlib

pasta = "interacoes"

print("🔄 Iniciando carregamento:")

for arquivo in os.listdir(pasta):
    if arquivo.endswith(".py") and arquivo != "__init__.py":
        importlib.import_module(f"{pasta}.{arquivo[:-3]}")
        print(f"   ✔ {arquivo} carregado")

print("✅ Carregamento finalizado com sucesso!")
