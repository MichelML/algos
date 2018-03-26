const openSymbols = {
  '[': true,
  '{': true,
  '(': true
}

const closeSymbols = {
  ']': '[',
  '}': '{',
  ')': '('
}

const checkBrackets = (str) => {
  const openedSymbols = []
  for (let i = 0; i < str.length; i++) {
    if (openSymbols[str[i]]) {
      openedSymbols.push([str[i], i])
    } else if (closeSymbols[str[i]] !== undefined) {
      const lastOpened = openedSymbols[openedSymbols.length - 1];

      if (lastOpened && lastOpened[0] === closeSymbols[str[i]]) {
        openedSymbols.pop()
      } else {
        return i + 1;
      }
    }
  }

  return openedSymbols.length
    ? openedSymbols[0][1] + 1
    : 'Success';
}

require('readline')
  .createInterface({input: process.stdin, terminal: false})
  .on('line', (line) => {
    var stringOfBrackets = line.trim()
    console.log(checkBrackets(stringOfBrackets))
    process.exit()
  })
