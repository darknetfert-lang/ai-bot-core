import os
import datetime

def help_menu():
    print("""
Comandos disponibles:
- hola
- run
- open <app>
- calc <expresión>
- como estas
- quien eres
- hora
- clear
- exit
- help
""")

# 👇 Saludo automático
hora = datetime.datetime.now().hour

if hora < 12:
    print("Buenos días ☀️")
elif hora < 18:
    print("Buenas tardes 🌇")
else:
    print("Buenas noches 🌙")

# 👇 Loop principal
while True:
    cmd = input(">> ").lower()

    if cmd == "hola":
        print("Hola 👋")

    elif cmd == "run":
        print("Ejecutando tarea...")

    elif "google" in cmd:
       os.system("termux-open-url https://google.com")

    elif cmd.startswith("open "):
        app = cmd.replace("open ", "")
        print(f"Abriendo {app}...")
        os.system(app)

    elif cmd.startswith("calc "):
        try:
            result = eval(cmd.replace("calc ", ""))
            print("Resultado:", result)
        except:
            print("Error en cálculo")

    elif "como estas" in cmd or "cómo estás" in cmd:
        print("Todo bien 😎 ¿y tú?")

    elif "quien eres" in cmd:
        print("Soy tu bot 🔥")

    elif "hora" in cmd:
        print(datetime.datetime.now().strftime("%H:%M:%S"))

    elif cmd == "clear":
        os.system("clear")

    elif cmd == "help":
        help_menu()

    elif cmd == "exit":
        print("Bye 👋")
        break

    else:
        print("Comando no reconocido (usa 'help')")
​# Test para mi logro YOLO
