import pygame as pg
from settings import *


class Button:
	def __init__(self, x, y, image, scale):
		self.width = image.get_width()
		self.height = image.get_height()
		self.image = pg.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
		self.is_active = True

	def update_state(self, surface, should_appear_on_screen=True):
		action = False
		pos = pg.mouse.get_pos()

		if self.rect.collidepoint(pos):
			for event in pg.event.get():
				if event.type == pg.MOUSEBUTTONDOWN and self.is_active:
					self.is_active = False
					self.clicked = True
					break
				if event.type == pg.MOUSEBUTTONUP and not self.is_active:
					self.is_active = True
					self.clicked = False

		if self.clicked:
			action = True

		if pg.mouse.get_pressed()[0] == 0:
			self.clicked = False

		if self.image and should_appear_on_screen and self.is_active:
			surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
