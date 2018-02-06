var readline = require('readline')

var rl = readline.createInterface({input: process.stdin, terminal: false})

rl.on('line', (line) => {
  var sumOfTwo = line.trim()
            .split(' ')
            .map(num => parseInt(num, 10))
            .reduce((acc, val) => acc + val, 0)

  console.log(sumOfTwo)
  process.exit()
})
