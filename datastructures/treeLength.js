const treeLength = (array = []) => {
  return array.reduce((acc, val) => {
    acc[val] = !acc[val]
      ? 1
      : acc[val] + 1

    if (acc[val] >= 2) {
      acc.COUNT -= 1
    }

    return acc
  }, {COUNT: array.length}).COUNT
}

let lineCount = 0
require('readline')
  .createInterface({input: process.stdin, terminal: false})
  .on('line', (line) => {
    lineCount += 1

    if (lineCount === 2) {
      const nodes = line
        .trim()
        .split(' ')
      console.log(treeLength(nodes))
      process.exit()
    }
  })
