// source https://en.wikipedia.org/wiki/Least_common_multiple
let gcd = (a, b) => {
  let biggest = a >= b ? a : b
  let smallest = a < b ? a : b
  return smallest === 0
    ? biggest
    : gcd(smallest, biggest % smallest)
}

let leastCommonMultiple = (a, b) => {
  return (a * b) / gcd(a, b)
}

let rl = require('readline').createInterface({
  input: process.stdin,
  terminal: false
})

rl.on('line', (numbers) => {
  let twoNumbers = numbers.split(' ').map((num) => parseInt(num, 10))
  console.log(leastCommonMultiple(twoNumbers[0], twoNumbers[1]))
  process.exit()
})
