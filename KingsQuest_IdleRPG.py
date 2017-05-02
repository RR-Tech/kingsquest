import random
# RPG Text-Based Game
# Plot:
# The King has assigned you the quest of finding and fighting some of the 
# kingdom's most feared enemies in order to win his respect and become the official Hand of the King.
# The Hand is the King's closest advisor, appointed and authorized to make decisions on behalf 
# of the King's name. 

# Description: Game that simulates x battles between the player and an enemy monster per x levels.
# Each level a random item with random bonus stats is given (HP = health and AT = attack).
# Formula to win : defeat the enemies while keeping oneself alive.
# If all the levels are won - > wins the game -> successfully becomes the Hand of the King
# If not - > loses the game - > loses one's life, failing the quest


# CLASSES----------------------------------------
#Character class
class Character(object):
  _name = ""
  _health = 0
  _attack = 0
  
  def __init__(self, name, health, attack):
        self.set_name(name)
        self.set_health(health)
        self.set_attack(attack)
        
        
  def set_name(self, name):
    self._name = name
    
  def get_name(self):
    return self._name
    
  def set_health(self, health):
    self._health = health
  
  def get_health(self):
    return self._health
    
  def set_attack(self, attack):
    self._attack = attack
    
  def get_attack(self):
    return self._attack
  
  
  def addHP(self, plusHP):
    self._health += plusHP
  
  def removeHP(self, minusHP):
    self._health -= minusHP
    
  def addAT(self, plusAT):
    self._attack += plusAT
  
  def removeAT(self, minusAT):
    self._attack -= minusAT
    

#Items class
class Item(object):
  _name = ""
  _bonusHP = 0
  _bonusAT = 0
  
  def __init__(self, name, bonusHP, bonusAT):
      self.set_name(name)
      self.set_bonusHP(bonusHP)
      self.set_bonusAT(bonusAT)
  
  def set_name(self, name):
    self._name = name
    
  def get_name(self):
    return self._name
      
  def set_bonusHP(self, bonusHP):
    self._bonusHP = bonusHP
  
  def get_bonusHP(self):
    return self._bonusHP
    
  def set_bonusAT(self, bonusAT):
    self._bonusAT = bonusAT
    
  def get_bonusAT(self):
    return self._bonusAT
#-----------------------------------------------


#FUNCTIONS----------------------------------------
# Display the Main Menu
def displayMenu():
  
  print('============================================')
  print('                   Welcome to')
  print('                  KINGs QUEST !')
  print('============================================')
  print(' ')
  

# Create player
def createPlayer():
  global user
  defaultHP = 100
  defaultAT = 50

  username = input('Username: ')
  user = Character(username, defaultHP, defaultAT)


# Display Player Stats 
def displayPlayerStats():
  print ('HP: ' + str(user.get_health()) )
  print ('AT: ' + str(user.get_attack()) )
  print(' ')


# Create Monsters
def createMonsters():
  multipHP = 80
  multipAT = 60
  
  for i in range(nLvls):
    formulaHP = multipHP + ((i+1) * multipHP)
    formulaAT = multipAT + ((i+1) * multipAT)
    monsters.append(Character(MonsterNamesList[i], formulaHP, formulaAT))


# Display Monster stats
def displayMonsterStats(monster):
  print( monster.get_name() + " appears . . .")
  print ('Enemy HP: ' + str(monster.get_health()) )
  print ('Enemy AT: ' + str(monster.get_attack()) )
  print(' ')


# Create Items
def createItems():
  multipBase = 100
  multipBonus = 3
  
  for i in range(nItems):
    limit = multipBase + random.randrange(multipBase*multipBonus)
    statHP = random.randrange(limit)
    statST = random.randrange(limit)
    items.append(Item(ItemNamesList[i], statHP, statST))


# Drop random item
def dropItem():
  #randomize
  randomN = random.randrange(nItems)
  #collect random item data
  itemName = items[randomN].get_name()
  itemHP = items[randomN].get_bonusHP()
  itemAT = items[randomN].get_bonusAT()
  #display findings
  print('Bonus Item Found: ' + itemName + ' HP: +' + str(itemHP) + ' ST: +' + str(itemAT) )
  print(' ')
  #add item stats to player
  user.addHP(itemHP)
  user.addAT(itemAT)


# Display level 
def displayLevel(currentLvl):
  print('--------------------------------------- ')
  print('STATISTICS LVL ' + str(currentLvl+1))
  print(' ')


# Play the level
def playRound(enemy):
  result = None
  
  #while current enemy is alive
  while (enemy.get_health() >= 0):
    print(" ")
    print(" # # BATTLE # # ")
    print(" ")
    #update stats from battle
    user.removeHP(enemy.get_attack())
    enemy.removeHP(user.get_attack())
    #if the player died 
    if (user.get_health() <= 0):
      result = loseLevel()
      break
    
  #if the enemy is dead and the player still alive -> lvl up
  if(result is None): result = winLevel()

  print(" ")
  print('** Player Battle Aftermath ** ')
  displayPlayerStats()
  return result
  

# when a level is lost 
def loseLevel():
  print(" ")
  print('Match Result : LOSE')
  return 0 #lose status


# when a level is won -> level up
def winLevel():
  global nWins
  print(" ")    
  print('Match Result : WIN')
  print('-> Level Up Bonus : +'+ str(lvlUpBonusHP) +'HP ')
  user.addHP(lvlUpBonusHP)
  nWins +=1
  return 1 #win status
  

# Verify if the player won or lost the game
def gameResult():
  if (nWins == nLvls):
    wonMessage()
  else:
    lostMessage()


# WINNER message
def wonMessage():
  print(' ')
  print('=====================================') 
  print('Congrats ' + user.get_name() + ' !')
  print('Max level reached ! ')
  print('You have completed the quest!')
  print('Your rank is now: Hand of the King')
  print('=====================================')

# LOSER message
def lostMessage():
  print(' ')
  print('=====================================') 
  print('Sorry ' + user.get_name() + ', you failed the quest!')
  print('Rounds Won: ' + str(nWins) + '/' + str(nLvls))
  print('Your rank is now: Dead Knight')
  print('=====================================')
#--------------------------------------------------


#CONFIGS---------------------------------------
user = Character("Guest", 0 , 0)
MonsterNamesList = ['Mountain Scorpion',
                  'Giant Octupus',
                  'Terror Dragon',
                  'Chaos Beast',
                  'Grim Reaper',
                 ]
ItemNamesList = ['Dagger of Life',
                  'Sword of Justice',
                  'Shurikens of Darkness',
                  'Knights Key Sword',
                  'Dawn of Potions',
                  'Katana of Thruth',
                  'Kings Armor',
                  'Vest of Life',
                  'Light Crystals',
                  'Old Klain Sabre',
                 ]
nMonsters = len(MonsterNamesList)
nItems = len(ItemNamesList)
lvlUpBonusHP = 100
monsters = []
items = []
nLvls = nMonsters
nWins = 0


#START------------------------------------

displayMenu()
createPlayer()
createMonsters()
createItems()

displayPlayerStats()

for lvl in range(nLvls):
    displayLevel(lvl)
    
    dropItem()
    
    displayPlayerStats()
    
    displayMonsterStats(monsters[lvl])
    
    roundResult = playRound(monsters[lvl])
    
    if roundResult == 0: break;
    
gameResult()

#END--------------------------------------

#Stay tuned for King's Quest II.
    
    
    

