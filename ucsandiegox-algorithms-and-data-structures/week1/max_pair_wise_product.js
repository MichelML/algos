var readline = require('readline')

var rl = readline.createInterface({input: process.stdin, terminal: false})

rl.on('line', (line) => {
  var sortedArrayOfPositiveIntegers = line.trim()
            .split(' ')
            .map(num => parseInt(num, 10))
            .sort((a, b) => a > b)

  var arrLength = sortedArrayOfPositiveIntegers.length
  console.log(sortedArrayOfPositiveIntegers[arrLength - 1] * sortedArrayOfPositiveIntegers[arrLength - 2])
  process.exit()
})
