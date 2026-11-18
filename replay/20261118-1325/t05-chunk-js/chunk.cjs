'use strict';

function chunk(items, size) {
  if (!Number.isInteger(size) || size < 1) {
    throw new RangeError('size must be a whole number of at least 1');
  }

  const result = [];
  for (let i = 0; i < items.length; i += size) {
    result.push(items.slice(i, i + size));
  }
  return result;
}

module.exports = { chunk };
