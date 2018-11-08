# Game of life implementation by Jorgen Eriksson Midtbo

import numpy as np 
import matplotlib.pyplot as plt 

Nx, Ny = 20,20

def sum_neighbours(matrix, ix, iy):
	sum = 0
	for i in range(3):
		for j in range(3):
			sum += matrix[(ix+i-1)%Nx, (iy+j-1)%Ny]
	sum -= matrix[ix,iy]

	return sum




matrix = np.zeros((Nx,Ny))
matrix[9,8] = 1
matrix[10,9] = 1
matrix[11,10] = 1
matrix[10,11] = 1
matrix[9,12] = 1
# matrix[0,2] = 1
# matrix[5,5] = 1

N_timesteps = 100
f, ax = plt.subplots(1,1)
for i in range(N_timesteps):
	# print(matrix)
	ax.imshow(matrix, cmap="Greys")

	matrix_old = matrix
	matrix = np.zeros((Nx,Ny))
	for ix in range(Nx):
		for iy in range(Ny):
			sn = sum_neighbours(matrix_old, ix, iy)
			# print("ix = {:d}, iy = {:d}, sn = {:d}".format(ix, iy, int(sn)), flush=True)
			if matrix_old[ix,iy] > 0:
				if sn < 2 or sn > 3:
					matrix[ix,iy] = 0
				else:
					matrix[ix,iy] = 1
			else:
				if sn == 3:
					matrix[ix,iy] = 1



	plt.pause(0.5)			

