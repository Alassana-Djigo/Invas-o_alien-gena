class Settings():
	"""Uma classe para armazenar todas as configuraçoes da Invasao Alienígena """

	def __init__(self):
		"""Inicializa as configuraçoes estaticas"""
		# Configuraçao da tela
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)

		# Configuraçao da espaçonave
		self.ship_limit = 3

		# Configuraçoes dos projéteis
		self.bullet_width = 5
		self.bullet_height =15
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 3

		# Configurações dos alienígenas
		self.fleet_drop_speed = 10

		# A taxa com que a velocidade do jogo aumenta
		self.speedup_scale = 1.1
		self.score_scale = 1.5
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Inicializa as configurações que mudam no decorrer do jogo."""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1

		# fleet_direction igual a 1 representa a direita; -1 representa a esquerda
		self.fleet_direction = 1

		# Pontuação
		self.alien_points = 50

	def increase_speed(self):
		"""Aumenta as configurações de velocidade."""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
