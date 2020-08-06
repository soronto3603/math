const { combination } = require('./combination')

function bernstein(v, n) {
  return function (x) {
    return combination(5, 2) * Math.pow(x, v) * Math.pow(1 - x, n - v)
  }
}
