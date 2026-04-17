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

    elif cmd == "clear":
        os.system("clear")

    elif cmd == "help":
        help_menu()

    elif cmd == "exit":
        print("Bye 👋")
        break

    else:
        print("Comando no reconocido (usa 'help')")
