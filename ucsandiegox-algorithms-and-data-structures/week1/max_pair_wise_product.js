var readline = require('readline')

var rl = readline.createInterface({input: process.stdin, terminal: false})

var lineCount = 0
var arrayLength = 2
var sortedArrayOfPositiveIntegers = []

rl.on('line', (line) => {
  lineCount += 1
  if (lineCount === 1) {
    arrayLength = parseInt(line.trim(), 10)
  } else if (lineCount === 2) {
    sortedArrayOfPositiveIntegers = line.trim()
            .split(' ')
            .map(num => parseInt(num, 10))
            .sort((a, b) => a > b)

    var arrLength = sortedArrayOfPositiveIntegers.length
    console.log(sortedArrayOfPositiveIntegers[arrLength - 1] * sortedArrayOfPositiveIntegers[arrLength - 2])
    process.exit()
  }
})
