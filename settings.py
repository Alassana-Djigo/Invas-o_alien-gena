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

		# Configuraçoes dos projéteis
		self.bullet_speed_factor = 0.5
		self.bullet_width = 5
		self.bullet_height =15
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 3
