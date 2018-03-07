#!/usr/bin/python3
#Write a library that contains a class that can represent any 2𝑥2 real matrice. 
#Include two functions to calculate the sum and product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
#Examples:
#
# matrix_1 = Matrix(4,5,6,7)
# matrix_2 = Matrix(2,2,2,1)
#
# matrix_3 = matrix_2.add(matrix_1)
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#(If you want you can expand implementation to NxN matrix.)
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#The whole repository MUST be a fork from https://github.com/mwmajew/kol1_gr1.py
#
#Delete these comments before commit!
#Good luck.


class Matrix:
	def __init__(self, n, m):
		self.rows = n
		self.columns = m
		self.data = [[0] * m for x in range(n)]

	def __add__(self, matrix):
		m = Matrix(n, m)
		for i in range(n):
			for j in range(m):
				m.data[i][j] += self.data[i][j]
		return m

	def __index__(self, num):
		return

	# def __mul__(self, number):
	# 	return Matrix(self.a * number, self.b * number, self.c * number, self.d * number)

	def __str__(self):
		s = ""
		for row in self.data:
			s += str(row) + "\n"
		return s[:-1]

if __name__ == "__main__":
	print("Matrix:")
	matrix_1 = Matrix(2,3)
	# matrix_1[1][3] = 3
	print(matrix_1)
