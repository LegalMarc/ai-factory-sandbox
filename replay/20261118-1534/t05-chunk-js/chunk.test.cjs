const test = require('node:test');
const assert = require('node:assert');

const { chunk } = require('./chunk.cjs');

test('splits an array into pieces of the given size', () => {
  assert.deepStrictEqual(chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]]);
});

test('returns an empty array for an empty input', () => {
  assert.deepStrictEqual(chunk([], 3), []);
});

test('keeps a short final piece', () => {
  assert.deepStrictEqual(chunk([1, 2], 5), [[1, 2]]);
});

test('does not mutate the input and returns new arrays', () => {
  const input = [1, 2, 3, 4, 5];
  const result = chunk(input, 2);

  assert.deepStrictEqual(input, [1, 2, 3, 4, 5]);
  assert.notStrictEqual(result[0], input);
  result[0].push(99);
  assert.deepStrictEqual(input, [1, 2, 3, 4, 5]);
});

test('throws a RangeError for an invalid size', () => {
  for (const bad of [0, -1, 1.5, '2', undefined]) {
    assert.throws(() => chunk([1, 2, 3], bad), RangeError);
  }
});
