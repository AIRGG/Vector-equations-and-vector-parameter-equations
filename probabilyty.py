import random

tmpx = 2
tmpy = -3
tmpz = 1
for k in range(10000):
	x = random.randrange(1, 9)
	y = random.randrange(1, 9)
	z = random.randrange(1, 9)
	cek = (tmpx * x) + (tmpy * y) + (tmpz * z)
	if cek == 3:
		print(x, y, z)