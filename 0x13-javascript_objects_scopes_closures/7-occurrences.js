#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let total = 0;
  for (const i in list) {
    if (searchElement === list[i]) {
      total += 1;
    }
  }
  return (total);
};
