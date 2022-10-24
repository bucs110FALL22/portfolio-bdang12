class Shark:
	def __init__(self):
    self.control=keyboard #Control by keyboard
    self.growth=1*fish #growth in size by 1 for each fish
    self.healthbar=100 #Shark healthbar=100

class Bomb:
	def __init__(self):
    self.speed=1 #bomb start speed=1
    self.speed_incpermin=0.5 #speed increase per minute=0.5
    self.dmg=10 #dmg when hit is 10

class Fish:
	def __init__(self):
    self.point=1  #point when eat =1
    self.speed=0.5 #speed when moving=0.5
    self.health_recovery=5 #health recovery when eat =5