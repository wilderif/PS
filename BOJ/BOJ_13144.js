// BOJ_13144
// List of Unique Numbers

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const arr = inputArr[1].split(' ').map(Number);

  const check = new Set();
  let p2 = 0;
  let res = 0;
  for (let p1 = 0; p1 < n; p1++) {
    while (p2 < n) {
      if (check.has(arr[p2])) {
        break;
      } else {
        check.add(arr[p2++]);
        res += p2 - p1;
      }
    }
    check.delete(arr[p1]);
  }

  return res;
}

console.log(solution(input));
