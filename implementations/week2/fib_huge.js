// inspired from https://stackoverflow.com/a/14662102
// and https://stackoverflow.com/a/27205510
function multiplyMatrices (m1, m2) {
  let result = []
  for (let i = 0; i < m1.length; i++) {
    result[i] = []
    for (let j = 0; j < m2[0].length; j++) {
      let sum = 0
      for (let k = 0; k < m1[0].length; k++) {
        sum += m1[i][k] * m2[k][j]
      }
      result[i][j] = sum
    }
  }
  return result
}

function hugeFib (nthFibonacci) {
  let baseCase = [[1, 1], [1, 0]]
  let result = [[1, 1], [1, 0]]
  for (let i = 1; i < nthFibonacci; i++) {
    result = multiplyMatrices(result, baseCase)
  }

  return result
}

console.log(hugeFib(239)[0][1] % 1000)
