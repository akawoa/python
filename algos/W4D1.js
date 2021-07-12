/*
    Generate Coin Change

    Given a number of U.S. cents, return an object with the optimal 
    configuration of coins.

    EXAMPLE:

    var input = 173;
    var output = {
        quarters: 6,
        dimes: 2,
        nickels: 0,
        pennies: 3
    }

    A couple of different approaches:

    Option 1: Keep decrementing by the highest coin value possible, adding to that 
    key value pair each time, making your way down the hierarchy of coins

    Option 2: Our old friend modulo (i.e. the % operator)

    Modulo example:
    42 % 25 would give us 17, because 25 x 1 is 25, and there's 17 left to get us to 42

    Because (6 x 25) + (2 x 10) + (0 x 5) + (3 x 1) 
    is 150 + 20 + 0 + 3 = 173.
*/



// console.log(173 % 25);
// console.log((173 - 23) / 25)
// console.log(23 % 10)
// console.log((23-3) / 10)
// console.log(3 % 1)

var input = 173;

function generateCoinChangeObject(cents) {
    var output = {
        quarters: 0,
        dimes: 0,
        nickels: 0,
        pennies: 0
    }

    if (cents >= 25) {
        var count = (cents - (cents % 25)) / 25
        cents -= (count * 25)
        output["quarters"] = count
    }
    if (cents >= 10) {
        var count = (cents - (cents % 10)) / 10
        cents -= (count * 10)
        output["dimes"] = count
    }
    if (cents >= 5) {
        var count = (cents - (cents % 5)) / 5
        cents -= (count * 5)
        output["nickels"] = count
    }
    if (cents >= 1) {
        output["pennies"] = cents
    }    
    return output
}

console.log(generateCoinChangeObject(input))

