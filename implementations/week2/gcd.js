let readline = require('readline')

let gcd = (a, b) => {
  let biggest = a >= b ? a : b
  let smallest = a < b ? a : b
  return smallest === 0
    ? biggest
    : gcd(smallest, biggest % smallest)
}

let rl = readline.createInterface({
  input: process.stdin,
  terminal: false
})

rl.on('line', (numbers) => {
  let twoNumbers = numbers.split(' ').map((num) => parseInt(num, 10))
  console.log(gcd(twoNumbers[0], twoNumbers[1]))
  process.exit()
})
