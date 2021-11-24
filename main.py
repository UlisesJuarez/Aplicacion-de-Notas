"""
Proyecto python y msql
"""
print("""
Acciones disponibles:
    -registro
    -login
""")
from usuarios import acciones

hazEl=acciones.Acciones()
accion=input("Que quieres hacer: ")

if accion=="registro":
    hazEl.registro()

elif accion=="login":
    hazEl.login()
