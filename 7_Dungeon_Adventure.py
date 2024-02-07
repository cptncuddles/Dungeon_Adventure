#We are creating a text based adventure game in the style of Final Fantasy
import random

#Here are the classes and methods needed for the game. Can obviously expanded as knowledge of OOP grows.

class Player_Character:
    def __init__(self, name, hp, ac, const):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.const = const

    def __repr__(self):
        return "{character_name} is a wandering adventurer. After years of service to the merchant guilds of The Clovis Concord, you became bored by the simple life afforded to yourself. \n You have recently decided to strike out on an adventure of your own, equipped with your wits and a simple adventurer's pack you set off from Niccodrana towards Zadash. You have run into many insteresting characters along your route, feeling confident and excited about the possibilities you decided to venture off the main road outside of Trostenwald to check out some ruins a fellow adventurer mentioned.".format(character_name = pc.name)
    
    def id(self):
        print(str(self.name))

    def attack(self):
        ap = random.randint(1, 20)
        if ap >= g1.ac:
            print("Succeeds")
            dmg = random.randint(1,6)
            g1.hp = g1.hp - dmg
        else:
            return "Fails"
    
    def sneak_attack(self):
        ap = random.randint(1, 20) + 5
        if ap >= g1.ac:
            print("Succeeds")
            dmg = (random.randint(1,6))*2
            g1.hp = g1.hp - dmg
        else:
            return "Fails"
    
    def pick_pocket(self):
        pp = random.randint(1,10)
        if pp >= 3:
            return "Succeeds"
        else:
            return "Fails"
    
    def fireball(self):
        fb = random.randint(1,20)
        if fb >= g1.ac:
            print("Succeeds")
            dmg = random.randint(1,6) + 2
            g1.hp = g1.hp - dmg
        else:
            return "Fails"
        
class Mob:
    def __init__(self, name, hp, ac, const):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.const = const
    
    def __repr__(self):
        return self.name
    
    def attack(self):
        ap = random.randint(1, 20)
        if ap >= pc.ac:
            print("Succeeds")
            dmg = random.randint(1,6)
            pc.hp = pc.hp - dmg
        else:
            return "Fails"
    
    def slash(self):
        ap = random.randint(1, 20)
        if ap >= pc.ac:
            print("Succeeds")
            dmg = random.randint(1,6) + 2
            pc.hp = pc.hp - dmg
        else:
            return "Fails"
        
#Here are the functions used for combat
def advance():
    input("Press [Enter]")

def health_left():
    print("Your attack leaves the guard with {hp} health.".format(hp = g1.hp))

def combat():
    while g1.hp >= 1:
        a4 = input("What move would you like to use? ")
        if a4 == str("Attack"):
            pc.attack()
            health_left()
            advance()
            if random.randint(1, 20) % 2 == 0:
                g1.attack()
                hp_left()
                if pc.hp == 0:
                    ded()
            else:
                g1.slash()
                hp_left()
                if pc.hp == 0:
                    ded()
        elif a4 == str("Sneak Attack"):
            pc.sneak_attack()
            health_left()
            advance()
            if random.randint(1, 20) % 2 == 0:
                g1.attack()
                hp_left()
                if pc.hp == 0:
                    ded()
            else:
                g1.slash()
                hp_left()
                if pc.hp == 0:
                    ded()
        elif a4 == str("Fireball"):
            pc.fireball()
            health_left()
            advance()
            if random.randint(1, 20) % 2 == 0:
                g1.attack()
                hp_left()
                if pc.hp == 0:
                    ded()
            else:
                g1.slash()
                hp_left()
                if pc.hp == 0:
                    ded()
    else:
        print("You have defeated your enemy!")
        advance()

def prebattle():
    print("Here is your possible attacks:")
    print("Attack")
    print("Sneak Attack")
    print("Fireball")
    advance()

def ded():
    if pc.hp <= 0:
        print("You have died.")
        print("GAME OVER")

def hp_left():
    print("That attack left you with {hp} health.".format(hp=pc.hp))

def ending1():
    print("As you bask in your victory, you realize you will most likely need a disguise to make your escape a bit more manageable. As you begin to remove the dead guard's clothes you notice some strange marking on his torso, his arms, and his legs. He seems to have been cut very intently and sewn back together. \n You make note of this as you give your clothes to Tolen, and dawn the guard’s attire. Feeling more prepared than you have yet, you open the door to a blinding light. You realize you aren’t underground. You take stock of your surroundings and realize you are in a major city. \n There are crowds of people everywhere, the smell of food drifting in and around you, and the feel of a crisp cool breeze blowing across your face. You feel like you have been here before. As you try to get your bearings, Tolen firmly grabs your arm and whispers, ‘We are not safe yet, please follow me. I have a safe place nearby with people we can trust.’ \n You realize that this isn’t going to be like one of your normal adventures.")

def ending2():
    print("As you bask in your victory, you realize you will most likely need a disguise to make your escape a bit more manageable. As you begin to remove the dead guard's clothes you notice some strange marking on his torso, his arms, and his legs. He seems to have been cut very intently and sewn back together. \n You make note of this as you dawn the guard’s attire. Feeling more prepared than you have yet, you open the door to a blinding light. You realize you aren’t underground. You take stock of your surroundings and realize you are in a major city. \n There are crowds of people everywhere, the smell of food drifting in and around you, and the feel of a crisp cool breeze blows across your face. You feel like you have been here before. As you try to get your bearings, a strange woman crosses the packed street and approaches you. ‘If you are who I think you are, you need to follow me quickly. We have much to discuss.’ As you follow her into the din of the crowd you realize that this isn’t going to be like one of your normal adventures.")

def ending3():
    print("Feeling more prepared than you have at any point, you open the door to a blinding light. You realize you aren’t underground. You take stock of your surroundings and realize you are in a major city. \n There are crowds of people everywhere, the smell of food drifting in and around you, and the feel of a crisp cool breeze blows across your face. You feel like you have been here before. \n As you try to get your bearings, a strange woman crosses the packed street and approaches you. ‘If you are who I think you are, you need to follow me quickly. We have much to discuss.’ As you follow her into the din of the crowd you realize that this isn’t going to be like one of your normal adventures.")

pc = Player_Character("", 25, 13, 11)


g1 = Mob("Derek", 15, 4, 8)

print("Welcome Adventurer! Before we begin, you need to name your character.")
advance()
pc.name = input("What will you name your character? ")
advance()
print("Excellent choice! Let our adventure commence!")
advance()
print("Here is a little background on your character:")
print(pc)
advance()


print("You awaken groggy and confused in a dimly lit cell with 2 other prisoners.\n The last thing you remember is exploring a random derelict house looking for some treasure. You heard a quick rustling and felt a heavy blow across the back of your head.\n As you gather your wits and begin to look around you notice a solitary guard positioned at the entrance to the cell. The other two prisoners look like they have been here a lot longer than you. As you begin to stand to speak with them a loud bang and creaking catches your attention.\n Two more guards and what looks like a captain appear outside the cell. The captain looks into the cell at the three of you and points to the person closest to you saying 'That one will be the next sacrifice. We will come back for the other two in a bit.'\n The two new guards rush the cell and grab the man next to you who is kicking a screaming. His screams echo around the cell as he is dragged off crying for help. You don’t have much time. You need to get out of here, fast.")
advance()
print("You think you can pick the guard's pocket for the key, but it might be better to speak with your cellmate first to figure out what is going on.")
advance()

a2 = input("What do you do? [Pick Guards Pocket] or [Speak with Cellmate]? ")

if a2 == str("Pick Guards Pocket"):
    pc.pick_pocket()
    if pc.pick_pocket() == str("Succeeds"):
            print("You deftly swipe the key to the cell off of the guard and silently motion to your fellow prisoner that it's time to leave. You take a small rock and while the guard isn't looking throw it down the hallway to distract him.\n As he gets up to leave you silently move the key into the lock and turn allowing yourself and your fellow prisoner to escape quickly and hide behind the heavy door.")
            advance()
            print("You wait for the guard to walk past you and see the open cell door. As he goes to investigate, he walks right past you. You realize this is the perfect opportunity to strike, or you could shove him in and lock the door and hope for the best.")
            advance()
            a3 = input("What do you do? [Suprise Attack] or [Shove Them and Lock the Door]? ")
#This is the Shove them branch            
            if a3 == str("Shove Them and Lock the Door"):
                print("You quickly and quietly move towards the guard. Hoping he is too confused to notice you. You throw all your weight behind your next move and you shove him deep into the cell and slam the door shut.")
                advance()
                print("He exclaims as the door closes, but by the time the words begin to escape his lips you have already turned and faced your companion. \n You try to get a good look at them, but the light is so dim you can only make out a shocked and defeated look under all of the grim and dried blood.")
                advance()
                print("You open your lips to speak, but are surprised with they speak. Their voice is frail and wavering, but you clearly hear 'Thank you. I am Tolen. I have been here much longer than I can remember. I know I am weak, but I will do all that I can to help you if you do not leave me behind.'")
                advance()
                print("Curious the old man seemed to read your mind....")
                a4 = input("Should you [Bring Him With You] or [Leave Him Behind]? ")
                if a4 == str("Bring Him With You"):
                    print("Something inside you tells you that you can't leave Tolen behind. You decide to trust your gut on this and walk over asking, 'Can you stand and walk? Or do I need to carry you?'")
                    advance()
                    print("Tolen replies 'I may seem weak and frail, but I have stregnth yet for this adventrue before us. Do not worry about me, I will not be a burden to us.' You shake his hand and decide that it's time to leave before the guard awakes and begins to call for help.")
                    advance()
                    print("You turn. Your eyes adjusting to the dim light. As you begin to traverse the corridor you find more cells filled with dead or dying prisoners of all kinds: Orcs, Elves, Tabaxi, Halflings, Goblins...It seems that your captors care not what you are, where you are from, or what state you are in, merely that you exist...")
                    advance()
                    print("The corridor begins to turn upwards, a clear indication you are underground. As you begin to venture upwards you hear voices. With every few steps they become louder and clearer. You must be getting closer to the exit.")
                    advance()
                    print("The path begins to level out and you start to see the end of the corridor. But as you draw closer you realize there is a guard blocking a door at the end of the hall. You turn to Tolen and ask if they are ready for a fight. ‘I shall do my best to assist you however I can.’")
                    advance()
                    print("That doesn’t entirely imbue you with confidence, but it is better than nothing. You approach the guard who stands defiantly in front of the door.")
                    a5 = input("Should you try to [Talk First], or just get this [Fight] started? ")
                    if a5 == str("Talk First"):
                        print("You call out to the guard upon approach, ‘Good evening! My friend and I seem to be a little lost. We sort of stumbled our way into this cozy dungeon….’ You don’t get a chance to finish your sentence as the guard strikes out hitting you square across the face. Guess it’s time to fight.")
                        pc.hp = pc.hp - 2
                        advance()
                        hp_left()
#Here is the only round of combat for this branch of the encounter.
                        prebattle()
                        combat()
                        ending1()
                    else:
                        print("The guard calls out to you as you approach, but you make no inclination to stop or talk. Your intention is unclear to him, until you strike him firmly in the jaw.")
                        g1.hp = g1.hp - 2
                        advance()
                        combat()
                        ending1()
#Leave him behind loop
                else:
                    print("You know that you can’t make it out and take care of someone at the same time. You look at Tolen and just shake your head before decisively closing the door. \n Locking him in with the guard. Tolen gives you a look of surprise and disgust. ‘Nothing personal old man, I just can’t get us both out.’")
                    advance()
                    print("You decide that it's time to leave before the guard awakes and begins to call for help.")
                    advance()
                    print("You turn, your eyes adjusting to the dim light. As you begin to traverse the corridor you find more cells filled with dead or dying prisoners of all kinds: Orcs, Elves, Tabaxi, Halflings, Goblins...It seems that your captors care not what you are, where you are from, or what state you are in, merely that you exist...")
                    advance()
                    print("The corridor seems to wind endlessly to the left and right, but it seems to be turning upwards. a clear indication you are underground. As you begin to venture upwards you hear voices. With every few steps they become louder and clearer. You must be getting closer to the exit.")
                    advance()
                    print("The path begins to level out and you start to see the end of the corridor. But as you draw closer you realize there is a guard blocking a door at the end of the hall. You take measure of him from the shadows. You notice he seems to be favoring his right side even while standing still. You can’t make much more out before you get to a point where you need to act.")
                    advance()
                    print("With a deep breath to remain calm you gather your nerve and rush swiftly towards the guard. Ready to strike!")
                    prebattle()
                    combat()
                    ending2()
#This is the Surprise Attack Branch
            else:
                print("You quickly and quietly move towards the guard. Hoping he is too confused to notice you. You draw back and as you have done so many times before you strike!")
                advance()
                prebattle()
                combat()
                print("As you bask in your victory, you realize you will most likely need a disguise to make your escape a bit more manageable. As you begin to remove the dead guard's clothes you notice some strange marking on his torso, his arms, and his legs. He seems to have been cut very intently and sewn back together. You make note of this as you dawn the guard’s attire.")
                advance()
                print("You turn, your eyes adjusting to the dim light. As you begin to traverse the corridor you find more cells filled with dead or dying prisoners of all kinds: Orcs, Elves, Tabaxi, Halflings, Goblins...It seems that your captors care not what you are, where you are from, or what state you are in, merely that you exist…")
                advance()
                print("The corridor seems to wind endlessly to the left and right, but it seems to be turning upwards. a clear indication you are underground. As you begin to venture upwards you hear voices. With every few steps they become louder and clearer. You must be getting closer to the exit.")
                advance()
                print("The path begins to level out and you start to see the end of the corridor. But as you draw closer you realize there is a guard blocking a door at the end of the hall.")
                advance()
                print("Filled with a bold spirit you stride up to the door and growl at him to get out of your way. To which he gladly obliges….strange….")
                ending3()
#This is the Talk to Prisoner Branch, it will reroute to the Pickpocket branch after giving you background Lore.    
    else:
        print("Perhaps you should talk to your fellow prisoner.")

else:
    print("Deciding that discretion will be the best course of action, you cross the cell to speak with your cellmate. As you draw near they recoil in fear. An instinctual action you gather as they settle as they realize you are not there to hurt them.")
    advance()
    print("You crouch down to get closer to eye level, you see the dried blood caked on their body. Their ragged clothes matted to the husk of a body they have left. Clearly they have been here a long time and have most definitely seen better days.")
    advance()
    print("Hi there friend, my name is {name}, what is yours?".format(name = pc.id))
    advance()
    print("My name is Tolen, I am….was a respected apothecary in service of the Dwindalian Empire.")
    advance()
    print("Tolen, what do you know about what is going on here?")
    advance()
    print("You do not know? This is The Abyss. Everyone you see here has been brought here for one purpose only. To serve as a sacrifice to…Them….")
    print("He trembles in fear, it’s obvious now is not the time to continue down that path of questioning.")
    advance()
    print("Tell me Tolen, how do we get out of here quickly?")
    advance()
    print("There is only one way out. The Abyss was made in such a way that only those who are devoted to……Them…..can leave.")
    advance()
    print("Okay, how much resistance can we expect when we escape?")
    advance()
    print("I do not know. I have lost count of how many days, weeks, months I have been here. I have been beaten and tortured countless times by many guards. I do not know what awaits anyone who can manage to escape their cell.")
    advance()
    print("Well that was sort of helpful…..I guess it’s time to find an actual way out of the cell. Perhaps the guard wouldn’t miss that key he has attached loosely to his belt…")

    a6 = input("It's time to get out of here, are you ready to get that key? Y/N ")
    if a6 == str("Y") or a6 == str("N"):
        print("You are getting that key whether you are ready or not.")
        pc.pick_pocket()
        if pc.pick_pocket() == str("Fails") or pc.pick_pocket() == str("Succeeds"):
            pc.pick_pocket() == str("Succeeds")
            if pc.pick_pocket() == str("Succeeds"):
                print("You deftly swipe the key to the cell off of the guard and silently motion to your fellow prisoner that it's time to leave. You take a small rock and while the guard isn't looking throw it down the hallway to distract him.\n As he gets up to leave you silently move the key into the lock and turn allowing yourself and your fellow prisoner to escape quickly and hide behind the heavy door.")
                advance()
                print("You wait for the guard to walk past you and see the open cell door. As he goes to investigate, he walks right past you. You realize this is the perfect opportunity to strike, or you could shove him in and lock the door and hope for the best.")
                advance()
                a3 = input("What do you do? [Suprise Attack] or [Shove Them and Lock the Door]? ")
#This is the Shove them branch            
                if a3 == str("Shove Them and Lock the Door"):
                    print("You quickly and quietly move towards the guard. Hoping he is too confused to notice you. You throw all your weight behind your next move and you shove him deep into the cell and slam the door shut.")
                    advance()
                    print("He exclaims as the door closes, but by the time the words begin to escape his lips you have already turned and faced your companion. \n You try to get a good look at them, but the light is so dim you can only make out a shocked and defeated look under all of the grim and dried blood.")
                    advance()
                    print("You open your lips to speak, but are surprised with they speak. Their voice is frail and wavering, but you clearly hear 'Thank you. I am Tolen. I have been here much longer than I can remember. I know I am weak, but I will do all that I can to help you if you do not leave me behind.\'")
                    advance()
                    print("Curious the old man seemed to read your mind....")
                    a4 = input("Should you [Bring Him With You] or [Leave Him Behind]? ")
                    if a4 == str("Bring Him With You"):
                        print("Something inside you tells you that you can't leave Tolen behind. You decide to trust your gut on this and walk over asking, 'Can you stand and walk? Or do I need to carry you?'")
                        advance()
                        print("Tolen replies 'I may seem weak and frail, but I have stregnth yet for this adventrue before us. Do not worry about me, I will not be a burden to us.' You shake his hand and decide that it's time to leave before the guard awakes and begins to call for help.")
                        advance()
                        print("You turn. Your eyes adjusting to the dim light. As you begin to traverse the corridor you find more cells filled with dead or dying prisoners of all kinds: Orcs, Elves, Tabaxi, Halflings, Goblins...It seems that your captors care not what you are, where you are from, or what state you are in, merely that you exist...")
                        advance()
                        print("The corridor begins to turn upwards, a clear indication you are underground. As you begin to venture upwards you hear voices. With every few steps they become louder and clearer. You must be getting closer to the exit.")
                        advance()
                        print("The path begins to level out and you start to see the end of the corridor. But as you draw closer you realize there is a guard blocking a door at the end of the hall. You turn to Tolen and ask if they are ready for a fight. ‘I shall do my best to assist you however I can.’")
                        advance()
                        print("That doesn’t entirely imbue you with confidence, but it is better than nothing. You approach the guard who stands defiantly in front of the door.")
                        a5 = input("Should you try to [Talk First], or just get this [Fight] started? ")
                        if a5 == str("Talk First"):
                            print("You call out to the guard upon approach, ‘Good evening! My friend and I seem to be a little lost. We sort of stumbled our way into this cozy dungeon….’ You don’t get a chance to finish your sentence as the guard strikes out hitting you square across the face. Guess it’s time to fight.")
                            pc.hp = pc.hp - 2
                            advance()
                            hp_left()
#Here is the only round of combat for this branch of the encounter.
                            prebattle()
                            combat()
                            ending1()
                        else:
                            print("The guard calls out to you as you approach, but you make no inclination to stop or talk. Your intention is unclear to him, until you strike him firmly in the jaw.")
                            g1.hp = g1.hp - 2
                            advance()
                            combat()
                            ending1()
#Leave him behind loop
                    else:
                        print("You know that you can’t make it out and take care of someone at the same time. You look at Tolen and just shake your head before decisively closing the door. \n Locking him in with the guard. Tolen gives you a look of surprise and disgust. ‘Nothing personal old man, I just can’t get us both out.’")
                        advance()
                        print("You decide that it's time to leave before the guard awakes and begins to call for help.")
                        advance()
                        print("You turn, your eyes adjusting to the dim light. As you begin to traverse the corridor you find more cells filled with dead or dying prisoners of all kinds: Orcs, Elves, Tabaxi, Halflings, Goblins...It seems that your captors care not what you are, where you are from, or what state you are in, merely that you exist...")
                        advance()
                        print("The corridor seems to wind endlessly to the left and right, but it seems to be turning upwards. a clear indication you are underground. As you begin to venture upwards you hear voices. With every few steps they become louder and clearer. You must be getting closer to the exit.")
                        advance()
                        print("The path begins to level out and you start to see the end of the corridor. But as you draw closer you realize there is a guard blocking a door at the end of the hall. You take measure of him from the shadows. You notice he seems to be favoring his right side even while standing still. You can’t make much more out before you get to a point where you need to act.")
                        advance()
                        print("With a deep breath to remain calm you gather your nerve and rush swiftly towards the guard. Ready to strike!")
                        prebattle()
                        combat()
                        ending2()
#This is the Surprise Attack Branch
                else:
                    print("You quickly and quietly move towards the guard. Hoping he is too confused to notice you. You draw back and as you have done so many times before you strike!")
                    advance()
                    prebattle()
                    combat()
                    print("As you bask in your victory, you realize you will most likely need a disguise to make your escape a bit more manageable. As you begin to remove the dead guard's clothes you notice some strange marking on his torso, his arms, and his legs. He seems to have been cut very intently and sewn back together. You make note of this as you dawn the guard’s attire.")
                    advance()
                    print("You turn, your eyes adjusting to the dim light. As you begin to traverse the corridor you find more cells filled with dead or dying prisoners of all kinds: Orcs, Elves, Tabaxi, Halflings, Goblins...It seems that your captors care not what you are, where you are from, or what state you are in, merely that you exist…")
                    advance()
                    print("The corridor seems to wind endlessly to the left and right, but it seems to be turning upwards. a clear indication you are underground. As you begin to venture upwards you hear voices. With every few steps they become louder and clearer. You must be getting closer to the exit.")
                    advance()
                    print("The path begins to level out and you start to see the end of the corridor. But as you draw closer you realize there is a guard blocking a door at the end of the hall.")
                    advance()
                    print("Filled with a bold spirit you stride up to the door and growl at him to get out of your way. To which he gladly obliges….strange….")
                    ending3()