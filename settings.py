class Settings():
	"""Uma classe para armazenar todas as configuraçoes da Invasao Alienígena """

	def __init__(self):
		"""Inicializa as configuraçoes"""
		# Configuraçao da tela
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)

		# Configuraçao da espaçonave
		self.ship_speed_factor = 1.5
		self.ship_limit = 3

		# Configuraçoes dos projéteis
		self.bullet_speed_factor = 0.5
		self.bullet_width = 5
		self.bullet_height =15
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 3

		# Configurações dos alienígenas
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		self.fleet_direction = 1
