var readline = require('readline')

var calcFib = (x) => x < 2 ? x : (() => {
  var fibNumbers = [0, 1]
  for (let i = 2; i <= x; i++) {
    fibNumbers.push(fibNumbers[i - 1] + fibNumbers[i - 2])
  }
  return fibNumbers[x]
})()

var rl = readline.createInterface({
  input: process.stdin,
  terminal: false
})

rl.on('line', (num) => {
  console.log(calcFib(parseInt(num.trim(), 10)))
  process.exit()
})
