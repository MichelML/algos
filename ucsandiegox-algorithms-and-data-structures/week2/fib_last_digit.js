const fibLastDigit = (n) => {
  let first = 0
  let second = 1
  let res

  for (let i = 2; i <= n; i++) {
    res = (first + second) % 10
    first = second
    second = res
  }

  return res
}

var rl = require('readline').createInterface({
  input: process.stdin,
  terminal: false
})

rl.on('line', (num) => {
  console.log(fibLastDigit(parseInt(num.trim(), 10)))
  process.exit()
})
