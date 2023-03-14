#!/usr/bin/node

function esrever (list) {
	if (list === undefined) return;
	if (list === null) return;
  const size = list.length / 2;
  for (let i = 0, j = list.length - 1; i <= size; ++i, --j) {
    let temp = null;
    temp = list[i];
    list[i] = list[j];
    list[j] = temp;
  }
  return list;
}

module.exports = { esrever };
