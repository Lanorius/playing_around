import pygame, random, sys

#objects
class Pad:
	def __init__(self):
		self.touchable = True
		self.file = pygame.image.load('Toadie-Media/images/pad.png').convert()

class Pavement:
	def __init__(self):
		self.touchable = True
		self.file = pygame.image.load('Toadie-Media/images/pavement.png').convert_alpha()

class Log2:
	def __init__(self, x):
		self.x = x
		self.y = 70
		self.file = pygame.image.load('Toadie-Media/images/log2.png').convert_alpha()
		self.surface = self.file.get_rect(midtop = (self.x,self.y))

class Turtle2:
	def __init__(self, x):
		self.x = x
		self.y = 101
		self.file = pygame.image.load('Toadie-Media/images/turtle2.png').convert_alpha()
		self.surface = self.file.get_rect(midtop = (self.x,self.y))

class Log3:
	def __init__(self, x):
		self.x = x
		self.y = 134
		self.file = pygame.image.load('Toadie-Media/images/Log3.png').convert_alpha()
		self.surface = self.file.get_rect(midtop = (self.x,self.y))

class Log1:
	def __init__(self, x):
		self.x = x
		self.y = 166
		self.file = pygame.image.load('Toadie-Media/images/log1.png').convert_alpha()
		self.surface = self.file.get_rect(midtop = (self.x,self.y))

class Turtle3:
	def __init__(self, x):
		self.x = x
		self.y = 197
		self.file = pygame.image.load('Toadie-Media/images/turtle3.png').convert_alpha()
		self.surface = self.file.get_rect(midtop = (self.x,self.y))

class Truck:
	def __init__(self, x):
		self.touchable = False
		self.x = x
		self.y = 262
		self.file = pygame.image.load('Toadie-Media/images/truck.png').convert_alpha()
		self.rect = self.file.get_rect(topleft = (self.x,self.y))

class Car_Pink:
	def __init__(self, x):
		self.touchable = False
		self.x = x
		self.y = 290
		self.file = pygame.image.load('Toadie-Media/images/car_pink.png').convert_alpha()
		self.rect = self.file.get_rect(topleft = (self.x,self.y))

class Car_Purple:
	def __init__(self, x):
		self.touchable = False
		self.x = x
		self.y = 324
		self.file = pygame.image.load('Toadie-Media/images/car_purple.png').convert_alpha()
		self.rect = self.file.get_rect(topleft = (self.x,self.y))

class Digger:
	def __init__(self, x):
		self.touchable = False
		self.x = x
		self.y = 356
		self.file = pygame.image.load('Toadie-Media/images/digger.png').convert_alpha()
		self.rect = self.file.get_rect(topleft = (self.x,self.y))

class Car_Red:
	def __init__(self, x):
		self.touchable = False
		self.x = x
		self.y = 386
		self.file = pygame.image.load('Toadie-Media/images/car_red.png').convert_alpha()
		self.rect = self.file.get_rect(topleft = (self.x,self.y))

class Toad:
	def __init__(self):
		self.x = 32*6
		self.y = 416+7
		self.file = pygame.image.load('Toadie-Media/images/toad.png').convert_alpha()
		self.rect = self.file.get_rect(topleft = (self.x,self.y))
		#50% or more of the Toad should be touching turtles/logs/pads




#functions

def check_collision(cars):
	for car in cars:
			if toad.rect.colliderect(car.rect):
				#cars.remove(car)
				print("colli")
			else:
				print("no colli")



#pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512) # works in the youtube video but ruins the sound on my pc
pygame.init()
screen = pygame.display.set_mode((448,512))
clock = pygame.time.Clock() #forlater

# game variables
toad_pos = [32*6,416+7]
Lifes    = 3
Score    = 0
Time     = 100 #100 is randomly chosen for now

jump_sound  = pygame.mixer.Sound('Toadie-Media/audio/hop.ogg')


home = pygame.image.load('Toadie-Media/images/home.png').convert() #convert allows the game to run at a faster pace, but the code would work without it
# bg_surface = pygame.transform.scale2x(bg_surface)

toad = Toad()


log2s 		= []
turtle2s	= []
log3s		= []
log1s		= []
turtle3s	= []
trucks 		= []
car_pinks 	= []
car_purples = []
diggers 	= []
car_reds 	= []

for i in range(4):

	new_turtle2 = Turtle2(120*i)
	turtle2s.append(new_turtle2)

	if i < 2:
		new_turtle3 = Turtle3(120*i+20)
	else:
		new_turtle3 = Turtle3(120*i+40)
	turtle3s.append(new_turtle3)

for i in range(3):
	new_car_pink = Car_Pink(160*i+30)
	car_pinks.append(new_car_pink)

	new_car_purple = Car_Purple(160*i+30)
	car_purples.append(new_car_purple)

	new_digger = Digger(200*i+40)
	diggers.append(new_digger)

	new_car_red = Car_Red(160*i)
	car_reds.append(new_car_red)

for i in range(2):
	new_truck = Truck(160*i+60)
	trucks.append(new_truck)




while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit() #makes sure we shut down completey and without it you get an error
		if event.type == pygame.KEYDOWN:
			if event.key == 1073741906 and toad.y > 63:
				toad.y -= 32
			if event.key == 1073741905 and toad.y < 423:
				toad.y += 32
			if event.key == 1073741904 and toad.x > 31:
				toad.x -= 32
			if event.key == 1073741903 and toad.x < 416:
				toad.x += 32
			jump_sound.play()
			toad.rect = toad.file.get_rect(topleft = (toad.x,toad.y))


	screen.fill("darkblue", (0, 0, screen.get_width(), screen.get_height()// 2))
	screen.fill("black", (0, 256, screen.get_width(), screen.get_height()// 2))
	screen.blit(home,(0,0))

	pads = []
	for i in range(5):
		pads.append(Pad())
		x = 25 + i*96 #works almost perfect, but home.png might not be symetrict
		screen.blit(pads[i].file,(x,38))

	# Movement:
	for water_object in turtle2s:
		if water_object.x <= -60:
			water_object.x = 448
		else:
			water_object.x -= 1 #affects object speed
		water_object.rect = water_object.file.get_rect(topleft = (water_object.x,water_object.y))
		screen.blit(water_object.file,water_object.rect)

	for water_object in turtle3s:
		if water_object.x <= -90:
			water_object.x = 448
		else:
			water_object.x -= 1 #affects object speed
		water_object.rect = water_object.file.get_rect(topleft = (water_object.x,water_object.y))
		screen.blit(water_object.file,water_object.rect)


	#trucks
	for car in trucks:
		if car.x <= -52:
			car.x = 448
		else:
			car.x -= 1 #affects object speed
		car.rect = car.file.get_rect(topleft = (car.x,car.y))
		screen.blit(car.file,car.rect)

	#car_pinks
	for car in car_pinks:
		if car.x >= 448:
			car.x = -32
		else:
			car.x += 0.6 #affects object speed
		car.rect = car.file.get_rect(topleft = (car.x,car.y))
		screen.blit(car.file,car.rect)

	#car_purples
	for car in car_purples:
		if car.x <= -32:
			car.x = 448
		else:
			car.x -= 1 #affects object speed
		car.rect = car.file.get_rect(topleft = (car.x,car.y))
		screen.blit(car.file,car.rect)

	#diggers
	for car in diggers:
		if car.x >= 448:
			car.x = -32
		else:
			car.x += 0.9 #affects object speed
		car.rect = car.file.get_rect(topleft = (car.x,car.y))
		screen.blit(car.file,car.rect)

	#car_reds
	for car in car_reds:
		if car.x <= -32:
			car.x = 448
		else:
			car.x -= 0.75 #affects object speed
		car.rect = car.file.get_rect(topleft = (car.x,car.y))
		screen.blit(car.file,car.rect)




	check_collision(car_reds)


	pavement = Pavement()
	for i in range(14):
		screen.blit(pavement.file,(0+i*32,224))

	pavement = Pavement()
	for i in range(14):
		screen.blit(pavement.file,(0+i*32,416))

	#all toad related:

	
	#screen.blit(toad.file,(toad_pos[0],toad_pos[1]))
	screen.blit(toad.file,toad.rect)

	pygame.display.update()
	clock.tick(120)
pygame.quit()