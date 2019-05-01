# -*- coding: utf-8 -*-
#All of this is very extensive already. I did not complete the final combat sequences because chances are no one wants to fight a demon lord at level 4.
#I have completed 3 combat sequences and have 3 seprate endings to the game, not including player death.


import random

#Initalize Story Elements
global word
global dialogue
global time
dialogue = 0
time = 0

#Initalize Character and Player elements

global character

#Used to display the chosen character's name

global HP
global AC
global Str
global Dex
global Con
global Wis
global Int
global Cha
global Class

#HP (Hit Points), AC (Armor Class), Str (Strength), Dex (Dexterity), Con (Constitution), Wis (Wisdom), Int (Intelegence), and Cha (Charisma)
#Used for the chosen character's stats

global spells
global invocations
global breath
global breath_dc

#For the character Thava, because she is a warlock she has a pool of spell slots and not slots per level like Daern or Whistler
#Thava is a Warlock, meaning aside from spells, she also has Eldrich Invocations. These Invocations are abilities that she can do at will without expanding a spell slot.
#breath is used also for the character Thava, she is a Silver Dragonborn meaning she has a breath attack that does Cold damage (damage is determined by scale color)
#Her breath attack resets after a rest

global spells1 
global spells2
global spells3
global spell_dc
global abilities

#spells1, spells2, and spells3 are used to determine how many spell slots the character has left to use, resets after a rest
#abilities is basically the same as spells 1 2 and 3, but for class and/or race abilities

global slc
global sl1
global sl2
global sl3
global abilititylist

#All the sl variables differ from character to character, used to display what spell the character knows per each level 
#C = Cantrips (No cost), 1 = 1st Level (Uses one 1st level slot), 2 = 2nd Level (Uses one 2nd level slot), and 3 = 3rd Level (Uses one 3rd level slot)
#abilitylist is the same as the sls but for class and/or race abilities

global inventory

#inventory changes per each character, but there are some set items that everyone will have, like a backpack, a torch, and a bedroll.
#The Backpack and the Bedroll are filler for inventory space (Backpack) and the ability to take a rest (Bedroll). The torch can be taken out for a better perception check, giving a bonus of +3 to the roll. 

global inspiration
global inspiration_player

#inspiration is used for the character Whistler, he is a Bard meaning he has Bardic Inspiration. Bardic Inspiration is used by a Bard by stirring faith in them with words or music. 
#In D&D, it allows the player to roll an extra die on any attack or saving throw, but in my game it will be an prompt whenever the character has to make an attack and misses by less than 6 adding an extra value of 1-6 to the attack "roll", but only if they have inspiration.
#inspiration_player is a boolean to determine if the player has inspiration or not.

global ki
global darts
global arrows
global bolts

#ki is used for Lixiss, she is a monk meaning she has something similar to spell slots to use abilities that are specific to monks
#Lixiss has darts and arrows in her inventory, the darts and arrows variables are used to keep track of how many she has left
#bolts is darts but for Daern's crossbow bolts

global exp
global level

#There will be an exp and level up system, but, like D&D, levels take time. There will be no exp rewards from combat, only from certain story events.
#The amount of points needed to level up increases with each level, meaning Daern may be a level 5 cleric, but he will take longer to level up than the other characters.


global choice

#choice is used to make sure that people can't chose a new character

global tb
global db
global lb
global wb

#tb, db, lb, and wb are used as counters for each respective character's backstory to progress to the next partof the backstory

global character_info
global info

#character_info is a boolean to show if the player is viewing character info or not, used to end when the player is looking at the info

global area
global mansion
global mountain
global castle

#area is used to determine which dungeon the player is in
#mansion mountain and castle are used to progress dialogue in each specific dungeon

info = False
spell_dc = 0
breath_dc = 0
word = raw_input('')
arrows = 0
bolts = 0
mansion = 0
mountain = 0
castle = 0
area = ''
character_info = False
tb = 0
db = 0
lb = 0
wb = 0
invocations = []
darts = 0
abilities = 0
abilitylist = []
ki = 0
inspiration = 0
inspiration_player = False
choice = False
spells1 = 0
spells2 = 0
spells3 = 0
slc = []
sl1 = []
sl2 = []
sl3 = []
breath = False
inventory = ['Backpack', 'Bedroll', 'Torch']
exp = 0
level = 0
HP = 0
Class = ''
Str = 0
Dex= 0
Con = 0
Wis = 0
Int = 0
Cha = 0
character = ''
AC = 0

#This is where I initilize all the combat variables and the enemy class

class enemy(object):
    def __init__(self, name, ac, hp, enemy_active):
        self.name = name
        self.ac = ac
        self.hp = hp
        self.enemy_active = enemy_active
global combat
global skeleton
global goblin
global troll
global lich
global dragon
global demon
global boss
global menu
global attack
global enemy_save
global goblin1
global goblin2
global goblin3
global Troll
global goblin1_health
global goblin2_health
global goblin3_health
global skeleton1_health
global skeleton2_health
global skeleton3_health
global troll_health
global dragon_health
global lich_health
global graz_health
global aoe
combat = False
aoe = False
Troll = False
goblin1 = False
goblin2 = False
goblin3 = False
enemies = 0
attack = 0
menu = []
boss = False
skeleton = enemy('Skeleton', 13, 13, True)
goblin = enemy('Goblin', 13, 7, True)
troll = enemy('Troll', 15, 84, True)
lich = enemy('Lich' , 17, 135, True)
dragon = enemy('Dragon', 18, 142, True)
demon = enemy ("Graz'zt", 18, 175, True)

def start_game():
    
    #All of this story and characters are original concepts used in a Dungeons and Dragons campaign I created for my friends
    
    global combat
    global weapon
    global spell_dc
    global aoe
    global arrows
    global info
    global word
    global dialogue
    global character
    global level
    global exp
    global THP
    global DHP
    global LHP
    global WHP
    global AC
    global Str
    global Dex
    global Con
    global Wis
    global Int
    global Cha
    global Class
    global choice
    global invocations
    global spells
    global spells1 
    global spells2
    global spells3
    global slc
    global sl1
    global sl2
    global sl3
    global breath
    global inventory
    global ki
    global inspiration
    global inspiration_player
    global abilities
    global abilitylist
    global darts
    global tb
    global db
    global lb
    global wb
    global character_info
    global area
    global mansion
    global mountain
    global castle
    global goblin
    global bolts
    print '''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    You wake in Darkness. Unable to move or see. You try to call for help but no sound comes out. After what seems like an eternity of trying to scream and
    call for help, a light appears. After a minute or two, the light begins to move closer. Closer and closer, the light begins to blind you, making you 
    feel like you're staring into the sun. Once the sun spots fade, you find yourself in the Sleeping Wyvern Pub. You are sitting at a table listening to 
    a Dwarven man speak of his past adventures.
    
    Type A to continue
    '''
    i = 0
    while i == 0:
        word = raw_input(' ')
        if word == 'end':
            i = 1
        if word == 'end game':
            i = 1
            print 'FiX yOuR dArN gAmE'
        elif word in ('A', 'a'):
            if dialogue == 0:
                dialogue = dialogue + 1
                print '''
    The Dwarf takes a swig of ale large enough to down the whole pint and slams the tankard down on the table. "Aye, I see we have a new visitor, eh? 
    Well, I wasn't too far into my tale so I'll save you the trouble and start from the beginning. But first," he turns his head toward the bar, "WHAT 
    DOES IT TAKE FOR A DWARF TO GET A DRINK AROUND HERE?!?" Reluctantly, the bartender poors the man another pint, mumbling to himself "This better damn 
    well be your last one. You're drinking me out of stock."
    
    Type A to continue
            '''
            elif dialogue == 1:
                dialogue = dialogue + 1
                print '''
    "One day we found a Female Dragonborn with silver scales wandering around, looking for the entrance to Kragghammer. She claimed to be one of the high 
    Dragonborns from the Kingdom of Dragons and she needed counsel with the Dwarven Circle. The exact words she said were "The fate of the world is at stake. 
    Take me to see them NOW!" Realizing what was at stake, I split his platoon in two, having half continue partoling and the other half to come with me to 
    escort the Dragonborn to the Circle. We made their our into Kragghammer and down to the Room of the Circle as fast as possible. "My name is Saphara Cenxac, I 
    am a paladin from the Kingdom of Dragons. Rorviarar, Giver of Life has summoned me here to ask for aid in the upcoming battle against his evil counterpart, 
    Cavrusdien, The Dark One. Please send anyone and everyone you have to help us. The fate of the world is at stake." As she begged and pleaded, she grabbed her 
    holy symbol, two hands bound at the wrist with a red chord, the symbol of Ilmater, God of Endurance. The Circle was speechless, unsure of what to say until 
    one, the Female Barbarian Arra Caldara, stood up and said "I will be the only aly if I have to. I can not, no, I will not let this evil attack my home." She 
    picked up her Battle Axe, and her eyes flashed red, not with anger or hate, but with a feeling of bloodlust. The rest of the Circle shouted in agreement, 
    vowing to help the Kingdom of Dragons and the world. Daern, with the help of a few of his soldiers, patted Saphara on the shoulder, reassuring her that he 
    would help as well. He looked into her eyes and saw that they were a deep and rich blue, speckled with flakes of silver.
    
    Type A to Continue.
    '''
            elif dialogue == 2:
                dialogue = dialogue + 1
                print ''' 
    " After leaving the Room of the Circle, I pulled Saphara aside and asked her, "Why would a Paladin from the Kingdom of Dragons want help from the Dwarven 
    Circle? Surely you have enough Dragonborn forces to take care of Cavrusdien, right?" Saphara just looked down and walked away without looking at Me. Neither 
    of us said anything until I said"Maybe it was Cavrusdien, maybe HE did this. You have to... what if it was your people?" I don't know what I did, but the 
    snow around them stopped in midair and began to be pushed away from her. The snow at her feet started to melt and wings began to sprout from her back. "I... 
    I'm going to KILL YOU!" Saphara shouted as an aura of pure menace erupted from her. She jumped into the air and flew off yelling, "Cavrusdien! Your time has 
    come!" "Follow the Dragonborn! We WILL NOT let this scum destroy our world!" I yelled at my soldiers as I began charging after Saphara. We must've followed 
    her for a half hour at least. Another Dragonborn came out of the storm, by the look of him he was remarkably similar to Saphara. "No Saphara! Stop this 
    futile attack! You of all people should know how utterly USELESS this is! Everyone else is GONE, you can't change that!" Saphara immediately stopped and 
    dropped her weapons, floating in front of Cavrusdien. She turned to look at the Dragonborn that had come through the storn and said, "Tell our daughter I 
    love her." as Cavrusdien recovered from the last blow and extended his arm and grasped her body, there was a cacophony of bones snapping and metal breaking 
    as he crushed her body and ate her. The other Dragonborn was in shock, he was trying to form words but couldn't. Tears began to roll down his cheek and he 
    summoned a black trident adorned with blue flames. "YOU! YOU WILL DIE BY MY HANDS!" he screamed as he ran toward Cavrusdien, readying his trident. He lunged 
    his trident at Cavrusdien, who dodged with ease and began speaking in a gutteral and harsh tone, then turning to us saying, "Leave this 
    place, and your lives will be spared." "
    
    Type A to Continue
                '''
            elif dialogue == 3:
                dialogue = dialogue + 1
                print '''
    " That dragon really pissed me off, I yelled at my men, "CHARGE THE DRAGON! KILL HIM BEFORE THE STORM PASSES!" All the men charged without looking back, trying 
    to assist the Dragonborn as much as possible. We all believed they were making way until Cavrusdien chuckled and said, "I warned you, you should've 
    listened." as he opened his mouth and a great beam rained down on all of my soldiers.I couldn't stand watching my men die. I screamed as the Dragonborn 
    continued his ruthless assault on Cavrusdien. His eyes glossed over and he began attacking as fast and strong as he could. I began praying to my god to 
    empower the Dragonborn and help him defeat Cavrusdien. After a minute or two of praying I lost hope, but as soon as I stopped the Dragonborn's 
    gauntlets began to glow a radiant white, knocking him out of the craze. He dispelled the trident, and held up his glowing gauntlet. "This glow. This will 
    be the last thing you will EVER see." He screamed loudly and shot a bolt of light out of his gauntlet, "You... YOU WILL NEVER TORMENT ANYONE AGAIN! BURN 
    IN THE FIRES OF HELL YOU SCUM!" Cavrusdien screamed as if his soul was being ripped from his body and then everything was still. The snow stopped and where 
    Cavrusdien was standing was a plate-sized token with a dragon emblem on it. "Return to your people," the Dragonborn hissed as if he was on his death bed, 
    "Tell them the threat has been sealed away forever." He must have cast some magic, but a giant gust of wind pushed me back to the entrance to Kraghamer. 
    I couldn't stop thinking about how all of my men died before me and I couldn't do anything about it. I informed the Circle that I would be taking an extended 
    leave of absence. I left the mountain without saying another word and made my way here, to Falcreth." He paused and looked at the table, looking at the Elven 
    woman and Kenku man. "You two. You look like you have some skill. I heard of some jobs that might pay some in the area." He took a piece of paper out of his 
    pocket, "One lady wants a mansion south of here cleared, that seems like good work. Another has to do with... huh, a crypt in the mountains near Kraghammer, 
    it might be good to head back and check up on the city. Oh, and here, The King posted this, 'Wanted, four adventurers with moderate skill. More information 
    upon arrival in the Castle. Will be payed handsomely.' Any of these seem interesting to you? I know I need the gold."
    
    Type A to Continue
                '''
            elif dialogue == 4:
                dialogue = dialogue +1
                print '''
    The Elven woman and the Kenku man turn to each other and shrug. "I guess some extra gold wouldn't hurt." the Kenku says. "If he's on board, then so am I. 
    The name's Lixiss, This is Whistler. We met up on the way here and stuck together for a bit, so I know he's trustworthy. I'm a monk, I need no gold, I just 
    want to help people." The cloaked figure reaches out and grabs the Dwarf's shoulder, a silver and blue gauntlet on their hand, the person whispers in the 
    Dwarf's ear, "I'm in. In return I want answers." the voice sounded female, and young too. "Well then, We have an accord. Let's get outside before we talk 
    more, I need some fresh air after all this ale." The four people make their way outside, one after another with the cloaked one sliding the bartender 10 gold 
    pieces on the way out.
    
    Type A to Read About Characters
                '''
            elif dialogue == 5:
                dialogue = dialogue + 1
                print '''
    First in line is Lixiss Sylphine. An Elven Monk from Irlaqua, the Elven Capital of the empire. She uses her Kensei weapons much like a painter uses a brush, 
    they are an extension of her. Her Kensei weapons are a Scimitar and a Longbow. She is about 5 feet and 7 inches tall with emerald eyes and beautiful blonde 
    hair that she wears in a braid as to keep it out of her way when fighting.
    
    Type A to Continue
                '''
            elif dialogue == 6:
                dialogue = dialogue + 1
                print '''
    Second in line is Whistler. A Kenku Bard from the Tridore Forrest. In some regions, kenku are known as crow people known for their ability to flawlessly 
    immitate any sound they hear. His most known piece of music is the "Waltz of the Myconids", a catchy simple song popular with children for its simplistic 
    style. He is a Bard from the College of Whispers, meaning he knows how to manipulate his words and music in a more malicious and twisting manner to try and 
    gain popularity and power. 
    
    Type A to Continue
                '''
            elif dialogue == 7:
                dialogue = dialogue + 1
                print '''
    Third is Daern Frostbeard. A Dwarven War Cleric from Kraghammer. He mostly specializes in aiding others whenever they need it. He can protect from poison, 
    purify food and water, heal, and restore life to the recently dead. All he wants is to be able to thank the Dragonborn that saved his life back in the 
    mountains. He also wishes to speak with Rorviarar, Giver of Life and King of the Dragons, about the Dragonborn man that saved his life.
    
    Type A to Continue
    '''
            elif dialogue == 8:
                dialogue = dialogue + 1
                print '''
    The cloaked figure, is a mystery. She takes extra precautions to make sure no one sees her face or skin. She gives off a holy yet dark magical aura. She is 
    a warlock who specializes in defeating her enemies as quick as possible. Her patron, the Fiend, is equivilent to that of the devil, thus the dark aura. The 
    holy aura is still a mystery that even she doesn't understand. She wants as much information on any enemy she can obtain due to her researcher-like 
    tendencies.
    
    Type the Name or Class of the Character you wish to choose.
    '''
            elif tb == 1:
                tb = 2
                print '''
    One day, Ilisalor returned with a Flametongue Dagger. When he displayed it to Thava he noticed that the hilt of the blade resembled the same textures and 
    colors of her gauntlets. He dared not ask where she had gotten the gauntlets but he assumed he must have stolen the dagger from the same person she had 
    gotten the gauntlets from and the pair was a set and needed to be together. One day when Ilisalor was out on one of his adventures, Thava left their hideout 
    and made her way back to Erashi, storming up to Rorviarar demanding to know where her gauntlets had come from. Rorviarar looked up from his work, closed his 
    eyes and said quietly, "She really is your daughter Xarturium, she's just as persistent." That day, Thava heard the tale of her father's final fight, the 
    fight that could've ended the world if anything went wrong. Xarturium, who was known as the best Warlock in generations, fought Roravarar's counterpart, the 
    Chaos Dragon Cavrusdien, The Dark One. Xarturium fought without regard for anything around him until he felt the blessing of a Cleric on his gauntlets. 
    Noticing the stout Cleric surrounded by his fallen comrades, his new objective wasn't to save the world, but to save the Dwarf. With his fists glowing with 
    Daern's blessing of Ilmater, God of Endurance, Xarturim was able to deflect Cavrusdien's blows and use his magic to seal him in Limbo, the realm of Chaos.
    
    Type A to read part 3
    '''
            elif tb == 2:
                tb = 3
                print '''
    The amount of magic it took Xarturium to seal away Cavrusdien in Limbo took an lengthy toll on his body and lifeforce. He commanded the Dwarf to leave and 
    never come back, using the last bit of his magical strength to create a gust of wind to push him down the mountain. Xarturium returned to Erashi looking 
    years older than he looked when he had left. He demanded to have an audience with Rorviarar to tell him about the seal he made to keep Cavrusdien trapped 
    in Limbo, but didn't have enough strength to tell him everything. He only told Rorviarar to give his daughter the gauntlets, keep her safe from the rest of 
    the world, and never tell her what happened to her father. His final words were whispered into the newborn Thava's ear before his body burst into small orbs 
    of light before reforming into a Kirin and dashing off into the upper plane. After hearing all of this, Thava was taken aback. She couldn't bring herself to 
    form words. All she could think of was why her father had asked Rorviarar to never tell her what happened. She left without saying a word, making her way 
    back to their hideout where she could truly be alone and think over everything she had just learned. When she arrived at their hideout, one of Ilisalor's 
    companions was there waiting for her. The woman introduced herself as Sylna Faara, and by the way she spoke about Ilisalor, it was almost like she knew him 
    since birth. She told Thava that there was a huge altercation with the local guards and they both had to leave or be arrested. Sylna stayed behind so Ilisalor 
    could get a headstart running from the guards. Thava, after hearing all this news, went directly to Falcreth to try and find information on the Cleric her 
    father had saved.
    
    Type A to finish
    '''
            elif tb == 3:
                tb = 0
            elif db == 1:
                db = 2
                print '''
    Daern, realizing what was at stake, split his platoon in two having half continue partoling and the other half to come with him to escort the Dragonborn to 
    the Circle. They made their way into Kragghammer and down to the Room of the Circle, bypassing all unnecessary routes and taking as many shortcuts as they 
    could. When they made it to the Room of the Circle, they found that the Circle was about to summon Daern to have him give his daily report. The Dragonborn 
    cast aside Daern, making her presence known. "My name is Saphara Cenxac, I am a paladin from the Kingdom of Dragons. Rorviarar, Giver of Life has summoned me 
    here to ask for aid in the upcoming battle against his evil counterpart, Cavrusdien, The Dark One. Please send anyone and everyone you have to help us. The 
    fate of the world is at stake." As she begged and pleaded, she grabbed her holy symbol, two hands bound at the wrist with a red chord, the symbol of Ilmater, 
    God of Endurance. The Circle was speechless, unsure of what to say until one, the Female Barbarian Arra Caldara, stood up and said "I will be the only aly if 
    I have to. I can not, no, I will not let this evil attack my home." She picked up her Battle Axe, and her eyes flashed red, not with anger or hate, but with 
    a feeling of bloodlust. The rest of the Circle shouted in agreement, vowing to help the Kingdom of Dragons and the world. Daern, with the help of a few of 
    his soldiers, patted Saphara on the shoulder, reassuring her that he would help as well. He looked into her eyes and saw that they were a deep and rich blue, 
    speckled with flakes of silver.
    
    Type A to read part 3
    '''
            elif db == 2:
                db = 3
                print '''
    After leaving the Room of the Circle, Daern pulled Saphara aside and asked her, "Why would a Paladin from the Kingdom of Dragons want help from the Dwarven 
    Circle? Surely you have enough Dragonborn forces to take care of Cavrusdien, right?" Saphara just looked down and walked away without looking at Daern. The 
    whole way back to where Daern had stationed his men Saphara didn't say a word. When they arrived at the station, none of Daern's men were there, and there 
    was no sign of them leaving, they just disappeared. Daern begged and pleaded to Saphara, but all she did was stare off into the distance. For about 10 
    minutes Daern screamed and begged her to help but she didn't budge until he said "Maybe it was Cavrusdien, maybe HE did this. You have to... what if it was 
    your people?" Those last 6 words flipped a switch in Saphara, the snow around them stopped in midair and began to be pushed away from her. The snow at 
    her feet started to melt and wings began to sprout from her back. "I... I'm going to KILL YOU!" Saphara shouted as an aura of pure menace erupted from her. 
    She jumped into the air and flew off yelling, "Cavrusdien! Your time has come!"
    
    Type A to read part 4
    '''
            elif db == 3:
                db = 4
                print '''
    "Follow the Dragonborn! We WILL NOT let this scum destroy our world!" Daern yelled at his soldiers as he began charging after Saphara. He followed the glow 
    of her aura through the devistating snowstorm. By the time he caught up with her, she had already began attacking Cavrusdien. As they readied their weapons 
    another Dragonborn came out of the storm, by the look of him he was remarkably similar to Saphara. "No Saphara! Stop this futile attack! You of all people 
    should know how utterly USELESS this is! Everyone else is GONE, you can't change that!" Saphara immediately stopped and dropped her weapons, floating in 
    front of Cavrusdien. She turned to look at the Dragonborn that had come through the storn and said, "Tell our daughter I love her." as Cavrusdien recovered 
    from the last blow and extended his arm and grasped her body, there was a cacophony of bones snapping and metal breaking as he crushed her body and ate her. 
    The other Dragonborn was in shock, he was trying to form words but couldn't. Tears began to roll down his cheek and he summoned a black trident adorned with 
    blue flames. "YOU! YOU WILL DIE BY MY HANDS!" he screamed as he ran toward Cavrusdien, readying his trident. He lunged his trident at Cavrusdien, who dodged 
    with ease and began speaking in a gutteral and harsh tone, then turning to Daern and his soldiers saying, "Leave this place, and your lives will be spared." 
    
    
    Type A to read part 4.
    '''
            elif db == 4:
                print '''
    Daern, aggitated by the Dragon, commanded his men, "CHARGE THE DRAGON! KILL HIM BEFORE THE STORM PASSES!" All the men charged without looking back, trying 
    to assist the Dragonborn as much as possible. Everyone believed they were making way until Cavrusdien chuckled and said, "I warned you, you should've 
    listened." as he opened his mouth and a beam rained down on all of his soldiers. He collapsed into the snow and screamed as the Dragonborn continued his 
    ruthless assault on Cavrusdien. His eyes glossed over and he began attacking as fast and strong as he could. Daern began praying to his god, Ilmater, to 
    empower the Dragonborn and help him defeat Cavrusdien. Daern lost hope after a minute or two of playing, but as soon as he stopped the Dragonborn's 
    gauntlets began to glow a radiant white, knocking him out of the craze. He dispelled the trident, and held up his glowing gauntlet. "This glow. This will 
    be the last thing you will EVER see." He screamed loudly and shot a bolt of light out of his gauntlet, "You... YOU WILL NEVER TORMENT ANYONE AGAIN! BURN 
    IN THE FIRES OF HELL YOU SCUM!" Cavrusdien screamed as if his soul was being ripped from his body and then everything was still. The snow stopped and where 
    Cavrusdien was standing was a plate-sized token with a dragon emblem on it. "Return to your people," the Dragonborn hissed as if he was on his death bed, 
    "Tell them the threat has been sealed away forever." He lifted his hand and a gust of wind pushed Daern back to the entrance to Kraghammer. After the loss 
    of all his soldiers, he informed the Circle of what events transpired as well as informing them he would be taking an extended leave of absence to help 
    himself recover. He made his way to the trading port of Falcreth to start his journey of recovery.
    
    Type A to finish.
    '''
            elif character_info == True:
                character_info = False
            elif area == 'mansion':
                if mansion == 1:
                    mansion = 2
                    print '''
    "I can translate this book for you. The cover is in Abyssal so I think I'll be able to translate it directly. It says 'The Curse of The Lich', I'm not sure 
    if this is something we should be messing with." Lixiss begins to place the book back where she found it when Thava approaches her, grabbing her hand saying, 
    "Read it. I need to know." As she releases Lixiss' hand, a worried look begins to appear on Lixiss' face, "If you need to know, I will translate it for you." 
    She takes a deep breath, almost as if she was praying, and began to read the book to herself to discern if she should be speaking the words aloud. About 20 
    or 30 minutes goes by and she finally begins to read aloud, "This book is real, I don't know anything about magic, but this book definitely has some. Here 
    goes nothing, 'The Lich is a being that appears once in a thousand lifetimes, usually a powerful necromancer or a King seeking eternal life. These beings 
    bind their intellect and soul to a container or vessel allowing them to achieve a form of immortality. The Lich can be decieving in appearance, appearing 
    as a young magician or King, but can also appear as a ghastly spectral form. To truly destroy a Lich you must destroy the container or vessel they bound 
    themselves to. In some cases the Lich will keep their vessel locked away and safe from harm, but it may keep the vessel on it at all times.' Guys, this 
    book, its... I'm getting a bad feeling." She closes the book and puts it on the ground and glances at Thava, "Was that enough information for you?" Thava, 
    who had written down all the information, looks at Lixiss with a solemn face and replys, "I... yes. Thank you, Lixiss." Whistler looks at the group and 
    says, "Do you mind if I take the book? It may help my people find a solution to what happened in our forrest." He slowly reaches for the book, waiting for 
    any sign of resistance but finding none. He opens his pack, wrapps the book in a shirt, and slides it in.
    
    Type A to continue
    '''
                    if character == 'Thava':
                        inventory.append('Notes')
                        print '''
    You have obtained notes on the Lich.
    '''
                    if character == 'whistler':
                        inventory.append('Lich Book')
                        print '''
    You have obtained "The Curse of The Lich"
    '''
                elif mansion == 2:
                    mansion = 0
                    print '''
    After everyone is done in the foyer of the mansion, you move to a set of stairs in the back of the room that lead down into a basement level. The noises
    seem to be coming from that direction. As you move down the stairs Daern moves first, followed by Lixiss, then Thava, and in the rear Whistler. Lixiss 
    whispers to the group, "I think we should try and stealth, that way we coud catch whoever is doing this by surprise." Everyone moves only one step at a 
    time as to not make any noise. Once everyone makes it to the bottom of the stairs you begin to head toward the sound of wood breaking and glass shattering.
    Daern begins to peak around a corner when the wall he is holding collapses and a loud rumble echoes throughout the almost-vacated mansion. The noises and 
    laughter stop immediately. "Great, now they know we're here. Nice job 'altar boy'." Lixiss scoffs at Daern. "'Altar Boy' eh? Never heard that one before. 
    You think you could've done better, Mrs. 'Punchy Princess'?" Thava pulls them apart, "Now is not the time to be fighting amongst ourselves, settle it later. 
    For now we have to deal with whatever is coming for us now." Whistler, who was standing back to try and not be caught in the middle of this, runs up 
    alerting the group, "GOBLINS!"
    
    Type A to initiate combat with Goblins
    '''
                    combat(goblin)
            elif area == 'mountains':
                combat(skeleton)
            elif area == 'castle':
                i = 17.332
                print '''
    Congratulations, you win. You completed the story. Hope you had fun.
    '''
        elif word in ('backstory', 'Backstory', 'Background', 'background'):
            if character == 'thava':
                tb = 1
                if tb == 1:
                    print '''
    Thava Alviir is the last surviving Dragonborn after the great war. Her father was, according to legend, the final Dragonborn and was recorded to have died 
    in order to to stop the great war. Daern told of a Dragonborn with the same gauntlets that Thava wears that, upon thinking back, looked remarkably  similar 
    to Thava. Thava grew up in the neighboring Kingdom, the Kingdom of Dragons: Erashi and was raised by their leader, the Radiant Dragon Rorviarar, Giver of 
    Life. After Rorviarar heard of her father, Xarturium Cenxac, laying down his life in order to protect a Dwarven Cleric, he decided to take in Xarturium's 
    newborn daughter, Thava Cenxac, and teach her the ways of the warlock and have her follow in the steps of her late father, having her study demons and 
    creatures from the Lower Planes. At the age of 17 she ran away from Erashi and went to pursue a career of her own in the Kingdom of Men. While venturing 
    around to try and find work, she stumbled across a Drow man by the name of Ilisalor Alviir. Ilisalor took her in, in an effort to protect her knowing full 
    well what she was, and taught her how to survive by making a living for herself. He called it the "old-fashioned way", but anyone who knows anything would 
    call it stealing.
    
    Type A to read part 2
    '''
            elif character == 'daern':
                db = 1
                if db == 1:
                    print '''
    Daern Frostbeard lived a pretty normal life. He ran his own hospital and helped the superstitious protect themselves from evil. But that life was boring for 
    him. He was at the ripe old age of 127 when he enlisted into the Regime at Kraghammer. Due to his exceptional healing abilities, he was promoted to
    Brigadier General where he headed a platoon of 25 Dwarven soldiers. Daern and the 239th Dwarven Division were tasked with keeping the location of Kragghammer 
    safe from intruders. Most days, the only people they interacted with were climbers who didn't know any better, occasionally a warrior or embassy from one of 
    the neighboring lands came to have counsel with the Dwarven Circle, a group of 9 Dwarves that control most of Kragghammer. One day they found a Female 
    Dragonborn with silver scales wandering around, looking for the entrance to Kragghammer. She claimed to be one of the high Dragonborns from the Kingdom of 
    Dragons and she needed counsel with the Dwarven Circle. The exact words she said were "The fate of the world is at stake. Take me to see them NOW!"
    
    Type A to read part 2
    '''
            elif character == 'lixiss':
                print '''
    INCOMPLETE!!!1! CHECK BACK WHEN I TELL YOU TO.
    '''
            elif character == 'whistler':
                print '''
    Restart the game, choose Lixiss and check her backstory.
    '''

#backstory is a command where if you enter one of the inputs ('backstory', 'Backstory', 'Background', 'background') once your character has been chosen
#you will be able to read a little blurb about their history and motives for doing what they do.

        elif word in ('Thava', 'thava', 'cloaked figure', 'Cloaked Figure', 'warlock', 'Warlock', 'wa', 't', 'T', 'Wa', 'Daern', 'daern', 'dwarf', 'Dwarf', 'cleric', 'Cleric', 'd', 'D', 'c', 'C', 'Lixiss', 'lixiss', 'elf', 'Elf', 'monk', 'Monk', 'L', 'l', 'M', 'm', 'Whistler', 'whistler', 'bird', 'Bird', 'Kenku', 'kenku', 'crow', 'Crow', 'bard', 'Bard', 'B', 'b', 'wh', 'Wh'):
            if dialogue >= 4:
                if choice == False:
                    if word in ('Thava', 'thava', 'cloaked figure', 'Cloaked Figure', 'warlock', 'Warlock', 'wa', 't', 'T', 'Wa'):
                        character = 'thava'
                        Class = 'Warlock'
                        level = 4
                        exp = 0
                        THP = 35
                        AC = 10
                        Str = 8
                        Dex = 11
                        Con = 13
                        Wis = 16
                        Int = 16
                        Cha = 14
                        abilities = 0
                        breath = True
                        abilitylist = ["Dark One's Blessing", 'Cold Breath']
                        spells = 2
                        slc = ['Friends', 'Chill Touch', 'Prestidigitation', 'Eldritch Blast', 'Vicious Mockery']
                        sl1 = ['Burning Hands', 'Command', 'Cure Wounds', 'Unseen Servent', 'Arms of Hadar' ,'Hellish Rebuke', 'Protection From Evil']
                        sl2 = ['blindness/Deafness', 'Scorching Ray', 'Shadow Blade']
                        sl3 = []
                        invocations = ['Mask of Many Faces', 'Eldritch Spear']
                        inventory.append('Quarterstaff')
                        inventory.append('Spellbook')
                        dialogue = 9
                        choice = True
                        print 'You have chosen the Warlock Thava Alviir.'
                        print '''
    Type which area you would like to go to, Mansion, Mountains, or Castle.
    '''
                    elif word in ('Daern', 'daern', 'dwarf', 'Dwarf', 'cleric', 'Cleric', 'd', 'D', 'c', 'C'):
                        character = 'daern'
                        Class = 'Cleric'
                        level = 5
                        exp = 0
                        DHP = 32
                        AC = 16
                        Str = 16
                        Dex = 12
                        Con = 16
                        Wis = 12
                        Int = 18
                        Cha = 12
                        abilities = 0
                        abilitylist = []
                        spells1 = 4
                        spells2 = 3
                        spells3 = 2
                        slc = ['Light', 'Spare the Dead', 'Sacred Flame', 'Thaumaturgy', 'Message', 'Eldrich Blast']
                        sl1 = ['Divine Favor', 'Shield of Faith', 'Command', 'Create/Destroy Water', 'Cure Wounds', 'Healing Word', 'Purify Food and Drink', 'Sanctuary']
                        sl2 = ['Aid', 'Poison Protect', 'Find Traps']
                        sl3 = ['Meld into Stone', 'Revivify', 'Animate Dead']
                        inventory.append('Warhammer')
                        inventory.append('Hand Axe')
                        inventory.append('Light Crossbow')
                        inventory.append('Bolts')
                        inventory.append('Rank Insignia')
                        inventory.append('Resurrection Scroll')
                        bolts = 20
                        dialogue = 9
                        choice = True
                        print 'You have chosen the Cleric Daern Frostbeard.'
                    elif word in ('Lixiss', 'lixiss', 'elf', 'Elf', 'monk', 'Monk', 'L', 'l', 'M', 'm'):
                        character = 'lixiss'
                        Class = 'Monk'
                        level = 4
                        exp = 0
                        LHP = 32
                        AC = 17
                        Str = 18
                        Dex = 20
                        Con = 12
                        Wis = 12
                        Int = 10
                        Cha = 12
                        ki = 4
                        abilities = 0
                        abilitylist = ['Deflect Missiles', 'Agile Parry', 'Flurry of Blows', 'Patient Defense']
                        inventory.append('Scimitar')
                        inventory.append('Longbow')
                        inventory.append('Quarterstaff')
                        inventory.append("Dungeoneer's Pack")
                        inventory.append('Darts')
                        arrows = 20
                        darts = 10
                        dialogue = 9
                        choice = True
                        print 'You have chosen the Monk Lixiss Sylphine.'
                    elif word in ('Whistler', 'whistler', 'bird', 'Bird', 'Kenku', 'kenku', 'crow', 'Crow', 'bard', 'Bard', 'B', 'b', 'wh', 'Wh'):
                        character = 'whistler'
                        Class = 'Bard'
                        level = 4
                        exp = 0
                        WHP = 21
                        AC = 15
                        Str = 8
                        Dex = 14
                        Con = 10
                        Wis = 13
                        Int = 9
                        Cha = 18
                        inspiration = 4
                        abilities = 0
                        abilitylist = ['Psychic Blades', 'Bardic Inspiration']
                        spells1 = 4
                        spells2 = 3
                        spells3 = 0
                        slc = ['Vicious Mockery', 'Light', 'True Strike']
                        sl1 = ['Dissonant Whispers', "Tasha's Hideous Laughter", 'Sleep', 'Thunderwave']
                        sl2 = ['Suggestion', 'Silence', 'Shatter']
                        sl3 = []
                        inventory.append('Rapier')
                        inventory.append("Diplomat's Pack")
                        inventory.append('Lute')
                        inventory.append('Dagger')
                        dialogue = 9
                        choice = True
                        print 'You have chosen the Bard Whistler.'
        elif word in ('check inventory', 'inventory', 'i', 'Check Inventory', 'Inventory', 'I'):
            if choice == True:
                print 'Your inventory consists of: %s' %inventory
        elif word in ('character', 'Character', 'c', 'C'):
            character_info = True
            character_info()
            if character_info == True:
                if word in ('spells', 'Spells', 'abilities', 'Abilities'):
                    description()
                    if info == True:
                        if word in ('bardic inspiration', 'Bardic Inspiration', 'Inspiration', 'Inspiration') and ('info', 'Info'):
                            info = False
                            print '''
   Bardic Inspiration:
       Use a bonus action on your turn to give one creature of your choice Bardic Inspiration. They can add 1d8 to any attack or saving throw.
   
   Type A to finish.
   '''
                        elif word in ('Psychic Blades', 'psychic blades') and ('info', 'Info'):
                            info = False
                            print '''
   Psychic Blades:
       When you hit a creature with a weapon attack, you can expend one use of your Bardic Inspiration to deal an extra 2d6 psychic damage to that target. 
       You can do so only once per round on your turn.
   
   Type A to finish.
   '''
                        elif word in ('Deflect Missiles', 'deflect missiles') and ('info', 'Info'):
                            info = False
                            print '''
   Deflect Missiles:
       You can use your reaction to deflect or catch the missile when you are hit by a ranged weapon attack. When you do so, the damage you take from the 
       attack is reduced by 1d10 + your Dexterity modifier + your monk level.
   
   Type A to finish.
   '''
                        elif word in ('Patient Defense', 'patient defense') and ('info', 'Info'):
                            info = False
                            print '''
   Patient Defense:
       You can spend 1 Ki point to dodge the next attack.
   
   Type A to finish.
   '''
                        elif word in ('Flurry of Blows', 'flurry of blows') and ('info', 'Info'):
                            info = False
                            print '''
   Flurry of Blows:
       Immediately after you take the Attack action on your turn, you can spend 1 ki point to make two unarmed strikes as a bonus action.
   
   Type A to finish.
   '''
                        elif word in ('Agile Parry', 'agile parry') and ('info', 'Info'):
                            info = False
                            print '''
   Agile Parry:
       If you make an unarmed strike as part of the Attack action on your turn you gain a +2 bonus to AC until the start of your next turn.
   
   Type A to finish.
   '''
                        elif word in ("Kensei's Shot", "kensei's shot") and ('info', 'Info'):
                            info = False
                            print '''
   Kensei's Shot:
     You can use a bonus action on your turn to make your ranged attacks with a kensei weapon more deadly. When you do so, any target you hit with a ranged 
     attack takes an extra 1d4 damage of the weapon’s type. You retain this benefit until the end of the current turn.
   
   Type A to finish.
   '''
                        elif word in ('Cold Breath', 'cold breath') and ('info', 'Info'):
                            info = False
                            print '''
   Cold Breath:
       When you use your breath weapon, each creature must make a Constitution saving throw. The DC for this saving throw equals 8 + your Constitution modifier 
       + your Proficiency Bonus. A creature takes 2d6 cold damage on a failed save, and half as much damage on a successful one.
   
   Type A to finish.
   '''
                        elif word in ("Dark One's Blessing", "dark one's blessing") and ('info', 'Info'):
                            info = False
                            print '''
   Dark One's Blessing:
       When you reduce a hostile creature to 0 hit points, you gain temporary hit points equal to your Charisma modifier + your warlock level
   
   Type A to finish.
   '''
                        elif word in ('friends', 'Friends') and ('info', 'Info'):
                            info = False
                            print '''
    Friends:
        For the duration (1 minute), you have advantage on all Charisma checks directed at one creature of your choice that isn't hostile toward you.
    
    Type A to finish.
    '''
                        elif word in ('Chill Touch', 'chill touch') and ('info', 'Info'):
                            info = False
                            print '''
    Chill Touch:
        You create a ghostly, skeletal hand in the space of a creature. On a hit, the targtet takes 1d8 necrotic damage and can't regain hit points until 
        the start of your next turn. If you hit an undead target, it also has disadvantage on attacks against you until the end of your next turn.
    
    Type A to finish.
    '''
                        elif word in ('Prestidigitation', 'prestidigitation') and ('info', 'Info'):
                            info = False
                            print '''
    Prestidigitation:
        The spell is a minor magical trick that novice spellcasters use for practice. You create one of the following magical effects:
            -You create an instantaneous, harmless sensory effect, such as a shower of sparks, a puff of wind, faint musical notes, or an odd odor.
            -You instantaneously light or snuff out a candle, a torch, or a small campfire.
            -You instantaneous clean or sil an object no larger than 1 cubic foot.
            -You chill, warm, or flavor up to 1 cubic foot of nonliving material for 1 hour.
            -You make a color, a small mark, or a symbol appear on an object or surface for 1 hour.
            -You create a nonmagical trinket or illusory image that can fit in your hand that lasts until the end of your next turn.
    
    Type A to finish.
    '''
                        elif word in ('Eldritch Blast', 'eldritch blast') and ('info', 'Info'):
                            info = False
                            print '''
    Eldritch Blast:
        A beam of crackling energy streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 
        force damage.
    
    Type A to finish.
    '''
                        elif word in ('Vicious Mockery', 'vicious mockery') and ('info', 'Info'):
                            info = False
                            print '''
    Vicious Mockery:
        You unleash a string of insults laced with subtle enchantments at a creature you can see within range. If the target canhear you, though it need not 
        understand you, it must succed on a Wisdom saving throw or take 1d4 psychic damage and have disadvantage on the next attack roll it makes before the 
        end of its next turn.
    
    Type A to finish.
    '''
                        elif word in ('light', 'Light') and ('info', 'Info'):
                            info = False
                            print '''
    Light:
        You touch one object that is no larger than 10 feet in any dimension. Until the spell ends, the object sheds a bright light in a 20 foot radius.
    
    Type A to finish.
    '''
                        elif word in ('Spare the Dead', 'spare the dead') and ('info', 'Info'):
                            info = False
                            print '''
    Spare the Dead:
        You touch a living creature that has 0 Hit Points. The creature becomes stable. This spell has no effect on undead or constructs.
    
    Type A to finish.
    '''
                        elif word in ('sacred flame', 'Sacred Flame') and ('info', 'Info'):
                            info = False
                            print '''
    Sacred Flame:
        Flame-like radiance decends on a creature that you can see. The target mus suced a Dexterity saving throw or take 1d8 radiant damage. The 
        target gains no benefit from cover for this saving throw.
    
    Type A to finish.
    '''
                        elif word in ('Thaumaturgy', 'thaumaturgy') and ('info', 'Info'):
                            info = False
                            print '''
    Thaumaturgy:
        You manifest a minor wonder, a sign of supernatureal power, within range. You create one of the following magical effects within range:
            -Your voice booms up to three times as loud for 1 minute.
            -You cause flames to flicker, brighten, dim, or change color for 1 minute.
            -You cause harmless tremors inthe ground for 1 minute.
            -You create an instantaneous sound that originates from a point of your choice, such as a rumble of thunder, the cry of a raven, or ominous whispers.
            -You instantaneously cause an unlocked door or window to fly open or slam shut.
            -You alter the appearance of your eyes for 1 minute.
    
    Type A to finish.
    '''
                        elif word in ('Message', 'message') and ('info', 'Info'):
                            info = False
                            print '''
    Message:
        You point your finger toward a creature within range and whisper a message. The target, and only the target, hears the message and can reply in a 
        whisper that only you can hear.
    
    Type A to finish.
    '''
                        elif word in ('true strike', 'True Strike') and ('info', 'Info'):
                            info = False
                            print '''
    True Strike:
        You extend your hand and point a finger at a target. Your magic grants you a brief insight to the target's defenses. On your next turn you gain advantage 
        on your first attack against the target.
    
    Type A to finish.
    '''
                        elif word in ('burning hands', 'Burning Hands') and ('info', 'Info'):
                            info = False
                            print '''
    Burning Hands:
        As you hold your hands with thumbs touching and fingers spread, a thin sheet of flames shoots forth from your outstreached fingertips. Each 
        creature must make a Dexterity saving throw. A creature takes 3d6 fire damage of a failed save, or half as much on a successful one.
    
    Type A to finish.
    '''
                        elif word in ('command', 'Command') and ('info', 'Info'):
                            info = False
                            print '''
    Command:
        You speak a one word command to a creature you can see. The target must succed on a Wisdom saving throw or follow the command on its next turn. 
        The spell has no effect if the target is undead, if it doesn't understand your language, or if your command is to directly harmful to it.
    
    Type A to finish.
    '''
                        elif word in ('Unseen Servant', 'unseen servant') and ('info', 'Info'):
                            info = False
                            print '''
    Unseen Servant:
        This spell creates an invisible, mindless, chapeless force taht performs simple tasks at your command until the spell ends. The servant can perform 
        simple tasks that a human servant could do, such as fetching things, cleaning, mending, folding clothes, lighting fires, serving food, and pouring wine.
    
    Type A to finish.
    '''
                        elif word in ('Arms of Hadar', 'arms of hadar') and ('info', 'Info'):
                            info = False
                            print '''
    Arms of Hadar:
        You invoke the power of Hadar, the Dark Hunger. Tendrils of dark energy erupt from you and batter all creatures. Each creature mus make a Strength 
        saving throw. On a failed save, a target takes 2d6 necrotic damage. On a successful save, the creature takes half damage.
    
    Type A to finish.
    '''
                        elif word in ('hellish rebuke', 'Hellish Rebuke') and ('info', 'Info'):
                            info = False
                            print '''
    Hellish Rebuke:
        You point your finger, and the creature that damaged you is momentarily surrounded by hellish flames. The creature must make a Dexterity saving throw. It 
        takes 2d10 fire damage on a failed save, or half as much damage on a successful one.
    
    Type A to finish.
    '''
                        elif word in ('Protection from Evil', 'protection from evil') and ('info', 'Info'):
                            info = False
                            print '''
    Protection from Evil:
        Until the spell ends, one willing creature you touch is protected agains certain types of creatures: abberations, celesstials, elementals, fey, fiends, 
        and undead.
    
    Type A to finish.
    '''
                        elif word in ('Divine Favor', 'divine favor') and ('info', 'Info'):
                            info = False
                            print '''
    Divine Favor:
        Your prayer empowers you with divine radience. Untell the spell ends, your weeapon attacks deal an extra 1d4 radiant damage on a hit.
    
    Type A to finish.
    '''
                        elif word in ('Shield of Faith', 'shield of faith') and ('info', 'Info'):
                            info = False
                            print '''
    Shield of Faith:
        A shimmering field appears and surrounds a creature of your choice within range, granting it a +2 bonus to AC for the duration.
    
    Type A to finish.
    '''
                        elif word in ('Create/Destroy Water', 'create/destroy water') and ('info', 'Info'):
                            info = False
                            print '''
    Create/Destroy Water:
        You can either create or destroy water.
        CREATE WATER: You can create up to 10 galons of clean water within range in an open container.
        DESTROY WATER: You destroy up to 10 galons of water in an open container within range.
    
    Type A to finish.
    '''
                        elif word in ('Cure Wounds', 'cure wounds') and ('info', 'Info'):
                            info = False
                            print '''
    Cure Wounds:
        A creature you touch regains a number of Hit Points equal to 1d8 + your spellcasting ability modifier. This spell has no effect on undead or constructs.
    
    Type A to finish.
    '''
                        elif word in ('Healing Word', 'healing word') and ('info', 'Info'):
                            info = False
                            print '''
    Healing Word:
        A creature of your choice that you can see within range regains hit points equal to 1d4 + your spellcasting ability modifier. This spell has no effect 
        on undead or constructs.
    
    Type A to finish.
    '''
                        elif word in ('Purify Food and Drink', 'purify food and drink') and ('info', 'Info'):
                            info = False
                            print '''
    Purify Food and Drink:
        All nonmagical food and drink within a 5 foot radius sphere centered on a point of your choice is purified and rendered free of poison and disease.
    
    Type A to finish.
    '''
                        elif word in ('Sanctuary', 'sanctuary') and ('info', 'Info'):
                            info = False
                            print '''
    Sanctuary:
        You ward a creature within range against attack. Until the spell ends, any creature who targets the warded creature with an attadck or harmful spell 
        must first make a Wisdom saving throw. On a failed save, the creature must choose a new target or lose the attack or spell. The spell doesn't protect 
        the warded creature from area effects, such as an explosion.
    
    Type A to finish.
    '''
                        elif word in ('Dissonant Whispers', 'dissonant whispers') and ('info', 'Info'):
                            info = False
                            print '''
    Dissonant Whispers:
        You whisper a discordant melody that only one creature of your choice can hear, wracking it with terrible pain. The target must make a Wisdom saving 
        throw. On a failed save, it takes 3d6 psychic damage and must immediately use its reaction, if available, to flee. On a successful save, the target 
        takes half as much damage and doesn't have to flee.
    
    Type A to finish.
    '''
                        elif word in ("Tasha's Hideous Laughter", "tasha's hideous laughter") and ('info', 'Info'):
                            info = False
                            print '''
    Tasha's Hideous Laughter:
        A creature of your choice that you can see within range percieves everything as hilariously funny and falls into fits of laughter if this spell affects 
        it. The target must succed on a Wisdom saving throw or fall prone, becoming incapacitated and unable to stand up for the dur4ation. A creature with an 
        Intelligence score of 4 or less isn't affected.
    
    Type A to finish.
    '''
                        elif word in ('Sleep', 'sleep') and ('info', 'Info'):
                            info = False
                            print '''
    Sleep:
        The spell sends creatures into a magical slumber. Roll 5d8; the total is how many hit points of creatures the spell can affect. 
    
    Type A to finish.
    '''
                        elif word in ('thunderwave', 'Thunderwave') and ('info', 'Info'):
                            info = False
                            print '''
    Thunderwave:
        A wave of thunderous force sweeps out rom you. Each creature mus make a Constitution saving throw. On a failed save a creatuer takes 2d8 thunder damage.
        On a successful save, the creature takes half as much damage.
    
    Type A to finish.
    '''
                        elif word in ('Blindness/Deafness', 'blindness/deafness') and ('info', 'Info'):
                            info = False
                            print '''
    Blindness/Deafness:
        youi can blind or deafen a foe. Choose one creature that you can see to make a Consititution saving throw. If it fails, the target is either blinded 
        or deafened (your choice). At the end of each of its turns, the target must make a Constitution saving throw. On a success the spell ends.
    
    Type A to finish.
    '''
                        elif word in ('Scorching Ray', 'scorching ray') and ('info', 'Info'):
                            info = False
                            print '''
    Scorching Ray:
        You create three rays of fire and hurl them at targets. You can gurl them at one target or several. Make a ranged spell attack for each ray. On a hit, 
        the target takes 2d6 fire damage.
    
    Type A to finish.
    '''
                        elif word in ('Shadow Blade', 'Shadow Blade') and ('info', 'Info'):
                            info = False
                            print '''
    Shadow Blade:
        You weave together threads of hsadow to create a sword of solidified gloom in your hand. This magic sword lasts until the spell ends. It counts as a 
        simple melee weapon with which you are proficient. It deals 2d8 psychic damage on a hit and has the finesse, light, and thrown properties. When you 
        use the blade to attack a target that is in dim light or darkenss you make the attack with advantage.
    
    Type A to finish.
    '''
                        elif word in ('Aid', 'aid') and ('info', 'Info'):
                            info = False
                            print '''
    Aid:
        Your spell bolsters your allies with toughness and resolve. Choose up to three creatures, 
        each target's hit point maximum and current hit points increase by 5 for the duration.
        
    Type A to finish.
    '''
                        elif word in ('Poison Protect', 'poison protect') and ('info', 'Info'):
                            info = False
                            print '''
    Poison Protect:
        You touch a creature. If it is poisoned, you neutralize the poison. If more than one poison afflicts the target, you neutralize one poison that you know is present, 
        or you neutralize one at random.
    
    Type A to finish.
    '''
                        elif word in ('Find Traps', 'find traps') and ('info', 'Info'):
                            info = False
                            print '''
    Find Traps:
        You sense the presence of any trap within your sight. A trap, for the purpose of this spell, includes anything that would inflict a sudden or 
        unexpected effect you consider harmful or undesirable, which was specifically intended as such by its creator.
    
    Type A to finish.
    '''
                        elif word in ('Suggestion', 'suggestion') and ('info', 'Info'):
                            info = False
                            print '''
    Suggestion:
        You suggest a course of activity (limited to a scentence or two) and magically influence a creature you can see within range that can hear and understand 
        you. Creatures that can'[t be charmed are immune to this effect. The suggestion must be worded in such a manner as to make the course of action sound 
        reasonable. The target must make a Wisdom saving throuw. On a failed save, it pursues the course of action you described to the best of its ability.
    
    Type A to finish.
    '''
                        elif word in ('Silence', 'silence') and ('info', 'Info'):
                            info = False
                            print '''
    Silence:
        For the duration(10 minutes), no sound can be created within or pass through a 20 foot radius sphere centered on a point you choose. Any creature or 
        object entirely inside the sphere is iummune to thunder damage, and creatures are deafened while currently inside it.
    
    Type A to finish.
    '''
                        elif word in ('Shatter', 'shatter') and ('info', 'Info'):
                            info = False
                            print '''
    Shatter:
        A sudden loud ringing noise, painfully intense, erupts from a point of your choice within range. Each creature must make a Constitution saving throw. A 
        creature takes 3d8 thunder damage on a failed save, or half as much on a successful one. A creature made of inorganic material such as stone, crystaal, 
        or metal has disadvantage on the saving throw.
    
    Type A to finish.
    '''
                        elif word in ('Meld into Stone', 'meld into stone') and ('info', 'Info'):
                            info = False
                            print '''
    Meld into Stone:
        You step into a stone object or surface large enough to fully contain your body, melding yourself and all the equipment you carry with the stone for the 
        duration. 
    
    Type A to finish.
    '''
                        elif word in ('Revivify', 'revivify') and ('info', 'Info'):
                            info = False
                            print '''
    Revivify:
        You touch a creature that has died within the last minute. That creature returns to life with 1 hit point. The spell can't return to life a creature that 
        has died of old age, nor can it restore any mmissing body parts.
    
    Type A to finish.
    '''
                        elif word in ('Animate Dead', 'animate dead') and ('info', 'Info'):
                            info = False
                            print '''
    Animate Dead:
        This spell creates an undead servant. Choose a pile of bones or a corpse of a medium or small humanoid. Your spell imbues the targed with a 
        foul mimicry of life, raising it as an undead creature. The target becomes a skeleton if you chose bones or zombie if you chose corpse. On each 
        of your turns, you can use a bonus action to mentally command any creature you made with this spell.
    
    Type A to finish.
    '''
        elif dialogue == 9 and choice == True:
            if word in ('mansion', 'Mansion', 'house', 'House'):
                area = 'mansion'
                mansion = 1
                print '''
    You and your comrades arrive at the mansion. All of the windows are either boarded up or shattered, and the shed in the back seems to have collapsed. 
    You can hear noises coming from inside the mansion almost like glass shattering and the sound of someone laughing. You walk in the entrance to find the 
    floor littered with books and broken wood. One book in particular is unaffected by the dust and drit like the rest of the books and has no splinters near 
    it. Lixiss approaches the book, inspecting its rich dark cover emblazoned with Emeralds. She closes her eyes, sighs, and mumbles one word, "Abyssal". 
    
    Type A to continue
    '''
            elif word in ('mountains', 'Mountains', 'Kragnammer', 'kraghammer'):
                area = 'mountain'
                mountain = 1
                print '''
    You travel to the mountains and find a Crypt near the entrance to Kraghammer. Curious as to what the mission is, the party enters and are attacked by 3 
    Skeletons.
    
    Type A to initiate combat with Skeletons.
    '''
            elif word in ('Kings Landing', 'kings landing', 'castle', 'Castle'):
                area = 'castle'
                castle = 1
                print '''
    You visit the king. He has no idea who you are. Try again.
    
    Type A to regret your decision.
    '''

            else:
                print "I don't understand %s" %word

def combat(ins_enemy):
    global goblin1
    global goblin2
    global goblin3
    global Troll
    global goblin1_health
    global goblin2_health
    global goblin3_health
    global skeleton1_health
    global skeleton2_health
    global skeleton3_health
    global troll_health
    global dragon_health
    global lich_health
    global graz_health
    global menu
    enemy = ins_enemy
    enemy.enemy_active = True
    if enemy.enemy_active == True:
        if character == 'thava':
            menu.append('Attack with Quarterstaff')
            menu.append('Cast Spell')
            menu.append('Use Breath')
        elif character == 'daern':
            menu.append('Attack with Warhammer')
            menu.append('Attack with Light Crossbow')
            menu.append('Cast Spell')
        elif character == 'lixiss':
            menu.append('Attack with Fists')
            menu.append('Attack with Scimitar')
            menu.append('Attack with Longbow')
            menu.append('Attack with Quarterstaff')
            menu.append('Attack with Darts')
        elif character == 'whistler':
            menu.append('Attack with Rapier')
            menu.append('Attack with Dagger')
            menu.append('Cast Spell')
            menu.append('Use Bardic Inspiration')
        if enemy.name == 'Goblin':
            goblin1_health = enemy.hp
            goblin2_health = enemy.hp
            goblin3_health = enemy.hp
            goblin1 = True
            goblin2 = True
            goblin3 = True
            print '''
    There are 3 Goblins here that look very craxed and hungry. They look like they're the source of all the damage to the mansion.
    
    What would you like to do? You can %s
    ''' %menu
            if character == 'thava':
                combat_thava()
            if character == 'daern': 
                combat_daern()
            elif character == 'lixiss': 
                combat_lixiss()
            elif character == 'whistler': 
                combat_whistler()
        elif enemy.name == 'Troll':
            Troll = True
            troll_health = enemy.hp
            print '''
    An angry blood-crazed Troll roars and stares at you with bloodshot lips and blood dripping from its mouth.
    
     What would you like to do? You can %s
     ''' %menu
    
def combat_thava():
    global aoe
    global weapon
    global THP
    global DHP
    global LHP
    global WHP
    global heal
    global spell_dc
    global damage
    global word
    global spells
    global slc
    global sl1
    global sl2
    global sl3
    global bolts
    global inspiration_player
    word = raw_input('')
    if combat == True and character == 'thava':
        if word in ('Attack with Quarterstaff', 'attack with quarterstaff', 'attack', 'Attack', 'quarterstaff', 'Quarterstaff'):
            weapon = 'qs'
            print'''
    You swing your quarterstaff at the enemy.
    '''
            attack = random.randint(1,20)
            if attack == 1:
                print '''
    You miss horribly and drop your quarterstaff, your next turn will be skipped.
    
    Next turn.
    '''
            else:
                attack = attack + 0
                combat_damage()
        elif word in ('Cast spell', 'cast spell', 'Spell', 'spell'):
            print '''
    Type the name of the spell you wish to cast.
    %s
    %s
    %s
    ''' %(slc, sl1, sl2)
            if word in ('friends', 'Friends'):
                print '''
    You cast Friends. Your face now looks like it has makeup on. You wasted your attack.
    
    Next turn.
    '''
            elif word in ('Chill Touch', 'chill touch'):
                weapon = 'ct'
                print '''
    You cast Chill Touch at the enemy.
    '''
                attack = random.rand.int(1,20)
                if attack == 1:
                    print '''
    Your spell backfires and numbs your hand. Your next turn will be skipped.
    
    Next turn.
    '''
                else:
                    attack = attack + 4
                    combat_damage()
            elif word in ('prestidigitation', 'Prestidigitiation'):
                print '''
    You cast Prestidigitation. Your clothes are now less dusty. You have wasted your attack.
    
    Next turn.
    '''
            elif word in ('Eldritch Blast', 'eldritch blast'):
                weapon = 'eb'
                print '''
    You cast Eldritch Blast at the enemy.
    '''
                attack = random.rand.int(1,20)
                if attack == 1:
                    print '''
    Your spell backfires and you dislocate your wrist. Your next turn will be skipped.
    '''
                else:
                    attack = attack + 4
                    combat_damage()
            elif word in ('vicious mockery', 'Vicious Mockery'):
                weapon = 'vm'
                print '''
    You cast Vicious Mockery at the enemy.
    '''
                spell_dc = 12
                combat_damage()
            elif word in ('cure wounds', 'Cure Wounds') and spells >=1:
                spells = spells - 1
                print '''
    You use a spell slot to cast cure wounds. Who would you like to heal?
    
    Type Thava, Daern, Lixiss, or Whistler. You have %s spell slots left.
    ''' %spells
                if word in ('Thava', 'thava'):
                    heal = random.randint(1,8) + 2
                    THP = heal + THP
                    print '''
    You heal yourself for %s points.
    
    Next turn.
    ''' %heal
                if word in ('Daern', 'daern'):
                    heal = random.randint(1,8) + 2
                    DHP = heal + DHP
                    print '''
    You heal Daern for %s points.
    
    Next turn.
    ''' %heal
                if word in ('Lixiss', 'lixiss'):
                    heal = random.randint(1,8) + 2
                    LHP = heal + LHP
                    print '''
    You heal Lixiss for %s points.
    
    Next turn.
    ''' %heal
                if word in ('Whistler', 'whistler'):
                    heal = random.randint(1,8) + 2
                    WHP = heal + WHP
                    print '''
    You heal Whistler for %s points.
    
    Next turn.
    ''' %heal
            elif word in ('Burning Hands','burning hands'):
                aoe = True
                weapon = 'bh'
                print '''
    You invoke the power of the Fiend to cast Burning Hands.
    '''
            elif word in ('command', 'Command'):
                spells = spells - 1
                print '''
    You try to command any of the Goblins, but their earwax is too dense and your voice isn't high enough to get through. You wasted a spell slot.
    
    Next turn. You have %s spells left.
    ''' %spells
            elif word in ('Unseen Servant', 'unseen servant') and spells >=1:
                spells = spells - 1
                print '''
    You use a spell slot to call your ghost butler, he promptly tells you that dinner isn't ready yet and dissipates into the air. You wasted a spell slot.
    
    Next turn. You have %s spells left.
    ''' %spells
            elif word in('arms of hadar', 'Arms of Hadar') and spells >=1:
                weapon = 'aoh'
                spells = spells - 1
                print '''
    Finally you cast the cool spell, Arms of Hadar. Dark aetheral evil tendrils come up from your shadow attacking the enemies.
    
    You have %s spells left
    ''' %spells
            elif word in sl2:
                print '''
    No second level spells, under construction, come back later.
    '''
     
def combat_daern():
    global aoe
    global weapon
    global THP
    global DHP
    global LHP
    global WHP
    global heal
    global spell_dc
    global damage
    global word
    global spells1
    global spells2
    global spells3
    global slc
    global sl1
    global sl2
    global sl3
    global bolts
    global inspiration_player
    if word in ('Attack with Warhammer', 'attack with warhammer', 'attatck', 'Attack', 'warhammer', 'Warhammer'):
        weapon = 'qs'
        print'''
    You swing your quarterstaff at the enemy.
    '''
        attack = random.randint(1,20)
        if attack == 1:
            print '''
    You miss horribly and drop your quarterstaff, your next turn will be skipped.
    
    Next turn.
    '''
        else:
            attack = attack + 0
            combat_damage()
    if word in ('Attack with Crossbow', 'attack with crossbow', 'crossbow', 'Crossbow'):
        weapon = 'cb'
        bolts = bolts - 1
        print '''
    You take aim at the enemy with your crossbow. You have %s bolts left.
    ''' %bolts
        attack = random.randint(1,20)
        if attack == 1:
            print '''
    Your crossbow jams and you can't get the bolt out, your next turn will be skipped.
    '''
        else:
            attack = attack + 1
    elif word in ('Cast spell', 'cast spell', 'Spell', 'spell'):
        print '''
    Type the name of the spell you wish to cast.
    %s
    %s
    %s
    %s
    ''' %(slc, sl1, sl2, sl3)
        if word in ('light', 'Light'):
            print '''
    You cast Light. Your hand now looks like it went through the sun but kept all the light. You wasted your attack.
    
    Next turn.
    '''
        elif word in ('Spare the Dead', 'Spare the Dead'):
            weapon = 'ct'
            print '''
    You cast Chill Touch at the enemy.
    '''
            attack = random.rand.int(1,20)
            if attack == 1:
                print '''
    Your spell backfires and numbs your hand. Your next turn will be skipped.
    
    Next turn.
    '''
            else:
                attack = attack + 4
                combat_damage()
        elif word in ('prestidigitation', 'Prestidigitiation'):
            print '''
    You cast Prestidigitation. Your clothes are now less dusty. You have wasted your attack.
    
    Next turn.
    '''
        elif word in ('Eldritch Blast', 'eldritch blast'):
            weapon = 'eb'
            print '''
    You cast Eldritch Blast at the enemy.
    '''
            attack = random.rand.int(1,20)
            if attack == 1:
                print '''
    Your spell backfires and you dislocate your wrist. Your next turn will be skipped.
    '''
            else:
                attack = attack + 4
                combat_damage()
        elif word in ('vicious mockery', 'Vicious Mockery'):
            weapon = 'vm'
            print '''
    You cast Vicious Mockery at the enemy.
    '''
            spell_dc = 12
            combat_damage()
        elif word in ('cure wounds', 'Cure Wounds') and spells >=1:
            spells1 = spells1 - 1
            print '''
    You use a spell slot to cast cure wounds. Who would you like to heal?
    
    Type Thava, Daern, Lixiss, or Whistler. You have %s spell slots left.
    ''' %spells
            if word in ('Thava', 'thava'):
                heal = random.randint(1,8) + 2
                THP = heal + THP
                print '''
    You heal yourself for %s points.
    
    Next turn.
    ''' %heal
            if word in ('Daern', 'daern'):
                heal = random.randint(1,8) + 2
                DHP = heal + DHP
                print '''
    You heal Daern for %s points.
    
    Next turn.
    ''' %heal
            if word in ('Lixiss', 'lixiss'):
                heal = random.randint(1,8) + 2
                LHP = heal + LHP
                print '''
    You heal Lixiss for %s points.
    
    Next turn.
    ''' %heal
            if word in ('Whistler', 'whistler'):
                heal = random.randint(1,8) + 2
                WHP = heal + WHP
                print '''
    You heal Whistler for %s points.
    
    Next turn.
    ''' %heal
        elif word in ('Burning Hands','burning hands'):
            aoe = True
            weapon = 'bh'
            print '''
    You invoke the power of the Fiend to cast Burning Hands.
    '''
        elif word in ('command', 'Command'):
            spells1 = spells1 - 1
            print '''
    You try to command any of the Goblins, but their earwax is too dense and your voice isn't high enough to get through. You wasted a spell slot.
    
    Next turn. You have %s spells left.
    ''' %spells
        elif word in ('Unseen Servant', 'unseen servant') and spells >=1:
            spells1 = spells1 - 1
            print '''
    You use a spell slot to call your ghost butler, he promptly tells you that dinner isn't ready yet and dissipates into the air. You wasted a spell slot.
    
    Next turn. You have %s spells left.
    ''' %spells
        elif word in('arms of hadar', 'Arms of Hadar') and spells >=1:
            weapon = 'aoh'
            spells1 = spells1 - 1
            print '''
    Finally you cast the cool spell, Arms of Hadar. Dark aetheral evil tendrils come up from your shadow attacking the enemies.
    
    You have %s spells left
    ''' %spells
        elif word in sl2:
            print '''
    No second level spells, under construction, come back later.
    '''
        elif word in sl3:
            print '''
    Please no, too op. In the process of huge nerf. Come back later.
    '''

def combat_lixiss():
    global damage
    global word
    global darts
    global arrows
    global ki
    global inspiration_player

def combat_whistler():
    global damage
    global word
    global spells1
    global spells2
    global slc
    global sl1
    global sl2
    global inspiration

def combat_damage():
    global word
    global damage
    global enemy_save
    global goblin1
    global goblin2
    global goblin3
    global goblin1_health
    global goblin2_health
    global goblin3_health
    global troll_health
    global skeleton1
    global skeleton2
    global skeleton3
    global skeleton1_health
    global skeleton2_health
    global skeleton3_health
    if enemy.name == 'Skeleton' and enemy.enemy_active == True:
        if skeleton1 == False and skeleton2 == False and skeleton3 == False:
            word = 'end'
            print'''
    You defeated all the skeletons, you hear a faint trumpet doot and silence. Congratulations on beating the medium level combat, uhh there may be more story, 
    you don't know.
    '''
        if weapon == 'aoh':
            damage = random.randint(3,18) + 4
            print '''
    The skeletons scream in agony as they all get dragged into the abyss. All of the skeletons are gone.
    '''
            if skeleton1 == True:
                skeleton1_health = skeleton1_health - damage
            if skeleton2 == True:
                skeleton2_health = skeleton2_health - damage
            if skeleton3 == True:
                skeleton3_health = skeleton3_health - damage
        elif aoe == True:
            if weapon == 'bh':
                enemy_save = random.randint(1,20)
                if enemy_save == 20:
                    print '''
    These skeletons just looked like they walked through hell and back and are ready to kill. The fire didn't effect them at all.
    
    Next Turn.
    '''
                elif 12 < enemy_save < 20:
                    damage = random.randint(1,9) + 4
                    print '''
    The skeletons scream in pain for a second, but then realizes that the fire was only on their hands. They each take %s damage.
    
    Next Turn.
    ''' %damage
                    if skeleton1 == True:
                        skeleton1_health = skeleton1_health - damage
                    if skeleton2 == True:
                        skeleton2_health = skeleton2_health - damage
                    if skeleton3 == True:
                        skeleton3_health = skeleton3_health - damage
                elif 1 < enemy_save < 12:
                    damage = random.randint(3,18) + 4
                    print '''
    The skeletons are engulfed in flames, screaming their heads off. They each take %s points of damage.
    ''' %damage
                    if skeleton1 == True:
                        skeleton1_health = skeleton1_health - damage
                    if skeleton2 == True:
                        skeleton2_health = skeleton2_health - damage
                    if skeleton3 == True:
                        skeleton3_health = skeleton3_health - damage
        elif aoe == False:
            if enemies > 1 and skeleton1 == True and skeleton2 == True and skeleton3 == True:
                print '''
    Which enemy would you like to attack, skeleton 1, skeleton 2, or skeleton 3?
    '''
            elif enemies > 1 and skeleton1 == True and skeleton2 == True and skeleton3 == False:
                print '''
    Which enemy would you like to attack, skeleton 1, or skeleton 2?
    '''
            elif enemies > 1 and skeleton1 == True and skeleton2 == False and skeleton3 == True:
                print '''
    Which enemy would you like to attack, skeleton 1, or skeleton 3?
    '''
            elif enemies > 1 and skeleton1 == False and skeleton2 == True and skeleton3 == True:
                print '''
    Which enemy would you like to attack, skeleton 1, or skeleton 3?
    '''
                if word in ('skeleton 1', 'skeleton 1') or skeleton1 == True and skeleton2 == False and skeleton3 == False:
                    if weapon == 'vm':
                        enemy_save = random.randint(1,20)
                        if enemy_save == 20:
                            print '''
    You tell the skeleton his mother is ugly. The skeleton, however, takes pride in that fact.
    
    Next Turn.
    '''
                        elif 12 < enemy_save < 20:
                            print '''
    You make a very witty remark that you think will work, but the skeleton isn't smart enough to understand it.
    
    Next Turn.
    '''
                        elif 1 < enemy_save < 12:
                            if character =='thava':
                                damage = random.randint(1,4) + 4
                            elif character == 'whistler':
                                damage = random.randint(1,4) + 6
                                print '''
    You call the skeleton a big dumb dummy. You really hurt his feelings with this one, dealing %s points of damage.
    ''' %damage
                    if attack >= 13:
                        if weapon == 'eb':
                            damage = random.randint(1,10) + 4
                            print '''
    You hit skeleton 1 for %s damage. Nice!
    
    Next turn.
    ''' %damage
                        skeleton1_health = skeleton1_health - damage
                        if skeleton1_health <= 0:
                            skeleton1 = False
                            print '''
    You defeated skeleton 1.
    '''
                        elif weapon == 'qs':
                            damage = random.randint(1,8) + 0
                            print '''
    You hit skeleton 1 for %s damage. Nice!
    
    Next turn.
    ''' %damage
                            skeleton1_health = skeleton1_health - damage
                            if skeleton1_health <= 0:
                                skeleton1 = False
                                print '''
    You defeated skeleton 1.
    '''
                        elif weapon == 'ct':
                                damage = random.randint(2,16) + 4
                                print '''
    You hit skeleton 1 for %s damage. Nice!
    
    Next turn.
    ''' %damage
                                skeleton1_health = skeleton1_health - damage
                                if skeleton1_health <= 0:
                                    skeleton1 = False
                                    print '''
    You defeated skeleton 1.
    '''
                    elif 1 < attack < 13:
                        if weapon == 'qs':
                            print '''
    You miss the skeleton. Your aim could use a little work.
    
    Next turn.
    '''
                        elif weapon == 'ct':
                            print '''
    You miss the skeleton. You should work on your spectral hand-eye coordination.
    
    Next turn.
    '''
                        elif weapon == 'eb':
                            print '''
    You miss the skeleton. You shoot magical force spears like you're a 300,927 year old.
    
    Next turn.
    '''
                if word in ('skeleton 2', 'skeleton 2') or skeleton1 == False and skeleton2 == True and skeleton3 == False:
                    if weapon == 'vm':
                        enemy_save = random.randint(1,20)
                    if enemy_save == 20:
                        print '''
    You tell the skeleton his mother is ugly. The skeleton, however, takes pride in that fact.
    
    Next Turn.
    '''
                    elif 12 < enemy_save < 20:
                        print '''
    You make a very witty remark that you think will work, but the skeleton isn't smart enough to understand it.
    
    Next Turn.
    '''
                    elif 1 < enemy_save < 12:
                        if character =='thava':
                            damage = random.randint(1,4) + 4
                        elif character == 'whistler':
                            damage = random.randint(1,4) + 6
                        print '''
    You call the skeleton a big dumb dummy. You really hurt his feelings with this one, dealing %s points of damage.
    ''' %damage
                    if attack >= 13:
                        if weapon == 'eb':
                            damage = random.randint(1,10) + 4
                            print '''
    You hit skeleton 2 for %s damage. Nice!
    
    Next turn.
    ''' %damage
                            skeleton2_health = skeleton2_health - damage
                            if skeleton2_health <= 0:
                                skeleton2 = False
                                print '''
    You defeated skeleton 2
    '''
                        elif weapon == 'qs':
                            damage = random.randint(1,8) + 0
                            print '''
    You hit skeleton 2 for %s damage. Nice!
    
    Next turn.
    ''' %damage
                            skeleton2_health = skeleton2_health - damage
                            if skeleton1_health <= 0:
                                skeleton1 = False
                                print '''
    You defeated skeleton 2.
    '''
                        elif weapon == 'ct':
                            damage = random.randint(2,16) + 4
                            print '''
    You hit skeleton 2 for %s damage. Nice!
    
    Next turn.
    ''' %damage
                            skeleton2_health = skeleton2_health - damage
                            if skeleton1_health <= 0:
                                skeleton1 = False
                                print '''
    You defeated skeleton 2.
    '''
                    elif 1 < attack < 13:
                        if weapon == 'qs':
                            print '''
    You miss the skeleton. Your aim could use a little work.
    
    Next turn.
    '''
                        elif weapon == 'ct':
                            print '''
    You miss the skeleton. You should work on your spectral hand-eye coordination.
    
    Next turn.
    '''
                        elif weapon == 'eb':
                            print '''
    You miss the skeleton. You shoot magical force spears like you're a 300,927 year old.
    
    Next turn.
    '''
                    if word in ('skeleton 3', 'skeleton 3') or skeleton1 == False and skeleton2 == False and skeleton3 == True:
                        if weapon == 'vm':
                            enemy_save = random.randint(1,20)
                            if enemy_save == 20:
                                print '''
    You tell the skeleton his mother is ugly. The skeleton, however, takes pride in that fact.
    
    Next Turn.
    '''
                            elif 12 < enemy_save < 20:
                                print '''
    You make a very witty remark that you think will work, but the skeleton isn't smart enough to understand it.
    
    Next Turn.
    '''
                            elif 1 < enemy_save < 12:
                                if character =='thava':
                                    damage = random.randint(1,4) + 4
                                elif character == 'whistler':
                                    damage = random.randint(1,4) + 6
                                print '''
    You call the skeleton a big dumb dummy. You really hurt his feelings with this one, dealing %s points of damage.
    ''' %damage
                        if attack >= 13:
                            if weapon == 'eb':
                                damage = random.randint(1,10) + 4
                                print '''
    You hit skeleton 3 for %s damage. Nice!
    
    Next turn.
    ''' %damage
                                skeleton3_health = skeleton3_health - damage
                                if skeleton3_health <= 0:
                                    skeleton3 = False
                                    print '''
    You defeated skeleton 3
    '''
                            elif weapon == 'qs':
                                damage = random.randint(1,8) + 0
                                print '''
    You hit skeleton 3 for %s damage. Nice!
    
    Next turn.
    ''' %damage
                                skeleton3_health = skeleton3_health - damage
                                if skeleton1_health <= 0:
                                    skeleton1 = False
                                    print '''
    You defeated skeleton 3.
    '''
                            elif weapon == 'ct':
                                damage = random.randint(2,16) + 4
                                print '''
    You hit skeleton 3 for %s damage. Nice!
    
    Next turn.
    ''' %damage
                                skeleton3_health = skeleton3_health - damage
                                if skeleton1_health <= 0:
                                    skeleton1 = False
                                    print '''
    You defeated skeleton 3.
    '''
                    elif 1 < attack < 13:
                        if weapon == 'qs':
                            print '''
    You miss the skeleton. Your aim could use a little work.
    
    Next turn.
    '''
                        elif weapon == 'ct':
                            print '''
    You miss the skeleton. You should work on your spectral hand-eye coordination.
    
    Next turn.
    '''
                        elif weapon == 'eb':
                            print '''
    You miss the skeleton. You shoot magical force spears like you're a 300,927 year old.
    
    Next turn.
    '''
    if enemy.name == 'Troll':
        if troll_health <= 0:
            print '''
    You pressed the win button. The game is over now. Good job. Congratulations. There is no alternate endings. Everything leading up to this was a joke and 
    none of this matters. The story totally doesn't continue if you choose a different destinaiton. Nope. I'm done now. I'm going on my lunch break. 
    See you never.
    '''
            word = 'end'
        if weapon == 'aoh':
            damage = random.randint(3,18) + 4
            print '''
    The Troll scream in agony as they all get dragged into the abyss. All of the Troll are gone.
    '''
            troll_health = troll_health - damage
            
        elif aoe == True:
            if weapon == 'bh':
                enemy_save = random.randint(1,20)
                if enemy_save == 20:
                    print '''
    The Troll literally eats the fire like it's a sandwitch. He sure has one iron gut.
    
    Next Turn.
    '''
                elif 12 < enemy_save < 20:
                    damage = random.randint(1,9) + 4
                    print '''
    The Troll screams in pain for a second, but then realizes that the fire was only on his hands. He takes %s damage.
    
    Next Turn.
    ''' %damage
                    troll_health = troll_health - damage
                elif 1 < enemy_save < 12:
                    damage = random.randint(3,18) + 4
                    print '''
    The Troll is engulfed in flames, screaming their heads off. He takes %s damage.
    ''' %damage
                    troll_health = troll_health - damage
        elif aoe == False:
            
                    if weapon == 'vm':
                        enemy_save = random.randint(1,20)
                        if enemy_save == 20:
                            print '''
    You tell the Troll his mother is ugly. The goblin, however, takes pride in that fact.
    
    Next Turn.
    '''
                        elif 12 < enemy_save < 20:
                            print '''
    You make a very witty remark that you think will work, but the Troll isn't smart enough to understand it.
    
    Next Turn.
    '''
                        elif 1 < enemy_save < 12:
                            if character =='thava':
                                damage = random.randint(1,4) + 4
                            elif character == 'whistler':
                                damage = random.randint(1,4) + 6
                                print '''
    You call the Troll a big dumb dummy. You really hurt his feelings with this one, dealing %s points of damage.
    ''' %damage
                    if attack >= 13:
                        if weapon == 'eb':
                            damage = random.randint(1,10) + 4
                            print '''
    You hit the Troll for %s damage. Nice!
    
    Next turn.
    ''' %damage
                            troll_health = troll_health - damage
                        elif weapon == 'qs':
                            damage = random.randint(1,8) + 0
                            print '''
    You hit the Troll for %s damage. Nice!
    
    Next turn.
    ''' %damage
                            goblin1_health = goblin1_health - damage
                        elif weapon == 'ct':
                                damage = random.randint(2,16) + 4
                                print '''
    You hit the Troll for %s damage. Nice!
    
    Next turn.
    ''' %damage
                    elif 1 < attack < 13:
                        if weapon == 'qs':
                            print '''
    You miss the Troll. Your aim could use a little work.
    
    Next turn.
    '''
                        elif weapon == 'ct':
                            print '''
    You miss the Troll. You should work on your spectral hand-eye coordination.
    
    Next turn.
    '''
                        elif weapon == 'eb':
                            print '''
    You miss the Troll. You shoot magical force spears like you're a 300,927 year old.
    
    Next turn.
    '''
    if enemy.name == 'Goblin':
        if goblin1 == False and goblin2 == False and goblin3 == False:
            print'''
    You defeated all the Goblins, but there's still a noise coming from down here in the basement.
    '''
        if weapon == 'aoh':
            damage = random.randint(3,18) + 4
            print '''
    The goblins scream in agony as they all get dragged into the abyss. All of the goblins are gone.
    '''
            if goblin1 == True:
                goblin1_health = goblin1_health - damage
            if goblin2 == True:
                goblin2_health = goblin2_health - damage
            if goblin3 == True:
                goblin3_health = goblin3_health - damage
            if goblin1 == False and goblin2 == False and goblin3 == False:
                print'''
    You pressed the win button. Congratulations, you have beaten the game. All of this lead up to some goblins in a mansion. Nothing more to see here, no 
    alternate endings. Nope. The game is done now. Hope you had fun. Bye. I'm gonna go get lunch now, see you never.
    '''
        elif aoe == True:
            if weapon == 'bh':
                enemy_save = random.randint(1,20)
                if enemy_save == 20:
                    print '''
    These Goblins just looked like they walked through hell and back and are ready to kill. The fire didn't effect them at all.
    
    Next Turn.
    '''
                elif 12 < enemy_save < 20:
                    damage = random.randint(1,9) + 4
                    print '''
    The Goblins scream in pain for a second, but then realizes that the fire was only on their hands. They each take %s damage.
    
    Next Turn.
    ''' %damage
                    if goblin1 == True:
                        goblin1_health = goblin1_health - damage
                    if goblin2 == True:
                        goblin2_health = goblin2_health - damage
                    if goblin3 == True:
                        goblin3_health = goblin3_health - damage
                elif 1 < enemy_save < 12:
                    damage = random.randint(3,18) + 4
                    print '''
    The Goblins are engulfed in flames, screaming their heads off. They each take %s points of damage.
    ''' %damage
                    if goblin1 == True:
                        goblin1_health = goblin1_health - damage
                    if goblin2 == True:
                        goblin2_health = goblin2_health - damage
                    if goblin3 == True:
                        goblin3_health = goblin3_health - damage
        elif aoe == False:
            if enemies > 1 and goblin1 == True and goblin2 == True and goblin3 == True:
                print '''
    Which enemy would you like to attack, Goblin 1, Goblin 2, or Goblin 3?
    '''
            elif enemies > 1 and goblin1 == True and goblin2 == True and goblin3 == False:
                print '''
    Which enemy would you like to attack, Goblin 1, or Goblin 2?
    '''
            elif enemies > 1 and goblin1 == True and goblin2 == False and goblin3 == True:
                print '''
    Which enemy would you like to attack, Goblin 1, or Goblin 3?
    '''
            elif enemies > 1 and goblin1 == False and goblin2 == True and goblin3 == True:
                print '''
    Which enemy would you like to attack, Goblin 1, or Goblin 3?
    '''
                if word in ('goblin 1', 'Goblin 1') or goblin1 == True and goblin2 == False and goblin3 == False:
                    if weapon == 'vm':
                        enemy_save = random.randint(1,20)
                        if enemy_save == 20:
                            print '''
    You tell the Goblin his mother is ugly. The goblin, however, takes pride in that fact.
    
    Next Turn.
    '''
                        elif 12 < enemy_save < 20:
                            print '''
    You make a very witty remark that you think will work, but the Goblin isn't smart enough to understand it.
    
    Next Turn.
    '''
                        elif 1 < enemy_save < 12:
                            if character =='thava':
                                damage = random.randint(1,4) + 4
                            elif character == 'whistler':
                                damage = random.randint(1,4) + 6
                                print '''
    You call the goblin a big dumb dummy. You really hurt his feelings with this one, dealing %s points of damage.
    ''' %damage
                    if attack >= 13:
                        if weapon == 'eb':
                            damage = random.randint(1,10) + 4
                            print '''
    You hit Goblin 1 for %s damage. Nice!
    
    Next turn.
    ''' %damage
                        goblin1_health = goblin1_health - damage
                        if goblin1_health <= 0:
                            goblin1 = False
                            print '''
    You defeated Goblin 1.
    '''
                        elif weapon == 'qs':
                            damage = random.randint(1,8) + 0
                            print '''
    You hit Goblin 1 for %s damage. Nice!
    
    Next turn.
    ''' %damage
                            goblin1_health = goblin1_health - damage
                            if goblin1_health <= 0:
                                goblin1 = False
                                print '''
    You defeated Goblin 1.
    '''
                        elif weapon == 'ct':
                                damage = random.randint(2,16) + 4
                                print '''
    You hit Goblin 1 for %s damage. Nice!
    
    Next turn.
    ''' %damage
                                goblin1_health = goblin1_health - damage
                                if goblin1_health <= 0:
                                    goblin1 = False
                                    print '''
    You defeated Goblin 1.
    '''
                    elif 1 < attack < 13:
                        if weapon == 'qs':
                            print '''
    You miss the Goblin. Your aim could use a little work.
    
    Next turn.
    '''
                        elif weapon == 'ct':
                            print '''
    You miss the Goblin. You should work on your spectral hand-eye coordination.
    
    Next turn.
    '''
                        elif weapon == 'eb':
                            print '''
    You miss the Goblin. You shoot magical force spears like you're a 300,927 year old.
    
    Next turn.
    '''
                if word in ('goblin 2', 'Goblin 2') or goblin1 == False and goblin2 == True and goblin3 == False:
                    if weapon == 'vm':
                        enemy_save = random.randint(1,20)
                    if enemy_save == 20:
                        print '''
    You tell the Goblin his mother is ugly. The goblin, however, takes pride in that fact.
    
    Next Turn.
    '''
                    elif 12 < enemy_save < 20:
                        print '''
    You make a very witty remark that you think will work, but the Goblin isn't smart enough to understand it.
    
    Next Turn.
    '''
                    elif 1 < enemy_save < 12:
                        if character =='thava':
                            damage = random.randint(1,4) + 4
                        elif character == 'whistler':
                            damage = random.randint(1,4) + 6
                        print '''
    You call the goblin a big dumb dummy. You really hurt his feelings with this one, dealing %s points of damage.
    ''' %damage
                    if attack >= 13:
                        if weapon == 'eb':
                            damage = random.randint(1,10) + 4
                            print '''
    You hit Goblin 2 for %s damage. Nice!
    
    Next turn.
    ''' %damage
                            goblin2_health = goblin2_health - damage
                            if goblin2_health <= 0:
                                goblin2 = False
                                print '''
    You defeated Goblin 2
    '''
                        elif weapon == 'qs':
                            damage = random.randint(1,8) + 0
                            print '''
    You hit Goblin 2 for %s damage. Nice!
    
    Next turn.
    ''' %damage
                            goblin2_health = goblin2_health - damage
                            if goblin1_health <= 0:
                                goblin1 = False
                                print '''
    You defeated Goblin 2.
    '''
                        elif weapon == 'ct':
                            damage = random.randint(2,16) + 4
                            print '''
    You hit Goblin 2 for %s damage. Nice!
    
    Next turn.
    ''' %damage
                            goblin2_health = goblin2_health - damage
                            if goblin1_health <= 0:
                                goblin1 = False
                                print '''
    You defeated Goblin 2.
    '''
                    elif 1 < attack < 13:
                        if weapon == 'qs':
                            print '''
    You miss the Goblin. Your aim could use a little work.
    
    Next turn.
    '''
                        elif weapon == 'ct':
                            print '''
    You miss the Goblin. You should work on your spectral hand-eye coordination.
    
    Next turn.
    '''
                        elif weapon == 'eb':
                            print '''
    You miss the Goblin. You shoot magical force spears like you're a 300,927 year old.
    
    Next turn.
    '''
                    if word in ('goblin 3', 'Goblin 3') or goblin1 == False and goblin2 == False and goblin3 == True:
                        if weapon == 'vm':
                            enemy_save = random.randint(1,20)
                            if enemy_save == 20:
                                print '''
    You tell the Goblin his mother is ugly. The goblin, however, takes pride in that fact.
    
    Next Turn.
    '''
                            elif 12 < enemy_save < 20:
                                print '''
    You make a very witty remark that you think will work, but the Goblin isn't smart enough to understand it.
    
    Next Turn.
    '''
                            elif 1 < enemy_save < 12:
                                if character =='thava':
                                    damage = random.randint(1,4) + 4
                                elif character == 'whistler':
                                    damage = random.randint(1,4) + 6
                                print '''
    You call the goblin a big dumb dummy. You really hurt his feelings with this one, dealing %s points of damage.
    ''' %damage
                        if attack >= 13:
                            if weapon == 'eb':
                                damage = random.randint(1,10) + 4
                                print '''
    You hit Goblin 3 for %s damage. Nice!
    
    Next turn.
    ''' %damage
                                goblin3_health = goblin3_health - damage
                                if goblin3_health <= 0:
                                    goblin3 = False
                                    print '''
    You defeated Goblin 3
    '''
                            elif weapon == 'qs':
                                damage = random.randint(1,8) + 0
                                print '''
    You hit Goblin 3 for %s damage. Nice!
    
    Next turn.
    ''' %damage
                                goblin3_health = goblin3_health - damage
                                if goblin1_health <= 0:
                                    goblin1 = False
                                    print '''
    You defeated Goblin 3.
    '''
                            elif weapon == 'ct':
                                damage = random.randint(2,16) + 4
                                print '''
    You hit Goblin 3 for %s damage. Nice!
    
    Next turn.
    ''' %damage
                                goblin3_health = goblin3_health - damage
                                if goblin1_health <= 0:
                                    goblin1 = False
                                    print '''
    You defeated Goblin 3.
    '''
                    elif 1 < attack < 13:
                        if weapon == 'qs':
                            print '''
    You miss the Goblin. Your aim could use a little work.
    
    Next turn.
    '''
                        elif weapon == 'ct':
                            print '''
    You miss the Goblin. You should work on your spectral hand-eye coordination.
    
    Next turn.
    '''
                        elif weapon == 'eb':
                            print '''
    You miss the Goblin. You shoot magical force spears like you're a 300,927 year old.
    
    Next turn.
    '''

                

def character_info():
    global character
    global character_info
    if character_info == True:
        if character == 'thava':
            print '''
    Thava Alviir is a Warlock that draws her magic from her patron, The Fiend. 
    Her stats are as follows:
        Armor Class: 10
        Strength: 8
        Dexterity: 11
        Constitution: 13
        Wisdom: 16
        Intelligence: 16
        Charisma: 12
        
        To finish, type A.
        To read Spell information, type Spells.
    '''
        if character == 'daern':
            print '''
    Daern Frostbeard is a Cleric of the War Domain, who draws his magic from Ilmater, God of Endurance.
    His stats are as follows:
        Armor Class: 16
        Strength: 16
        Dexterity: 12
        Constitution: 16
        Wisdom: 12
        Intelligence: 18
        Charisma: 12
        
        To finish, type A.
        To read Spell information, type Spells.
    '''
        if character == 'lixiss':
            print '''
    Lixiss Sylphine is a Monk that trained inn the Way of the Kensei, she sees her weapon in the same way a calligrapher or painter regards a pen or brush.
    Her stats are as follows:
        Armor Class: 17
        Strength: 18
        Dexterity: 20
        Constitution: 12
        Wisdom: 12
        Intelligence: 10
        Charisma: 12
        
        To finish, type A.
    '''
        if character == 'whistler':
            print '''
    Whistler is a Bard from the College of Whispers.
    His stats are as follows:
        Armor Class: 15
        Strength: 8
        Dexterity: 14
        Constitution: 10
        Wisdom: 13
        Intelligence: 9
        Charisma: 18
        
        To finish, type A.
        To read Spell information, type Spells.
    '''

    
def description():
    global info
    if character == 'thava':
        print '''
    Cantrips:
        Friends
        Chill Touch
        Prestidigitation
        Eldritch Blast
        Vicious Mockery
    First Level Spells:
        Burning Hands
        Command
        Cure Wounds
        Unseen Servent
        Arms of Hadar
        Hellish Rebuke
        Protection From Evil
    Second Level Spells:
         Blindness/Deafness
         Scorching Ray
         Shadow Blade
    Abilities:
        Cold Breath
        Dark One's Blessing
         
    To finish, type A.
    For more information on a specific spell or ability, type the name.
    '''
        info = True
    if character == 'daern':
        print '''
    Cantrips:
        Light
        Spare the Dead
        Sacred Flame
        Thaumaturgy
        Message
        Eldrich Blast
    First Level Spells:
        Divine Favor
        Shield of Faith
        Command
        Create/Destroy Water
        Cure Wounds
        Healing Word
        Purify Food and Drink
        Sanctuary
    Second Level Spells:
        Aid
        Poison Protect
        Find Traps
    Third Level Spells:
        Meld into Stone
        revivify
        Animate Dead
    
    To finish, type A.
    For more information on a specific spell or ability, type the name.
    '''
        info = True
    if character == 'lixiss':
        print '''
    Lixiss has no spells.
    Abilities:
        Deflect Missiles
        Patient Defense
        Flurry of Blows
        Agile Parry
        Kensei's Shot
    
   To finish, type A.
   For more information on a specific ability, type the name.
    '''
        info = True
    if character == 'whistler':
        print '''
    Cantrips:
       Vicious Mockery
       Light
       True Strike
    First Level Spells:
        Dissonant Whispers
        Tasha's Hideous Laughter
        Sleep
        Thunderwave
    Second Level Spells:
        Suggestion
        Silence
        Shatter
    Abilities:
        Bardic Inspiration
        Psychic Blades
        
    To finish, type A.
    For more information on a specific spell or ability, type the name.
    '''
        info = True


start_game()