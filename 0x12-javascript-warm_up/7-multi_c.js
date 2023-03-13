#!/usr/bin/node
const itr = Number(process.argv[2]);
if (isNaN(itr)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < itr; i++) {
    console.log('C is fun');
  }
}
