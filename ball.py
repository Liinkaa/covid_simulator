#BALL CLASS

import constants
import random

#AUXILIAR VECTOR CLASS FOR THE MOVEMENT OF THE BALLS
class Vec2:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Infected:

	def __init__(self): 

		self.pos = Vec2(
			random.uniform(constants.AREA_BOX[0], constants.AREA_BOX[1]),
			random.uniform(constants.AREA_BOX[2], constants.AREA_BOX[3])
		)

		self.vel = Vec2(
			random.uniform(-constants.BALL_SPEED, constants.BALL_SPEED),
			random.uniform(-constants.BALL_SPEED, constants.BALL_SPEED),
		)

		self.color = constants.INFECTED_BALL_COLOR

		self.r = constants.RADIUS
	

	def update(self):

		self.pos.x += self.vel.x
		self.pos.y += self.vel.y

		if self.vel.x < 0 and self.pos.x < constants.AREA_BOX[0]:
			self.vel.x *= -1

		if self.vel.x > 0 and self.pos.x > constants.AREA_BOX[1]:
			self.vel.x *= -1

		if self.vel.y < 0 and self.pos.y < constants.AREA_BOX[2]:
			self.vel.y *= -1

		if self.vel.y > 0 and self.pos.y > constants.AREA_BOX[3]:
			self.vel.y *= -1

	def __str__(self):
		return "Infected"

class Ball:

	def __init__(self): 

		self.pos = Vec2(
			random.uniform(constants.AREA_BOX[0], constants.AREA_BOX[1]),
			random.uniform(constants.AREA_BOX[2], constants.AREA_BOX[3])
		)

		self.vel = Vec2(
			random.uniform(-constants.BALL_SPEED, constants.BALL_SPEED),
			random.uniform(-constants.BALL_SPEED, constants.BALL_SPEED),
		)

		self.color = constants.INIT_COLOR

		self.r = constants.RADIUS


	def update(self):

		self.pos.x += self.vel.x
		self.pos.y += self.vel.y

		if self.vel.x < 0 and self.pos.x < constants.AREA_BOX[0]:
			self.vel.x *= -1

		if self.vel.x > 0 and self.pos.x > constants.AREA_BOX[1]:
			self.vel.x *= -1

		if self.vel.y < 0 and self.pos.y < constants.AREA_BOX[2]:
			self.vel.y *= -1

		if self.vel.y > 0 and self.pos.y > constants.AREA_BOX[3]:
			self.vel.y *= -1

	def __str__(self):
		return "Ball"

