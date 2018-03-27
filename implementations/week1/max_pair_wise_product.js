const readline = require('readline')
const rl = readline.createInterface({input: process.stdin, terminal: false})
const collator = new Intl.Collator(undefined, {numeric: true, sensitivity: 'base'})

let inputCount = 0
let arrLength = 0
rl.on('line', (line) => {
  inputCount += 1
  if (inputCount === 1) {
    arrLength = parseInt(line, 10)
  } else if (inputCount === 2) {
    const sortedArray = line.trim()
      .split(' ')
      .sort(collator.compare)

    console.log(
      parseInt(sortedArray[arrLength - 1], 10) * parseInt(sortedArray[arrLength - 2], 10)
    )
    process.exit()
  }
})
