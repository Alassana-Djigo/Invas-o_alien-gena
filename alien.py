import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Uma classe que representa um único alien da frota"""

	def __init__(self,ai_settings,screen):
		"""Inicializa e define a posiçao inicial"""
		super(Alien,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# Carrega a imagem do alien e define rect
		self.image = pygame.image.load("imgs/alien01.bmp")
		self.rect = self.image.get_rect()

		# Inicia cada novo alien no topo da tela
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Armazena a posiçao do alien
		self.x = float(self.rect.x)

	def blitme(self):
		"""Desenha o alien"""
		self.screen.blit(self.image,self.rect)

	def check_edges(self):
		"""Devolve True se o mesmo estiver na borda da tela"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True

	def update(self):
		"""Move-os para a direita"""
		self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x
