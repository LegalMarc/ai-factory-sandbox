const { test } = require("node:test");
const assert = require("node:assert");
const { chunk } = require("./chunk.cjs");

test("chunks array into pieces of given size", () => {
  assert.deepStrictEqual(chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]]);
});

test("empty array returns empty array", () => {
  assert.deepStrictEqual(chunk([], 3), []);
});

test("does not mutate input and returns new arrays", () => {
  const a = [1, 2, 3, 4];
  const result = chunk(a, 2);
  assert.deepStrictEqual(a, [1, 2, 3, 4]);
  assert.deepStrictEqual(result, [[1, 2], [3, 4]]);
  assert.notStrictEqual(result[0], a);
  result[0].push(99);
  assert.deepStrictEqual(a, [1, 2, 3, 4]);
});

test("size larger than array returns single chunk", () => {
  assert.deepStrictEqual(chunk([1, 2], 5), [[1, 2]]);
});

test("invalid size throws RangeError", () => {
  const a = [1, 2, 3];
  for (const bad of [0, -1, 1.5, "2", undefined]) {
    assert.throws(() => chunk(a, bad), RangeError);
  }
});
