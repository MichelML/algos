const treeLength = (array = []) => {
  if (array.length === 0) {
    return 0
  }

  const counts = []
  const childrenRegistry = {}

  for (let i = 0; i < array.length; i++) {
    let child = i
    let count = 0

    while (child !== -1) {
      count += 1

      if (childrenRegistry[child] === undefined || childrenRegistry[child] < count) {
        childrenRegistry[child] = count
        child = array[child]
      } else {
        child = -1
        count = undefined
      }
    }

    if (count !== undefined) {
      counts.push(count)
    }
  }

  return Math.max(...counts)
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
        .map((val) => + val)
      console.log(treeLength(nodes))
      process.exit()
    }
  })
