function comparator (a, b) {
  const comp1 = parseInt(a + b, 10)
  const comp2 = parseInt(b + a, 10)

  if (comp1 === comp2) { return 0 }

  return comp1 > comp2
    ? -1
    : 1
}

function getLargestNumber (arrayOfStringNumber) {
  return arrayOfStringNumber.sort(comparator).join('')
}

let rl = require('readline').createInterface({input: process.stdin, terminal: false})

let count = 0
rl.on('line', (num) => {
  count += 1

  if (count === 2) {
    console.log(getLargestNumber(num.trim().split(' ')))
    process.exit()
  }
})
