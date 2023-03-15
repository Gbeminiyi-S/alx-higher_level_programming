#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;
  let temp;
  for (let i = 0; i < Math.floor(len / 2); i++) {
    temp = list[i];
    list[i] = list[len - i - 1];
    list[len - i - 1] = temp;
  }
  return list;
};
