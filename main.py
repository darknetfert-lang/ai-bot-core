import os

while True:
    cmd = input(">> ")

    if cmd == "hola":
        print("Hola 👋")

    elif cmd == "run":
        print("Ejecutando tarea...")

    elif cmd.startswith("open "):
        app = cmd.replace("open ", "")
        os.system(app)

    elif cmd == "clear":
        os.system("clear")

    elif cmd == "exit":
        print("Bye 👋")
        break

    else:
        print("Comando no reconocido")
