

class Controller : 
    def _init_(self, nbColumn, nbElevator, nbFloor):
        self.nbColumn = nbColumn
        self.nbElevator = nbElevator
        self.nbFloor = nbFloor
        self.column = Column(nbElevator, nbFloor)
        
    

class Column : 
    def _init_(self, nbElevator, nbFloor):
    self.nbElevator = nbElevator
    self.elevatorList = []
    self.callBtnList = []
    self.nbFloor = nbFloor
    self.bestElevator = None
    self.status = "on"


    i= 0
    while i < self.nbElevator:
        self.elevatorList.append(Elevator(i, nbFloors))
        i += 1

    j = 1 
    while j <= self.nbFloor:
        self.callBtnList.append(callBtn(j, "down"))
        self.callBtnList.append(callBtn(j, "up"))
        j += 1

    self.callBtnList.pop(0)
    self.callBtnList.pop(len(self.callBtnList)-1)

def findBestElevator(self, currentFloor, direction):
    bestElevator = None
    floorDifference1 = []

    if bestElevator == None:
        for elevator in self.elevatorList:
            if elevator.status is "moveDown" and currentFloor < elevator.position and direction is "down":
                bestElevator = elevator
    
    if bestElevator == None:
        for elevator in self.elevatorList:
            if elevator.status is "moveUp" and currentFloor > elevator.position and direction is "up":
                bestElevator == elevator

    if bestElevator == None: 
        for elevator in self.elevatorList:
            if elevator.status is "idle":
                floorDifference = abs(currentFloor - elevator.position)
                floorDifference1.append(floorDifference)
            else: floorDifference1.append(9999)

        bestScore = 10000
        for score in floorDifference1:
            if bestScore > score:
                bestScore = score

    scoreIndex = floorDifference1.index(bestScore)
    bestElevator = self.elevatorList[scoreIndex]
    self.bestElevator = bestElevator

    def RequestElevator(self, requestedFloor, direction):
        print("Request an elevator")
        time.sleep(1)
        print("you pressed the button on floor #", requestedFloor, "and you are going ", direction)
        time.sleep(1)
        bestElevator = self.findBestElevator(requestedFloor, direction)
        print("the best elevator for you is the #", bestElevator, floorlist)
        time.sleep(1)
        
        
        

