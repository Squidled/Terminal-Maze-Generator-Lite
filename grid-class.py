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
