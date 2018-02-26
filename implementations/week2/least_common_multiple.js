// source https://en.wikipedia.org/wiki/Least_common_multiple
var gcd = (a, b) => {
  var biggest = a >= b ? a : b
  var smallest = a < b ? a : b
  return smallest === 0
      ? biggest
      : gcd(smallest, biggest % smallest)
}

var leastCommonMultiple = (a, b) => {
  return (a * b) / gcd(a, b)
}

var rl = require('readline').createInterface({
  input: process.stdin,
  terminal: false
})

rl.on('line', (numbers) => {
  var twoNumbers = numbers.split(' ').map((num) => parseInt(num, 10))
  console.log(leastCommonMultiple(twoNumbers[0], twoNumbers[1]))
  process.exit()
})
