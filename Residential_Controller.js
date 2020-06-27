function testController() {
    var controller = init_elevator_system(10, 2);
  
    
  
        controller.column.elevatorList[0].currentFloor = 2; // set elevator 1 floor
        controller.column.elevatorList[0].status = "moveUp";
        controller.column.elevatorList[0].direction = "down";
        controller.column.elevatorList[1].currentFloor = 6; // set elevator 2 floor
        controller.column.elevatorList[1].status = "moveUp";
        controller.column.elevatorList[1].direction = "down";
  
        var elevator = controller.RequestElevator(5, "up");
        controller.RequestFloor(elevator, 7);
   
    //controller.column.elevatorList[0].currentFloor = 10;
    //controller.column.elevatorList[0].status = "moveUp";
    //controller.column.elevatorList[0].direction = "down";
    //controller.column.elevatorList[1].currentFloor = 3;
    //controller.column.elevatorList[1].status = "moveUp";
    //controller.column.elevatorList[1].direction = "down";
  
    var elevator = controller.RequestElevator(1, "up");
    controller.RequestFloor(elevator, 6);
    elevator = controller.RequestElevator(3, "up");
    controller.RequestFloor(elevator, 5);
    elevator = controller.RequestElevator(9, "down");
    controller.RequestFloor(elevator, 2);
    
  
    
  
     //controller.column.elevatorList[0].currentFloor = 10;
     //controller.column.elevatorList[0].status = "moveUp";
     //controller.column.elevatorList[0].direction = "down";
     //controller.column.elevatorList[1].currentFloor = 3;
     //controller.column.elevatorList[1].status = "moveUp";
     //controller.column.elevatorList[1].direction = "down";
  
     console.log(controller.column.elevatorList)
     var elevator = controller.RequestElevator(10, "down");
     controller.RequestFloor(elevator, 3);
  
     elevator = controller.RequestElevator(3, "down");
     controller.RequestFloor(elevator, 2);
       
  
  
    
  
          //BASE SETTINGS OF OUR BUILDING
  }
  function init_elevator_system(nbFloor, nbElevator) {
    var controller = new ElevatorController(nbFloor, nbElevator);
  
    return controller;
  }
          //COLUMN WITH ELEVATOR FIND AND REQUEST FUNCTIONS 
  class Column {
    constructor(nbFloor, nbElevator) {
      this.nbFloor = nbFloor;
      this.nbElevator = nbElevator;
      this.elevatorList = [];
      for (let i = 0; i < this.nbElevator; i++) {
        let elevator = new Elevator(i, "idle", 1, "up");
        this.elevatorList.push(elevator);
      }
    }
  }
  
  class Elevator {
    constructor(position, status, currentFloor, direction) {
      this.position = position;
      this.status = status;
      this.currentFloor = currentFloor;
      this.direction = direction;
      this.floorList = [];
    }
    //SEND THE REQUEST TO COMPUTE THE LIST
  
    QueueRequest(RequestedFloor) {
      this.floorList.push(RequestedFloor);
      this.sortedQueue();
      this.moveElevator(RequestedFloor);
    }
    //SORT QUEUE
  
    sortedQueue() {
      if (this.direction === "up") {
        this.floorList.sort();
      } else if (this.direction === "down") {
        this.floorList.sort();
        this.floorList.reverse();
      }
      return this.floorList;
    }
    //MOVING THE SYSTEM
  
    moveElevator(RequestedFloor) {
      while (this.floorList > 0) {
        
        if (RequestedFloor === this.currentFloor) {
          this.openDoor();
          this.status = "moveUp";
  
          this.floorList.shift();
        } else if (RequestedFloor < this.currentFloor) {
          this.status = "moveUp";
          console.log("---------------------------------------------------");
          console.log("Elevator" + this.position, this.status);
          console.log("---------------------------------------------------");
          this.Direction = "down";
          this.moveEleDown(RequestedFloor);
          this.status = "stopped";
          console.log("---------------------------------------------------");
          console.log("Elevator" + this.position, this.status);
          console.log("---------------------------------------------------");
          this.openDoor();
          this.floorList.shift();
        } else if (RequestedFloor > this.currentFloor) {
          sleep(1000);
          this.status = "moveUp";
          console.log("---------------------------------------------------");
          console.log("Elevator" + this.position, this.status);
          console.log("---------------------------------------------------");
          this.Direction = "up";
          this.moveEleUp(RequestedFloor);
          this.status = "stopped";
          console.log("---------------------------------------------------");
          console.log("Elevator" + this.position, this.status);
          console.log("---------------------------------------------------");
  
          this.openDoor();
  
          this.floorList.shift();
        }
      }
      if (this.floorList === 0) {
        this.status = "idle";
      }
    }
    Request_floor_button(RequestedFloor) {
      this.RequestedFloor = RequestedFloor;
      this.floor_light = floor_light;
    }
    Call_floor_button(FloorNumber, Direction) {
      this.FloorNumber = FloorNumber;
      this.Direction = Direction;
    }
    // open and close door
  
    openDoor() {
      sleep(1000);
      console.log("Open Door");
      console.log("---------------------------------------------------");
      sleep(1000);
  
      console.log("---------------------------------------------------");
      sleep(1000);
      this.closeDoor();
    }
    closeDoor() {
      console.log("close door");
      sleep(1000);
    }
  
    //MOVE THE ELEVATOR UP
  
    moveEleUp(RequestedFloor) {
      console.log("Floor : " + this.currentFloor);
      sleep(1000);
      while (this.currentFloor !== RequestedFloor) {
        this.currentFloor += 1;
        console.log("Floor : " + this.currentFloor);
  
        sleep(1000);
      }
    }
  
    moveEleDown(RequestedFloor) {
      console.log("Floor : " + this.currentFloor);
      sleep(1000);
      while (this.currentFloor !== RequestedFloor) {
        this.currentFloor -= 1;
        console.log("Floor : " + this.currentFloor);
  
        sleep(1000);
      }
    }
  }
  
  class ElevatorController {
    constructor(nbFloor, nbElevator) {
      this.nbFloor = nbFloor;
      this.nbElevator = nbElevator;
      this.column = new Column(nbFloor, nbElevator);
      // console.log(this.column);
  
      console.log("Controller iniatiated");
    }
  
    //REQUESTING THE BEST
  
    RequestElevator(FloorNumber, Direction) {
      sleep(1000);
      console.log("---------------------------------------------------");
      console.log("Request elevator to floor : ", FloorNumber);
      sleep(1000);
      console.log("---------------------------------------------------");
      console.log("Call Button Light On");
      sleep(1000);
  
      let elevator = this.findBestElevator(FloorNumber, Direction);
      elevator.QueueRequest(FloorNumber);
      return elevator;
    }
    //request floor
  
    RequestFloor(elevator, RequestedFloor) {
      sleep(1000);
      console.log("---------------------------------------------------");
      console.log("Requested floor : ", RequestedFloor);
      sleep(1000);
      console.log("---------------------------------------------------");
      console.log("Request Button Light On");
      sleep(1000);
      elevator.QueueRequest(RequestedFloor);
      // Elevator.moveElevator(RequestedFloor);
    }
    // here where the find best elevator is done
  
    findBestElevator(FloorNumber, Direction) {
      console.log("findBestElevator", FloorNumber, Direction);
  
      let bestElevator = null;
      let shortest_distance = 1000;
      for (let i = 0; i < this.column.elevatorList.length; i++) {
        let elevator = this.column.elevatorList[i];
  
        if (
          FloorNumber === elevator.currentFloor &&
          (elevator.status === "stopped" ||
            elevator.status === "idle" ||
            elevator.status === "moveUp")
        ) {
          return elevator;
        } else {
          let ref_distance = Math.abs(FloorNumber - elevator.currentFloor);
          if (shortest_distance > ref_distance) {
            shortest_distance = ref_distance;
            bestElevator = elevator;
  
            if (elevator.Direction === Direction) {
              bestElevator = elevator;
            }
          }
        }
      }
      return bestElevator;
    }
  }
  
  
  function sleep(milliseconds) {
    var start = new Date().getTime();
    for (var i = 0; i < 1e7; i++) {
      if (new Date().getTime() - start > milliseconds) {
        break;
      }
    }
  }

  