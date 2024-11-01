class Monster():
    def __init__(self,name, origin):
        self.name = name
        self.origin = origin
    
    def attack(self):
        pass

class Familiar(Monster):
    def attack(self):
        return("\nThe bird soars through the air dodging any attacks thrown by his enemy. he suddenly dives and uses his claws to tear away at his enemies flesh.")
    
class Devil(Monster):
    def attack(self):
        return("\nThe blue flame between their horns glows brighter. it starts to engulf their head. they start to jerk their head towards their opponent. the force in undeniable. once their head makes contant the enemy stumbles backwards and is set slightly aflame.")

class Werewolf(Monster):
    def attack(self):
        return("\nhe transforms into a beautiful ginger werewolf, his shirt ripps slightly. you wonder how many times he has ripped his favorite shirt. he gourgous locks flow in the midnight wind. he bares his fangs, his mouth twitches. he stubles towards his opponent, mouth watering. Suddenly the wolfman lunges and bites into the neck of his opponent. they immeditly pass out, blood flows up through onto his teeth.")
    
class Mothman(Monster):
    def attack(self):
        return("\nthe mothman starts to overshare. his eyes fill with stars and he gets more and more passionate; However, to everyone else it is unbarably boring. the mothmans enemy takes bored damage.")


August = Werewolf("August", "Longhope")
Thursday = Familiar("Thursday", "Longhope")
Jamie = Devil("Jamie", "Longhope")
Atlas = Mothman("Atlas", "Longhope")

print(Thursday.attack())
print(Jamie.attack())
print(August.attack())
print(Atlas.attack())