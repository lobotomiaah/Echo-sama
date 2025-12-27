from core.brain import Brain

brain = Brain()

print("Echo-sama online.")

while True:
    user = input("Você: ")
    if user.lower() in ["exit", "sair"]:
        break

    print("Echo-sama:", brain.respond(user))
