import random


animals = ["🐶 Dog meme!", "🐱 Cat meme!", "🐸 Frog meme!"]
games = ["🎮 Game meme!", "🕹️ Play meme!", "👾 Gamer meme!"]

rare = ["🌟 Rare meme!", "💎 Super rare meme!"]

def get_meme(topic):
    if random.randint(1, 5) == 1:
        return random.choice(rare)
    if topic == "animals":
        return random.choice(animals)
    if topic == "games":
        return random.choice(games)
    return "Sorry, I don’t know that topic."

print(get_meme("animals"))
print(get_meme("games"))
print(get_meme("space"))
