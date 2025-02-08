import pygame.font

class Button():

	def __init__(self,ai_settings,screen,msg):
		"""Inicializa os atributos do botao """
		self.screen = screen
		self.screen_rect = screen.get_rect()

		# Define as dimensoes e as prorpiedades do btn
		self.width, self.heigth =200,50
		self.button_color =(0,255,0)
		self.text_color = (255,255,255)
		self.font = pygame.font.SysFont(None, 48)

		# Constroi o objeto rect do btn e centraliza
		self.rect = pygame.Rect(0, 0, self.width, self.heigth)
		self.rect.center = self.screen_rect.center

		# A mensagem do btn deve aparece apenas uma vez
		self.prep_msg(msg)

	def prep_msg(self,msg):
		"""Transforma msg em img"""
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		# Desenha o btn e escreve a msg
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
