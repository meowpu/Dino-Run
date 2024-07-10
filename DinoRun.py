from cmu_graphics import *
spikes=Group(
)
app.time=0
app.stepsPerStep = 120
app.isMovingUp =False
app.isMovingDown =False
Rect(0,300,400,100,fill='khaki')
app.restartButton=Label('⟳',50,50,font='symbols',size=30)
app.isAlive=True
app.dispscore=Label(0,300,50)
dinosaur = Group(
Rect(90,200,30,60,fill='darkGreen'),
Polygon(100,200,100,160,200,200,fill='darkGreen'),
Polygon(90,200,100,160,100,200,fill='darkGreen'),
Rect(80,250,10,50,rotateAngle=30,fill='darkGreen'),
Rect(120,250,10,50,rotateAngle=-30,fill='darkGreen'),
Circle(120,180,5,fill='red')
)
dinosaur.bottom=300
def onStep():
  if (spikes.hitsShape(dinosaur)):
    app.isAlive=False
  if (app.isAlive==True):
    app.dispscore.value+=1
    app.time+=1
  if(app.isMovingUp==True):
    if(app.isAlive==True):
      dinosaur.centerY-=4
  if(dinosaur.top<=25):
    app.isMovingUp=False
    app.isMovingDown=True
  if(app.isMovingDown==True):
    if(app.isAlive==True):
      dinosaur.centerY+=4
  if(app.isAlive==True):
    spikes.centerX-=5
  if(dinosaur.bottom>=300):
    app.isMovingDown=False
  if(app.time==90):
    spikes.add(Rect(400,225,15,75))
    app.time=0
  for spike in spikes.children:
    if (spike.centerX<=0):
      spikes.remove(spike)
def onMousePress(x,y):
  if(dinosaur.bottom==300):
    app.isMovingUp=True
  if(app.restartButton.contains(x,y)):
    if(app.isAlive==False):
      app.dispscore.value=0
      spikes.clear()
      app.isAlive=True
      app.time=0
cmu_graphics.run()
