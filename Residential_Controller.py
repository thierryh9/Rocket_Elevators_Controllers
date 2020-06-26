

#LET'S GET YOU TO YOUR FLOOR!
import time
from random import randrange
#BASE SETTINGS OF OUR BUILDING
class Controller : 
    def __init__(self, nbColumn, nbElevator, nbFloor):
        self.nbColumn = nbColumn
        self.nbElevator = nbElevator
        self.nbFloor = nbFloor
        self.column = Column(nbElevator, nbFloor)
        
#COLUMN WITH ELEVATOR FIND AND REQUEST FUNCTIONS      
class Column : 
    def __init__(self, nbElevator, nbFloor):
    
        self.nbElevator = nbElevator
        self.callBtnNbr = nbFloor * 2 - 2
        self.elevatorList = []
        self.callBtnList = []
        self.nbFloor = nbFloor
        self.bestElevator = None
        self.state = "on"

        i= 0
        while i < self.nbElevator:
            self.elevatorList.append(Elevator(i, nbFloor)) 
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
                    bestElevator = elevator

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
        return bestElevator

    def RequestElevator(self, requestedFloor, direction):
        print("Request an elevator")
        time.sleep(1)
        print("you pressed the button on floor #", requestedFloor, "and you are going ", direction)
        time.sleep(1)
        bestElevator = self.findBestElevator(requestedFloor, direction)
        print("the best elevator for you is the #", (self.elevatorList.index(bestElevator))+1)
        time.sleep(1)
        bestElevator.addFloorToQueue(requestedFloor)
        print("New Queue is", bestElevator.floorList)
        time.sleep(1)
        bestElevator.moveElevator()
        print("The elevator arrived")
        time.sleep(1)



#ELEVATOR SETTINGS (MOVEMENT, FLOOR REQUEST AND QUEUE)
class Elevator:
    def __init__(self, elevatorNbr, nbFloor):

        self.floorList = []
        self.intBtnList = []
        self.status = []
        self.status = "idle"
        self.state = "stop"
        self.position = 1
        self.door = Door()
        self.intDisplay = self.position
        self.extDisplay = self.position
        self.elevatorNbr = elevatorNbr
        self.nbFloor = nbFloor
        self.currentWeight = randrange(1800)

        k = 1
        while k <= self.nbFloor:

            self.intBtnList.append(intBtn(k))
            k += 1

    def addFloorToQueue(self, requestedFloor):
        if requestedFloor not in self.floorList:
            self.floorList.append(requestedFloor)
            print("The floor has been added to the queue", self.floorList)
            time.sleep(1)
            self.floorList.sort()
            print("The queue has been sorted", self.floorList)
            time.sleep(1)

    def moveElevator(self):
        while len(self.floorList) > 0 :
            if self.floorList[0] > self.position:
                self.moveEleUp()
            elif self.floorList[0] < self.position:
                self.moveEleDown()
            elif self.floorList[0] == self.position:
                del self.floorList[0]

    def moveEleDown(self):

        print("The elevator", (self.elevatorNbr + 1), "is at floor #", self.position)
        time.sleep(1)
        while self.position > self.floorList[len(self.floorList)-1]:

            self.position = self.position - 1 
            print("The elevator", (self.elevatorNbr + 1), "is at floor #", self.position)
            self.status = "moveDown"
            self.state = "move"
            time.sleep(1)

        self.state = "stop"
        self.door.openDoor()
        del self.floorList[len(self.floorList)-1]

    def moveEleUp(self):
        print("The elevator", (self.elevatorNbr + 1), "is at floor #", self.position)
        time.sleep(1)
        while self.position < self.floorList[0]:
            
            self.position = self.position + 1
            print("The elevator", (self.elevatorNbr + 1), "is on floor #", self.position)
            self.status = "moveUp"
            self.state = "move"
            time.sleep(1)

        self.status = "stop"
        self.door.openDoor()
        del self.floorList[0]

    def RequestFloor(self, elevator, requestedFloor):
        print("You pressed the button #", requestedFloor, "on the panel")
        time.sleep(1)
        elevator.addFloorToQueue(requestedFloor)
        print("The new floor list is", elevator.floorList)
        time.sleep(1)
        elevator.moveElevator()
        print("Destination reached")
        time.sleep(1)


#DOOR (OPENING AND CLOSING)
class Door:
    def __init__(self):
        self.state = "stop"
        self.obstruction = False
        self.alarm = False
        self.Door = True

        if  self.Door == "open":
            print("Door opened, closing in 5 sec")
            self.controlDoor("close")
        else:
            self.Door == "closed"
            print("Door closed")

    def openDoor(self):
        self.Door == "open"
        print("Elevator door is opening")
        print("Door opened, closing in 5 sec")
        
              
#BUTTONS OUTSIDE AND INSIDE THE ELEVATOR
class callBtn:
    def __init__ (self, currentFloor, direction):
        self.currentFloor = currentFloor
        self.direction = direction
        self.callbtnLight = "off"

class intBtn:
    def __init__ (self, requestedFloor):
        self.requestedFloor = requestedFloor
        self.intBtnLight = "off"

    
#TESTS

Controller = Controller (1, 2, 10)   #1 column, 2 elevators, 10 floors

Controller.column.elevatorList[0].position = 1
Controller.column.elevatorList[0].status = "moveUp"
Controller.column.elevatorList[0].floorList = []
Controller.column.elevatorList[1].position = 9
Controller.column.elevatorList[1].status = "moveDown"
Controller.column.elevatorList[1].floorList = []

#CALL FUNCTION

Controller.column.RequestElevator(10, "down")

Controller.column.bestElevator.RequestFloor(Controller.column.bestElevator, 4)



   
                
        
        

