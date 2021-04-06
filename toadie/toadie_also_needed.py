'''
class Log1:
	def __init__(self):
		self.touchable = True
		self.file = pygame.image.load('Toadie-Media/images/log.png').convert_alpha()

class Log3:
	def __init__(self):
		self.touchable = True
		self.file = pygame.image.load('Toadie-Media/images/log3.png').convert_alpha()

class Turtle2:
	def __init__(self):
		self.touchable = True
		self.file = pygame.image.load('Toadie-Media/images/turtle2.png').convert_alpha()

class Turtle3:
	def __init__(self):
		self.touchable = True
		self.file = pygame.image.load('Toadie-Media/images/turtle3.png').convert_alpha()

class Truck:
	def __init__(self):
		self.touchable = True
		self.file = pygame.image.load('Toadie-Media/images/truck.png').convert_alpha()

class Car_Pink:
	def __init__(self):
		self.touchable = True
		self.file = pygame.image.load('Toadie-Media/images/car_pink.png').convert_alpha()

class Car_Purple:
	def __init__(self):
		self.touchable = True
		self.file = pygame.image.load('Toadie-Media/images/car_purple.png').convert_alpha()

class Digger:
	def __init__(self):
		self.touchable = True
		self.file = pygame.image.load('Toadie-Media/images/digger.png').convert_alpha()

class Car_Red:
	def __init__(self):
		self.touchable = True
		self.file = pygame.image.load('Toadie-Media/images/car_red.png').convert_alpha()


'''








	#screen.blit(log2.file,(log2x,log2.y))


	# testing size
'''
	turtle2 = Turtle2()
	screen.blit(turtle2.file,(0,101))

	log3 = Log3()
	screen.blit(log3.file,(0,134))

	log1 = Log1()
	screen.blit(log1.file,(0,166))

	turtle3 = Turtle3()
	screen.blit(turtle3.file,(0,197))

	truck = Truck()
	screen.blit(truck.file,(0,262))

	car_pink = Car_Pink()
	screen.blit(car_pink.file,(0,290))

	car_purple = Car_Purple()
	screen.blit(car_purple.file,(0,324))

	digger = Digger()
	screen.blit(digger.file,(0,356))

	car_red = Car_Red()
	screen.blit(car_red.file,(0,386))
'''