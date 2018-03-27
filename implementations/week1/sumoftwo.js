const readline = require('readline')

const rl = readline.createInterface({input: process.stdin, terminal: false})

rl.on('line', (line) => {
  const sumOfTwo = line.trim()
    .split(' ')
    .map((num) => parseInt(num, 10))
    .reduce((acc, val) => acc + val, 0)

  console.log(sumOfTwo)
  process.exit()
})
