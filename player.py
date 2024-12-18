import pygame

class Player():
	def __init__(self):
		self.image = pygame.image.load("./assets/Pink_Monster.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (48, 48))
		print(f"Taille de l'image du joueur : {self.image.get_size()}")
		self.rect = self.image.get_rect()
		self.LEFT_KEY, self.RIGHT_KEY, self.FACING_LEFT = False, False, False
		self.is_jumping, self.on_ground = False, False
		self.gravity, self.friction = 0.3, -.12
		self.position, self.velocity = pygame.math.Vector2(0, 0), pygame.math.Vector2(0, 0)
		self.acceleration = pygame.math.Vector2(0, self.gravity)
		self.rect.topleft = self.position
	
	def draw(self, display):
		display.blit(self.image, self.rect)

	def update(self, dt):
		self.horizontal_mouvement(dt)
		self.vertical_mouvement(dt)
		self.rect.topleft = self.position
		# print(f"Position du joueur après update : x={self.position.x}, y={self.position.y}")

	def horizontal_mouvement(self, dt):
		self.acceleration.x = 0
		if self.LEFT_KEY:
			self.acceleration.x -= .3
		elif self.RIGHT_KEY:
			self.acceleration.x += .3
		self.acceleration.x += self.velocity.x * self.friction
		self.velocity.x += self.acceleration.x * dt
		self.limit_velocity(4)
		self.position.x += self.velocity.x * dt + (self.acceleration.x * .5) * (dt * dt) #a tester en negatif
		self.rect.x = self.position.x

	def limit_velocity(self, max_val):
		self.velocity.x = max(-max_val, min(self.velocity.x, max_val))
		if abs(self.velocity.x) < .01: self.velocity.x = 0

	def vertical_mouvement(self, dt):
		self.velocity.y += self.acceleration.y * dt
		if self.velocity.y > 7: self.velocity.y = 7 #limite de la vitesse du saut
		self.position.y += self.velocity.y * dt + (self.acceleration.y * .5) * (dt * dt)
		if self.position.y > 496:
			self.on_ground = True
			self.velocity.y = 0
			self.position.y = 496
		self.rect.bottom = self.position.y

	def jump(self):
		if self.on_ground:
			self.is_jumping = True
			self.velocity.y -= 8
			self.on_ground = False

	def reset_key(self):
		self.LEFT_KEY, self.RIGHT_KEY = False, False
		self.is_jumping = False
		self.FACING_LEFT = False