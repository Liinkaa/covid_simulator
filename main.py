
#PYTHON CORONAVIRUS SIMULATION

import random
import pyxel
import constants
from ball import Ball
from ball import Infected

class App:

	def __init__(self):

		self.reset()

		self.balls = []#python list that will store the balls that are currently not infected in the box
		self.infected_balls = [Infected()]#python list that will store the balls that are currently infected in the box
		self.everybody_infected = False

		for i in range(random.randint(constants.RANGE_BALLS_GENERATED[0], constants.RANGE_BALLS_GENERATED[1])):
			self.balls.append(Ball())

		pyxel.init(constants.SCREEN_SIZE[0], constants.SCREEN_SIZE[1], caption = "Coronavirus simulation")
		pyxel.run(self.update, self.draw)


	def reset(self):

		#SET INITIAL CONDITIONS
		self.balls = []
		self.infected_balls = [Infected()]

		for i in range(random.randint(constants.RANGE_BALLS_GENERATED[0], constants.RANGE_BALLS_GENERATED[1])):
			self.balls.append(Ball())


	def update(self):
		
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()

		if pyxel.btnp(pyxel.KEY_R):
			self.reset()

		#stop when all balls are infected
		if len(self.balls) == 0:
			self.everybody_infected = True
			return

		#update ball movement
		for infected_ball in self.infected_balls:
			infected_ball.update()
		
		for ball in self.balls:
			ball.update()
		
		#check now if an infected ball is in contact with a non-infected ball
		for infected_ball in self.infected_balls:

			for normal_ball_index in range(len(self.balls)):
				
				if round(infected_ball.pos.x, 0) == round(self.balls[normal_ball_index].pos.x, 0) and round(infected_ball.pos.y, 0) == round(self.balls[normal_ball_index].pos.y, 0):

					#replace ball to infected in case of contact
					new_infected = Infected()

					#the new infected has the same attributes that the normal ball had
					new_infected.pos.x = self.balls[normal_ball_index].pos.x
					new_infected.pos.y = self.balls[normal_ball_index].pos.y
					new_infected.vel.x = self.balls[normal_ball_index].vel.x
					new_infected.vel.y = self.balls[normal_ball_index].vel.y

					#add to infected list
					self.infected_balls.append(new_infected)

					#remove from normal ball list
					del(self.balls[normal_ball_index])

	def draw(self):

		#backgorund
		pyxel.cls(constants.BACKGROUND[0])	

		#main cap
		pyxel.text(constants.MAIN_TEXT_POS[0], constants.MAIN_TEXT_POS[1], "COVID INFECTION RATE", 3) #[x, y, text, color]

		#other caps
		pyxel.text(constants.AUX_TEXT_POS[0], constants.AUX_TEXT_POS[1], "PRESS R TO RESTART | PRESS Q TO QUIT", 11)

		#box
		pyxel.rectb(constants.BOX[0], constants.BOX[1], constants.BOX[2], constants.BOX[3], constants.BOX[4]) #draw the outline of a rectangle: rect(x, y, w, h, col)

		#balls
		for j in self.balls:

			pyxel.circ(j.pos.x, j.pos.y, j.r, j.color) #draw circle: circ(x, y, radius, color)

		for i in self.infected_balls:

			pyxel.circ(i.pos.x, i.pos.y, i.r, i.color)

		#when everybody is infected
		if self.everybody_infected == True:

			pyxel.text(constants.AUX_TEXT_POS[0], constants.AUX_TEXT_POS[1]+7, "EVERYBODY GOT INFECTED!", 8)


App()
