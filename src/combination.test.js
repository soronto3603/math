const combination = require('./combination');

test('combination 4 c 2', () => {
  expect(combination(4, 2)).toStrictEqual([[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]])
  expect(combination(5, 3)).toStrictEqual([ [ 0, 1, 2 ],
    [ 0, 1, 3 ],
    [ 0, 1, 4 ],
    [ 0, 2, 3 ],
    [ 0, 2, 4 ],
    [ 0, 3, 4 ],
    [ 1, 2, 3 ],
    [ 1, 2, 4 ],
    [ 1, 3, 4 ],
    [ 2, 3, 4 ] ])
  expect(combination(2, 1)).toStrictEqual([ [ 0 ], [ 1 ] ])
})