import random
def dice_value():
	return random.randint(1, 6)
def is_prime(num):
	c = 0
	i = 1
	while i <= num:
	    if num % i == 0:
	        c += 1
	    i += 1
	if c == 2:
	    return True 
	else:
	    return False
def is_perfect_square(num):
	i = 1
	x = num
	c = 0
	while i <= num // 2 :
		if i * i == x:
			c = 1
		i += 1
	if c == 1:
		return True
	else:
		return False
def square_root(num):
	i = 1
	x = num
	if is_perfect_square(num) == True:
		while i <= num // 2:
			if i * i == x:
				t = i
			i += 1
		return t
print("Welcome to SNAKES AND LADDERS game!!!")
print("About the game")
print("1.User can roll the dice by pressing 1")
print("2.If the player is on the tile which is a prime number then the player can take a ladder")
print("3.The player will move upto the tile which is twice that number")
print("4.If the player is on the tile which is a perfect square then it is a snake")
print("5.The player moves down to square root of that number")
c1 = 0
c2 = 0
j = 10
a = '_'
board = []
b = int(input("Press 1 to roll the dice"))
if b == 1:
	u = dice_value()
else:
	print("ERROR")
if u == 6:
	c1 += u
	u = dice_value()
c = dice_value()
if c == 6:
	c2 += c
	c = dice_value()
for i in range(10) :
	board += [[a]* i]
print(*board)
print("User position", c1)
print("Computer position", c2)
while c1 < 100 and c2 < 100 :
	if c1 == 95 and u > 5:
		c1 += 0
	elif c1 == 96 and u > 4:
		c1 == 0
	elif c1 == 97 and u > 3:
		c1 == 0
	elif c1 == 98 and u > 2:
		c1 == 0
	elif c1 == 99 and u != 1:
		c1 == 0
	else:
		c1 += u
	if c2 == 95 and c > 5:
		c2 += 0
	elif c2 == 96 and c > 4:
		c2 == 0
	elif c2 == 97 and c > 3:
		c2 == 0
	elif c2 == 98 and c > 2:
		c2 == 0
	elif c2 == 99 and c != 1:
		c2 == 0
	else:
		c2 += c
	if u == 6 and c1 < 94:
	    c1 += u
	    u = dice_value()
	elif c == 6 and c2 < 94:
	    c2 += c
	    c = dice_value()
	if is_prime(c1) == True and c1 < 50:
	    c1 = c1 * 2
	elif is_perfect_square(c1) == True:
	    c1 = square_root(c1)
	elif is_prime(c2) == True and c2 < 50:
	    c2 = c2 * 2
	elif is_perfect_square(c2) == True:
	    c2 = square_root(c2)
	b = int(input("Press 1 to roll the dice"))
	if b == 1:
	    u = dice_value()
	c = dice_value()
	x = c1
	y = c2
	if c1 % 10 == 0:
	    r1 = (x // 10) - 1
	else:
	    r1= x // 10
	if c2 % 10 == 0:
	    r2 = (y // 10) - 1
	else:
	    r2 = y // 10
	col1 = x % 10
	col2 = y % 10
	board[r1[col1 - 1]] = "U"
	board[r2[col2 - 1]] = "C"
	print(*board)
	print("User position", c1)
	print("Computer position", c2)
	board = []
	for i in range(10):
	    board += [[a] * 10]
if c1 > c2:
	print("User won the game")
else:
	print("Computer won the game")