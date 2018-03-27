let readline = require('readline')

let calcFib = (x) => x < 2 ? x : (() => {
  let fibNumbers = [0, 1]
  for (let i = 2; i <= x; i++) {
    fibNumbers.push(fibNumbers[i - 1] + fibNumbers[i - 2])
  }
  return fibNumbers[x]
})()

let rl = readline.createInterface({
  input: process.stdin,
  terminal: false
})

rl.on('line', (num) => {
  console.log(calcFib(parseInt(num.trim(), 10)))
  process.exit()
})
