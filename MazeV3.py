import os,random,sys
sys.setrecursionlimit(1000000)
class Grid:
	def __init__(self,x_width,y_width,charchter):
		self.y_width = y_width
		self.x_width = x_width
		self.charchter = charchter
		self.grid_list = []
		for i in range(0,x_width * y_width):
			self.grid_list.append(self.charchter + " ")
		self.grid_checks = []
		for m in range(0,self.y_width//2):
			for l in range(0,self.x_width//2):
				self.grid_checks.append((2*l+1)+(2*(self.x_width*m)+self.x_width))
	def printgrid(self):
		os.system("clear")
		for i in range(0,self.y_width):
			line = ""
			for x in range(0,self.x_width):line += self.grid_list[x+(self.x_width*i)]
			print(line)
	def changeSpot(self,x,y,charchter):
		self.grid_list[x+y*self.x_width] = f"{charchter} "
	def checkSpot(self,x,y):
		return self.grid_list[x+y*self.x_width]
os.system("clear")
print("Please input a width and height for the maze! Both must be odd numbers")
width = int(input("Your width: ")); height = int(input("Your height: "))
Maze = Grid(width,height,"🀫")
Maze.changeSpot(0,1,">"); Maze.changeSpot(Maze.x_width-1,Maze.y_width-2,">")
def Wander(wander_x,wander_y):
	Maze.changeSpot(wander_x,wander_y,".")
	possibles = [(-2,0),(2,0),(0,2),(0,-2)]
	if all(Maze.grid_list[i] == Maze.grid_list[Maze.grid_checks[len(Maze.grid_checks)-1]] for i in Maze.grid_checks): Maze.printgrid(); return	
	print(f"{[Maze.grid_list[i] for i in Maze.grid_checks].count('. ')}/{len(Maze.grid_checks)}", end = "\r")
	def tryPobl():
		random1 = random.randint(0,len(possibles)-1)
		current_Pobl = possibles[random1]
		del possibles[random1]
		if ((wander_x + current_Pobl[0] >= 0 and wander_x+current_Pobl[0] < Maze.x_width) and (wander_y + current_Pobl[1] >= 0 and wander_y + current_Pobl[1] < Maze.y_width)) and (Maze.checkSpot(wander_x+current_Pobl[0],wander_y+current_Pobl[1]) != ". "):
			try:
				Maze.changeSpot(int(wander_x+current_Pobl[0]/2),int(wander_y+current_Pobl[1]/2),".")
				Wander(wander_x+current_Pobl[0],wander_y+current_Pobl[1])
			except Exception: tryPobl()
		else: tryPobl()
	tryPobl()
Wander(Maze.x_width-2,Maze.y_width-2)




	
