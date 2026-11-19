const test = require("node:test");
const assert = require("node:assert");
const { chunk } = require("./chunk.cjs");

test("splits an array into pieces with a shorter last piece", () => {
  assert.deepStrictEqual(chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]]);
});

test("returns an empty array for an empty input", () => {
  assert.deepStrictEqual(chunk([], 3), []);
});

test("returns the whole array as one piece when size exceeds length", () => {
  assert.deepStrictEqual(chunk([1, 2], 5), [[1, 2]]);
});

test("does not mutate the input and returns new arrays", () => {
  const input = [1, 2, 3, 4, 5];
  const result = chunk(input, 2);
  assert.deepStrictEqual(input, [1, 2, 3, 4, 5]);
  assert.notStrictEqual(result, input);
  assert.notStrictEqual(result[0], input.slice(0, 2));
});

test("throws a RangeError for invalid sizes", () => {
  for (const bad of [0, -1, 1.5, "2", undefined]) {
    assert.throws(() => chunk([1, 2, 3], bad), RangeError);
  }
});
