function combination(n, r) {
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

module.exports = combination;