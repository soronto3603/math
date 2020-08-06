function factorial(n) {
  return new Array(n - 1).fill(null).map((_, index) => index + 2).reduce((result, value) => result * value)
}

module.exports = factorial
