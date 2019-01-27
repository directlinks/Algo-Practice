maze=[[1,1,1,1],
[1,1,0,0],
[1,0,0,1],
[1,1,1,1]
]

x=[-1,1,0,0] #top,bottom,left,right
y=[0,0,-1,1]

class node:

	def __init__(self,x,y,d):
		self.x=x # x coordinate
		self.y=y # y coordinate
		self.d=0 # distance

queue=[]
visited=[[0 for j in range(4)]for i in range(4)]

def isvalid(temp):
	if temp.x>=0 and temp.y>=0 and temp.x<4 and temp.y<4 and visited[temp.x][temp.y]==0 and maze[temp.x][temp.y]!=0:
		return True
	else:
		return False
def bfs(src,destination): #src=0 destination=3
	visited[src.x][src.y]=1
	
	
	if maze[src.x][src.x]==0 or maze[destination.x][destination.y]==0:
		'''if starting point or ending point are zeros'''
		return -1
	
	#print src.x
	queue.append(src)
	#print stack
	while queue:
		current=queue.pop()

		if current.x==destination.x and current.y==destination.y:
			return current.d

		for i in range(4):
			x_=current.x+x[i]
			y_=current.y+y[i]
			temp=node(x_,y_,current.d)
			# print temp.x
			# print temp.y
			# print isvalid(temp)
			# print visited
			# raw_input()
			if isvalid(temp):
				temp.d=current.d+1
				visited[temp.x][temp.y]=1
				
				queue.append(temp)
	



src=node(0,0,0)
destination=node(1,1,0)
print bfs(src,destination)