package main

import (
	"fmt"
	"math/rand"
	"time"
)

// diceValues simulates rolling a specified number of dice with a given number of sides on each die.
func diceValues(numDice int, numSides int) int {
	sum := 0
	for d := 1; d <= numDice; d++ {
		// Initialize the random number generator with the current time's nanoseconds.
		rand.Seed(time.Now().UnixNano())
		// Generate a random value between 1 and numSides for each die.
		randomValue := rand.Intn(numSides) + 1
		fmt.Printf("Dice %d: %d\n", d, randomValue)
		sum += randomValue
	}
	return sum
}

func main() {
	numRolls := 2 // Number of times to roll the dice
	numDice := 3

	// The program simulates rolling the specified number of dice a specified number of times
	// and displays the results of each roll, including the total value rolled.
	for roll := 1; roll <= numRolls; roll++ {
		fmt.Println("Rolling:", roll)
		totalRoll := diceValues(numDice, 6) // Roll the dice and get the total
		fmt.Printf("The total rolled: %d\n", totalRoll)

		// Check for special cases based on the total rolled
		if totalRoll == 7 {
			fmt.Println("Lucky 7")
			if totalRoll%2 == 1 {
				fmt.Println("Odd")
			}
		} else if totalRoll == 2 && numDice == 2 {
			fmt.Println("Snake eyes (rolling two dice with a total of 2)")
		} else if totalRoll%2 == 0 {
			fmt.Println("Even")
		} else if totalRoll%2 == 1 {
			fmt.Println("Odd")
		}
	}
}
