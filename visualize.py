import pygame, random, time

#-----------------------------------------------------------------------------------------------
def insertionsort(arr,delay):
        sorted = []
        while len(arr) !=  0:

                sorted.append(arr[0])
                arr = arr[1:]
                for i in range(len(sorted)-1, 0, -1):
                        if len(sorted) == 1: 
                                break
                        elif sorted[i] < sorted[i-1]:
                                temp = sorted[i]
                                sorted[i] = sorted[i-1]
                                sorted[i-1] = temp 
                        else:
                                break
                graph = [x for x in sorted]
                for x in arr:
                        graph.append(x)

                draw(graph,white)
                time.sleep(delay)   
        return sorted
#-----------------------------------------------------------------------------------------------
def bubblesort(arr,delay):
	for i in range(len(arr)):
		for j in range(len(arr)-1-i):
			if arr[j] > arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
		draw(arr,white)
		time.sleep(delay)
	return arr
#-----------------------------------------------------------------------------------------------
def smallest(arr):
	small = {
	'num':arr[0],
	'index':0
	}
	for i in range(len(arr)):
		if arr[i] < small['num']:
			small['num'] = arr[i]
			small['index'] = i
	return small

def selectionsort(arr,delay):
	sorted=[]
	for i in range(len(arr)):
		small = smallest(arr)
		temp = arr[0]
		arr[0] = small['num']
		arr[small['index']] = temp
		sorted.append(arr[0])
		arr=arr[1:]
		graph = [x for x in sorted]
		for x in arr:
			graph.append(x)
		draw(graph,white)
		time.sleep(delay)
	return sorted
#-----------------------------------------------------------------------------------------------

pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

display_width = 1000
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))

clock = pygame.time.Clock()

values = [random.randint(0,display_height) for i in range(int(display_width/10))]

def draw(graph, color):
	gameDisplay.fill(black)
	x = 0
	for i in range(len(graph)):		
		pygame.draw.rect(gameDisplay, color, [x, display_height-graph[i], 10, graph[i]])
		x += 10
	pygame.display.update()

def display_text(msg,color,x,y,size):
	font=pygame.font.SysFont('verdana',size)
	text=font.render(str(msg),True,color)
	gameDisplay.blit(text, [x,y])
	pygame.display.update()

def finish(arr):
	x = 0
	for i in range(len(arr)):
		pygame.draw.rect(gameDisplay,green, [x, display_height-arr[i], 10, arr[i]])
		x+=10
		pygame.display.update()

def visualize(sortingalg,delay=0.01,values=values):
	start = time.time()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
		arr = sortingalg(values,delay)		
		if arr:
			end = time.time()
			runtime = end-start
			finish(arr)
			return runtime

	time.sleep(1)
delay = 0.01
runtime = visualize(selectionsort,delay)
display_text(runtime, white, 50, 50, 25)
time.sleep(5)

