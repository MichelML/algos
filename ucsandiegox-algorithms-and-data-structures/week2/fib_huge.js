// inspired from https://stackoverflow.com/a/14662102
// and https://stackoverflow.com/a/27205510
function multiplyMatrices(m1, m2) {
    var result = [];
    for (var i = 0; i < m1.length; i++) {
        result[i] = [];
        for (var j = 0; j < m2[0].length; j++) {
            var sum = 0;
            for (var k = 0; k < m1[0].length; k++) {
                sum += m1[i][k] * m2[k][j];
            }
            result[i][j] = sum;
        }
    }
    return result;
}

function huge_fib(nthFibonacci) {
    var base_case = [[1, 1], [1, 0]];
    var result = [[1, 1], [1, 0]];
    for (var i = 1; i < nthFibonacci; i++) {
        result = multiplyMatrices(result, base_case)
    }

    return result;
}

console.log(huge_fib(239)[0][1] % 1000)