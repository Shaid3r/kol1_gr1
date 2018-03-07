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
	def __init__(self, a, b, c, d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d

	def __add__(self, matrix):
		return Matrix(self.a + matrix.a, self.b + matrix.b, self.c + matrix.c, self.d + matrix.d)

	def __mul__(self, number):
		return Matrix(self.a * number, self.b * number, self.c * number, self.d * number)

	__rmul__ = __mul__

	def __str__(self):
		return "Matrix: ({},{},{},{})".format(
			self.a, self.b, self.c, self.d)

if __name__ == "__main__":
	print("Matrix_1:")
	matrix_1 = Matrix(4,5,6,7)
	print(matrix_1)
	print("Matrix_2:")
	matrix_2 = Matrix(2,2,2,1)
	print(matrix_2 )
	print("Matrix_1 + matrix 2:")
	print(matrix_1 + matrix_2)
	print("Matrix_1 * 3:")
	print(matrix_1 * 3)
