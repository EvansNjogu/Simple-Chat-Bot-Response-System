import random

rEating = "I don't like eating anything because I'm a bot obviously!"
rRobot = "Yes I am a robot, but I'm a good one. Let me prove it. How can I help you?"
rSomething = "I have nothing to tell you, except that I was created by Evans!"
rJoke = "I only know 1 joke, I only know 25 letters of the alphabet, I don't know y. Haha!"

def unknown():
    reponse = ["Could you please re-phrase that?",
                "...",
                "Sounds about right",
                "What does that mean?",
                "I am not sure I understood you, tried Googling?"][random.randrange(5)]
    return reponse