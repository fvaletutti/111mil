#!/usr/bin/env python3

# Desarrollar un algoritmo que rellene un vector con los números impares comprendidos entre 1 y 100
# y los muestre en pantalla en orden ascendente. 

vector = []

for i in range(1, 101):
	if i % 2 != 0: 
		vector.append(i)

for i in range(0, len(vector)):
	print(str(vector[i]))