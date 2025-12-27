from core.brain import Brain

brain = Brain()

print("🤖 Echo-sama online. Hmpf…")

while True:
    user = input("Você: ")
    if user.lower() in ["sair", "exit"]:
        break

    resposta = brain.responder(user)
    print("Echo-sama:", resposta)

