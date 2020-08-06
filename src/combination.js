const factorial = require('./factorial')
// https://ko.wikipedia.org/wiki/%EC%A1%B0%ED%95%A9

function combinationList(n, r) {
  const result = []
  function fill(array) {
  	if (array.length === r) {
      result.push(array)
      return
    }

    const lastValue = array[array.length - 1]
    for (let i = lastValue + 1; i < n; i++) {
      fill([...array, i])
    }
  }

  for (let i = 0; i < n ; i++) {
    fill([i])
  }
  return result
}

function combination(n, k) {
  return factorial(n) / (factorial(k) * factorial(n - k))
}

module.exports = {
  combination,
  combinationList,
}
