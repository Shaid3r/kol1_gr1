#!/usr/bin/python3

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
