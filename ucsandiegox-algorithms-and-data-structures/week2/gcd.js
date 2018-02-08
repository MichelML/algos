var readline = require('readline')

var gcd = (a, b) => {
  var biggest = a >= b ? a : b
  var smallest = a < b ? a : b
  return smallest === 0
    ? biggest
    : gcd(smallest, biggest % smallest)
}

var rl = readline.createInterface({
  input: process.stdin,
  terminal: false
})

rl.on('line', (numbers) => {
  var twoNumbers = numbers.split(' ').map((num) => parseInt(num, 10))
  console.log(gcd(twoNumbers[0], twoNumbers[1]))
  process.exit()
})
