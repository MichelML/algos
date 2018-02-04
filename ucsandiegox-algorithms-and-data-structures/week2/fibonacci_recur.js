const readline = require('readline')

const calcFib = (x) => x < 2 ? x : calcFib(x - 1) + calcFib(x - 2)

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

rl.question('Enter a small number: ', (num) => {
  console.log(calcFib(parseInt(num, 10)))
  rl.close()
})
