import pygame

class Ship():

	def __init__(self,ai_settings,screen):
		"""Inicializa a espaçonave e define a sua posiçao inicial"""
		self.screen = screen
		self.ai_settings = ai_settings
		# Carrega a imagem da espaçonave e obtém seu rect
		self.image = pygame.image.load("imgs/ship.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Inicia cada nova espaçonave na parte inferio central da tela
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Aramazenar um valor decimal para o centro da espaçonave
		self.center = float(self.rect.centerx)

		# Flag de movimento
		self.moving_right = False
		self.moving_lefth = False

	def update(self):
		""" Atualiza a posiçao da espaçonave de acordo com a flag de movimento """
		# Atualiza o valor do centro da espaçonave, e n do retângulo
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor

		if self.moving_lefth and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor

		# Atualiza o objeto rect de acordo com self.center
		self.rect.centerx = self.center

	def blitme(self):
		"""Desenha a espaçonave em sua posiçao atual """
		self.screen.blit(self.image, self.rect)
