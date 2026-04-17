import os

def help_menu():
    print("""
Comandos disponibles:
- hola
- run
- open <app>
- clear
- exit
- help
""")

while True:
    cmd = input(">> ").lower()

    if cmd == "hola":
        print("Hola 👋")

    elif cmd == "run":
        print("Ejecutando tarea...")

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

    elif cmd == "clear":
        os.system("clear")

    elif cmd == "help":
        help_menu()

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
    import datetime
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
