import pygame, random, sys

#objects
class Pad:
	def __init__(self, x):
		self.x = x
		self.y = 38
		self.occupied = False
		self.file = pygame.image.load('Toadie-Media/images/pad.png').convert_alpha()
		self.rect = self.file.get_rect(midtop = (self.x,self.y))
		with_toad = pygame.image.load('Toadie-Media/images/toad.png').convert_alpha()
		self.with_toad = pygame.transform.rotozoom(with_toad,180,1) 
		self.toad_rect = self.with_toad.get_rect(midtop = (self.x-1,self.y-2))

class Pavement:
	def __init__(self):
		self.touchable = True
		self.file = pygame.image.load('Toadie-Media/images/pavement.png').convert_alpha()

class Toad_Lives:
	def __init__(self):
		self.file = pygame.image.load('Toadie-Media/images/toad_lives.png').convert_alpha()

class Log2:
	def __init__(self, x):
		self.x = x
		self.y = 70
		self.speed = 0.7
		self.leaving_x = 448
		self.reset_x = -115
		self.file = pygame.image.load('Toadie-Media/images/log2.png').convert_alpha()
		self.rect = self.file.get_rect(midtop = (self.x,self.y))

class Turtle2:
	def __init__(self, x):
		self.x = x
		self.y = 101
		self.speed = -1
		self.leaving_x = -60
		self.reset_x = 448
		self.file = pygame.image.load('Toadie-Media/images/turtle2.png').convert_alpha()
		self.rect = self.file.get_rect(midtop = (self.x,self.y))

class Log3:
	def __init__(self, x):
		self.x = x
		self.y = 134
		self.speed = 1
		self.leaving_x = 448
		self.reset_x = -180
		self.file = pygame.image.load('Toadie-Media/images/log3.png').convert_alpha()
		self.rect = self.file.get_rect(midtop = (self.x,self.y))

class Log1:
	def __init__(self, x):
		self.x = x
		self.y = 166
		self.speed = 0.6
		self.leaving_x = 448
		self.reset_x = -84
		self.file = pygame.image.load('Toadie-Media/images/log.png').convert_alpha()
		self.rect = self.file.get_rect(midtop = (self.x,self.y))

class Turtle3:
	def __init__(self, x):
		self.x = x
		self.y = 197
		self.speed = -1
		self.leaving_x = -90
		self.reset_x = 448
		self.file = pygame.image.load('Toadie-Media/images/turtle3.png').convert_alpha()
		self.rect = self.file.get_rect(midtop = (self.x,self.y))

class Truck:
	def __init__(self, x):
		self.touchable = False
		self.x = x
		self.y = 262
		self.speed = -1
		self.leaving_x = -50
		self.reset_x = 448
		self.file = pygame.image.load('Toadie-Media/images/truck.png').convert_alpha()
		self.rect = self.file.get_rect(topleft = (self.x,self.y))

class Car_Pink:
	def __init__(self, x):
		self.touchable = False
		self.x = x
		self.y = 290
		self.speed = 0.6
		self.leaving_x = 448
		self.reset_x = -32
		self.file = pygame.image.load('Toadie-Media/images/car_pink.png').convert_alpha()
		self.rect = self.file.get_rect(topleft = (self.x,self.y))

class Car_Purple:
	def __init__(self, x):
		self.touchable = False
		self.x = x
		self.y = 324
		self.speed = -1
		self.leaving_x = -32
		self.reset_x = 448
		self.file = pygame.image.load('Toadie-Media/images/car_purple.png').convert_alpha()
		self.rect = self.file.get_rect(topleft = (self.x,self.y))

class Digger:
	def __init__(self, x):
		self.touchable = False
		self.x = x
		self.y = 356
		self.speed = 0.9
		self.leaving_x = 448
		self.reset_x = -32
		self.file = pygame.image.load('Toadie-Media/images/digger.png').convert_alpha()
		self.rect = self.file.get_rect(topleft = (self.x,self.y))

class Car_Red:
	def __init__(self, x):
		self.touchable = False
		self.x = x
		self.y = 386
		self.speed = -0.75
		self.leaving_x = -32
		self.reset_x = 448
		self.file = pygame.image.load('Toadie-Media/images/car_red.png').convert_alpha()
		self.rect = self.file.get_rect(topleft = (self.x,self.y))

class Toad:
	def __init__(self):
		self.x 		  = 32*6
		self.y 		  = 416+7
		self.file 	  = pygame.image.load('Toadie-Media/images/toad.png').convert_alpha()
		self.file_alt = pygame.image.load('Toadie-Media/images/dead_toad.png').convert_alpha()
		self.rect 	  = self.file.get_rect(topleft = (self.x,self.y))
		#50% or more of the Toad should be touching turtles/logs/pads


# functions
def move_all_objects(objects): #can probably be much nicer
	for game_object in objects:
		if game_object.speed > 0:
			if game_object.x >= game_object.leaving_x:
				game_object.x = game_object.reset_x
			else:
				game_object.x += game_object.speed*movement #affects object speed

		else:
			if game_object.x <= game_object.leaving_x:
				game_object.x = game_object.reset_x
			else:
				game_object.x += game_object.speed*movement #affects object speed

		game_object.rect = game_object.file.get_rect(topleft = (game_object.x,game_object.y))
		screen.blit(game_object.file,game_object.rect)

def check_collision_pad(toad, pads):
	for pad in pads:
			if toad.rect.colliderect(pad.rect):
				toad.x = 32*6
				toad.y = 416+7
				toad.rect = toad.file.get_rect(topleft = (toad.x,toad.y))
				screen.blit(toad.file,toad.rect)
				if pad.occupied == False:
					pad.occupied = True
					return(True)
				else:
					return(False)
	return(False)


def check_collision(cars):
	for car in cars:
		if toad.rect.colliderect(car.rect):
			#return(False) # while developig
			return(True)
	return(False)

def check_collision_water_object(water_objects):
	for water_object in water_objects:
		if toad.rect.colliderect(water_object.rect):
			return(water_object.speed)
	return(0)


def score_display():
		score_surface = game_font.render("SCORE  "+str(int(score)),True,(255,255,255))
		score_rect = score_surface.get_rect(topleft = (10,480))
		screen.blit(score_surface,score_rect)

def time_display(time):
	time_bar_surface = 0
	pygame.draw.rect(screen,(0,255,0),(280,473,100,25)) # green bar for full time
	pygame.draw.rect(screen,(255,0,0),(280,473,100-time,25)) # growing red bar
	time_surface = game_font.render("TIME",True,(255,255,0))
	time_rect = time_surface.get_rect(topleft = (400,480))
	screen.blit(time_surface,time_rect)
	if time > 0:
		return(time-0.03*movement)
	return(0)



# pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512) # works in the youtube video but ruins the sound on my pc
pygame.init()
screen = pygame.display.set_mode((448,512))
clock = pygame.time.Clock() #forlater

# game variables
toad_moved_y = 416+7
lives    = 3
score    = 0
game_state = 0 # 0 = starting screen | 1 = playing the game | 2 = game over | 3 = victory
time     = 100 #100 is randomly chosen for now
times_won = 0
movement = 1+times_won*0.2
game_font = pygame.font.Font('04B_19.TTF',12)
game_font_b = pygame.font.Font('04B_19.TTF',36)

jump_sound  = pygame.mixer.Sound('Toadie-Media/audio/hop.ogg')


home = pygame.image.load('Toadie-Media/images/home.png').convert() #convert allows the game to run at a faster pace, but the code would work without it
# bg_surface = pygame.transform.scale2x(bg_surface)

toad = Toad()
pavement = Pavement()
toad_live = Toad_Lives()

#creating objects
pads 		= []
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

for i in range(5):

	new_pad = Pad(35 + i*96)
	pads.append(new_pad) #works almost perfect, but home.png might not be symetrict

for i in range(4):

	new_turtle2 = Turtle2(120*i)
	turtle2s.append(new_turtle2)

	if i < 2:
		new_turtle3 = Turtle3(120*i+20)
	else:
		new_turtle3 = Turtle3(120*i+40)
	turtle3s.append(new_turtle3)

for i in range(3):

	new_log2 = Log2(170*i)
	log2s.append(new_log2)

	new_log1 = Log1(180*i)
	log1s.append(new_log1)

	new_car_pink = Car_Pink(160*i+30)
	car_pinks.append(new_car_pink)

	new_car_purple = Car_Purple(160*i+30)
	car_purples.append(new_car_purple)

	new_digger = Digger(200*i+40)
	diggers.append(new_digger)

	new_car_red = Car_Red(160*i)
	car_reds.append(new_car_red)

for i in range(2):
	new_log3 = Log3(250*i)
	log3s.append(new_log3)

	new_truck = Truck(160*i+60)
	trucks.append(new_truck)

#game loop
while True: 
	while game_state == 0:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				game_state = 1
				lives = 3
				toad.x = 32*6
				toad.y = 416+7

		screen.fill("black", (0, 0, screen.get_width(), screen.get_height()))

		start_surface = game_font_b.render("Welcome to Toadie",True,(0,255,0))
		start_rect = start_surface.get_rect(topleft = (55,80))
		screen.blit(start_surface,start_rect)

		start_surface_b = game_font_b.render("Press any key to start",True,(0,255,0))
		start_rect_b = start_surface_b.get_rect(topleft = (5,400))
		screen.blit(start_surface_b,start_rect_b)

		pygame.display.update()
		clock.tick(120)


	while game_state == 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit() #makes sure we shut down without errors
			if event.type == pygame.KEYDOWN:
				if event.key == 1073741906 and toad.y > 63 and movement != 0:
					toad.y -= 32
					jump_sound.play()
					if toad.y == toad_moved_y-32:
						toad_moved_y -= 32
						score+=10+times_won*5
				if event.key == 1073741905 and toad.y < 423:
					toad.y += 32
					jump_sound.play()
				if event.key == 1073741904 and toad.x > 31:
					toad.x -= 32
					jump_sound.play()
				if event.key == 1073741903 and toad.x < 416:
					toad.x += 32
					jump_sound.play()
				if movement == 0:
					toad.x = 32*6
					toad.y = 416+7
					toad_moved_y = 416+7
					#movement = 1
					movement = 1+times_won*0.2
					time = 100
				toad.rect = toad.file.get_rect(topleft = (toad.x,toad.y))



		screen.fill("darkblue", (0, 0, screen.get_width(), screen.get_height()// 2))
		screen.fill("black", (0, 256, screen.get_width(), screen.get_height()// 2))
		screen.blit(home,(0,0))

		for water_object in pads:
			screen.blit(water_object.file,water_object.rect)
			if water_object.occupied == True:
				screen.blit(water_object.with_toad,water_object.toad_rect)

		# Movement:
		move_all_objects(log2s+turtle2s+log3s+log1s+turtle3s+trucks+car_pinks+car_purples+diggers+car_reds)

		#Pavement, Lives, Score and Time display
		for i in range(14):
			screen.blit(pavement.file,(0+i*32,224))
			screen.blit(pavement.file,(0+i*32,416))

		for i in range(lives):
			screen.blit(toad_live.file,(i*15+10,460))
		score_display()
		time = time_display(time)

		#all toad related:

		if time == 0:
			if movement == 1:
				lives -= 1
			movement = 0
			screen.blit(toad.file_alt,toad.rect)

		if check_collision_pad(toad, pads) == True:
			score+=round(time/10)*10*lives+times_won*5
			time = 100

		if check_collision(trucks+car_pinks+car_purples+diggers+car_reds) == True:
			if movement == 1:
				lives -= 1
			movement = 0
			screen.blit(toad.file_alt,toad.rect)


		on_water_object = check_collision_water_object(log1s+log2s+log3s+turtle2s+turtle3s) 
		toad.x += on_water_object*movement

		+times_won*0.2
		if toad.y < 224 and on_water_object == 0:
			if movement != 0:
				lives -= 1
			movement = 0
			screen.blit(toad.file_alt,toad.rect)

		if movement != 0:
			toad.rect = toad.file.get_rect(topleft = (toad.x,toad.y))
			screen.blit(toad.file,toad.rect)

		win_condition = 5
		for pad in pads:
			if pad.occupied:
				win_condition-=1
		if win_condition == 0 and movement != 0:
				game_state = 3
				times_won += 1

		if lives == 0:
			game_state = 2

		pygame.display.update()
		clock.tick(120)

	while game_state == 2:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				for pad in pads:
					pad.occupied = False
				game_state = 1
				toad.x = 32*6
				toad.y = 416+7
				lives = 3
				toad_moved_y = 416+7
				movement = 1
				score = 0
				time = 100
				toad.rect = toad.file.get_rect(topleft = (toad.x,toad.y))

		screen.fill("black", (0, 0, screen.get_width(), screen.get_height()))

		start_surface = game_font_b.render("game over",True,(0,255,0))
		start_rect = start_surface.get_rect(center = (224,80))
		screen.blit(start_surface,start_rect)

		#Scoreboard (perhaps you could add high scores)

		start_surface_b = game_font_b.render("Your Score is "+str(score),True,(0,255,0))
		start_rect_b = start_surface_b.get_rect(center = (224,256))
		screen.blit(start_surface_b,start_rect_b)

		start_surface_b = game_font_b.render("Press any key to start",True,(0,255,0))
		start_rect_b = start_surface_b.get_rect(topleft = (5,400))
		screen.blit(start_surface_b,start_rect_b)

		pygame.display.update()
		clock.tick(120)

	while game_state == 3:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				for pad in pads:
					pad.occupied = False
				game_state = 1
				toad.x = 32*6
				toad.y = 416+7
				lives = 3
				toad_moved_y = 416+7
				movement = 1+times_won*0.2
				time = 100
				toad.rect = toad.file.get_rect(topleft = (toad.x,toad.y))

		screen.fill("black", (0, 0, screen.get_width(), screen.get_height()))

		start_surface = game_font_b.render("You Won!",True,(0,255,0))
		start_rect = start_surface.get_rect(center = (224,80))
		screen.blit(start_surface,start_rect)

		#Scoreboard (perhaps you could add high scores)

		start_surface_b = game_font_b.render("Your Score is "+str(score),True,(0,255,0))
		start_rect_b = start_surface_b.get_rect(center = (224,256))
		screen.blit(start_surface_b,start_rect_b)

		start_surface_b = game_font_b.render("Press any key to start",True,(0,255,0))
		start_rect_b = start_surface_b.get_rect(topleft = (5,400))
		screen.blit(start_surface_b,start_rect_b)

		pygame.display.update()
		clock.tick(120)

pygame.quit()