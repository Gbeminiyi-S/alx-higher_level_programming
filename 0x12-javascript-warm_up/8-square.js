#!/usr/bin/node
const itr = Number(process.argv[2]);

if (isNaN(itr)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < itr; i++) {
    let symbol = '';
    for (let i = 0; i < itr; i++) {
      symbol += 'X';
    }
    console.log(symbol);
  }
}
