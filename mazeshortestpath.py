import queue
def create():
	maze=[]
	maze.append(["1","S","1","1","1","1","1","1","1","1"])
	maze.append(["1"," ","1","1","1","1","1","1","1","1"])
	maze.append(["1"," ","1","1","1","1","1","1","1","1"])
	maze.append(["1"," ","1","1","1","1","1","1","1","1"])
	maze.append(["1"," "," "," "," "," "," "," "," ","1"])
	maze.append(["1","1","1","1","1","1","1","1"," ","1"])
	maze.append(["1","1","1","1","1","1","1","1"," ","1"])
	maze.append(["1","1","1","1","1","1","1","1","F","1"])
	return maze
def print_m(maze):
	for i in maze:
		print(*i)
def findend(maze,moves):
	i=0
	j=maze[0].index('S')
	for move in moves:
		if move=='l':
			j-=1
		elif move=='r':
			j+=1
		elif move=='u':
			i-=1
		elif move=='d':
			i+=1
	if maze[i][j]=='F':
		print(moves)
		return True
	return False
			
def valid(maze,moves):
	i=0
	j=maze[0].index('S')
	for move in moves:
		if move=='l':
			j-=1
		elif move=='r':
			j+=1
		elif move=='u':
			i-=1
		elif move=='d':
			i+=1
		if not (0<=i <len(maze) and 0<=j < len(maze[0])):
			return False
		elif maze[i][j]=='1':
			return False
	return True 
	

maze=create()
print_m(maze)
n=queue.Queue()
a=""
n.put("")
k=['l','r','u','d']
while findend(maze,a):
	a=n.get()
	for i in k:
		p=a+i
		if valid(maze,p):
			n.put(p)

