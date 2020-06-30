package main

import (
	"fmt"
	"math"
	"math/rand"
	"sort"
)

//BATTERY

//ALL WE NEED IN OUR BATTERY RIGHT HERE

type Battery struct {
	nbColumn			int
	nbElevator			int
	nbFloor				int
	columnList			[]columnList
	bestColumn			Column
	bestElevator		Elevator
	floorNumber			int
	requestedFloor		int
	floorPerColumn		int
	requestFloorBtnList	[]RequestFloorBtn //one button for every floor on the panel in the lobby
	callBtnList			[]CallBtn	
}

//1st method
func (b *Battery) requestElevator(floorNumber int, requestedFloor int) Elevator {
	fmt.Println("Request an elevator")
	fmt.Println("You are on floor #", floorNumber)
	fmt.Println("You are going on floor #", requestedFloor)

	bestColumn := b.findBestColumn(floorNumber, requestedFloor)  //Column finder
	fmt.Println("The appropriate column for you will be the #", (bestColumn.id)+1)

	bestElevator := bestColumn.findBestElevator(floorNumber)   	//Then we get the best elevator
	fmt.Println("You are taking the elevator #", (bestElevator.elevatorNbr)+1)

	bestElevator.addFloorToFloorList(floorNumber) // Adding the current floor to the queue
	fmt.Println("Here is the elevator queue", bestElevator.floorList)

	bestElevator.moveElevator()	//best elevator coming to pick the user up
	fmt.Println("Your elevator has arrived, welcome aboard")

	return bestElevator

}

//2nd method
func (b *Battery) requestFloor(floorNumber int, requestedFloor int) {
	bestElevator := b.requestElevator(floorNumber, requestedFloor)
	bestElevator.addFloorToFloorList(requestedFloor)
	bestElevator.moveElevator()
	fmt.Println("Destination reached")
	}

func (b *Battery) construcColumn(){
	floorPerColumn := int(math.Ceil(float64(b.nbFloor / b.nbColumn)))

	for i := 0; i < b.nbColumn; i++ {
		bottomRange := (floorPerColumn*i + 1) + 1 //2,23,44,65
		topRange := (floorPerColumn * (i+1)) + 1 //22,43,64,85

		b.columnList = append(b.columnList, Column{i, b.nbElevator, b.nbFloor, bottomRange, topRange, nil, nil})
	}

	for j := 0; j < b.nbColumn; j++ {
		b.columnList[j].constructElevator()
	}
	b.constructRequestFloorBtn()	//Panel buttons
	b.constructCallBtn()			//Call buttons per floor
}

func (b *Battery) constructRequestFloorBtn() {
	for a := 2; a <= (b.nbFloor + 1); a++ {
		b.requestFloorBtnList = append(b.requestFloorBtnList, RequestFloorBtn{a})
	}
}

func (b *Battery) constructCallBtn() {
	for z := 2; z <= (b.nbFloor + 1); z++ {
		b.callBtnList = append(b.callBtnList, CallBtn{z, "down"})
	}
}

//FINDING THE BEST COLUMN
func (b *Battery) findBestColumn(floorNumber int, requestedFloor int) Column {
	
	if floorNumber == 1 {
		for k := 0; k < b.nbColumn; k++ {
			if requestedFloor >= b.columnList[k].bottomRange && requestedFloor <= b.columnList[k].topRange{
				b.bestColumn = b.columnList[k]
			}
		}
	
	} else {
		for l := 0; 1 < b.nbColumn; 1++ {
			if floorNumber >= b.nbcolumnList[l].bottomRange && floorNumber <= b.columnList[l].topRange {
				b.bestColumn = b.columnList[l]
		}
	}
	return b.bestColumn
}

//COLUMN SECTION

type Column struct {
	id 				int
	nbElevator		int
	elevatorList	[]Elevator	
}

func (c * Column) findBestElevator(floorNumber int) Elevator {		//scenario1
	floorDifference1 := []int{}
	bestElevator := c.elevatorList[0]
	if floorNumber == 1 {
		for m := 0; m < len(c.elevatorList); m++ {
			if c.elevatorList[m].position == 1 {
				floorDifference := int(math.Abs(float64(c.elevatorList[m].position-floorNumber))) + 1000
				floorDifference1 = append(floorDifference1, floorDifference)
			}
			if c.elevatorList[m].status == "moveDown" {
				floorDifference := int(math.Abs(float64(c.elevatorList[m].position-floorNumber))) + 2000
				floorDifference1 = append(floorDifference1, floorDifference)
			}
			if c.elevatorList[m].status == "idle" {
				floorDifference := int(math.Abs(float64(c.elevatorList[m].position-floorNumber))) + 3000
				floorDifference1 = append(floorDifference1, floorDifference)
			}
			if c.elevatorList[m].status == "moveUp" {
				floorDifference := int(math.Abs(float64(c.elevatorList[m].position-floorNumber))) + 4000
				floorDifference1 = append(floorDifference1, floorDifference)
			}
		}
		bestScore := 10000	//lowest score will be the elevator sent
		bestScoreIndex := 0
		for n := 0; n < len(floorDifference1); n++ {
			if bestScore > floorDifference1[n] {
				bestScore = floorDifference1[n]
				bestScoreIndex = n
			}
		}
		bestElevator = c.elevatorList[bestScoreIndex]

	}	else {				//scenario2
			for o := 0; o < len(c.elevatorList); o++ {
				if c.elevatorList[o].status == "moveDown" && c.elevatorList[o].position > floorNumber {
					floorDifference := int(math.Abs(float64(c.elevatorList[o].position-floorNumber))) + 1000
					floorDifference1 = append(floorDifference1, floorDifference)
				}
				if c.elevatorList[m].status == "idle" {
					floorDifference := int(math.Abs(float64(c.elevatorList[o].position-floorNumber))) + 2000
					floorDifference1 = append(floorDifference1, floorDifference)
				}
				if c.elevatorList[m].status == "moveUp" {
					floorDifference := int(math.Abs(float64(c.elevatorList[o].position-floorNumber))) + 3000
					floorDifference1 = append(floorDifference1, floorDifference)
				}
			}
			bestScore := 10000 //lowest score will be the elevator sent
			bestScoreIndex := 0
			for n := 0; n < len(floorDifference1); n++ {
				if bestScore > floorDifference1[n] {
					bestScore = floorDifference1[n]
					bestScoreIndex = n
			}
			bestElevator = c.elevatorList[bestScoreIndex]
	}





