// BOJ_20922
// 겹치는 건 싫어

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const [n, k] = inputArr[0].split(' ').map(Number);
  const arr = inputArr[1].split(' ').map(Number);

  const check = {};
  let p2 = 0;
  let res = 0;
  for (let p1 = 0; p1 < n; p1++) {
    while (p2 < n) {
      if (check[arr[p2]] > 0) {
        if (check[arr[p2]] < k) {
          check[arr[p2++]]++;
        } else {
          break;
        }
      } else {
        check[arr[p2]] = 1;
        p2++;
      }
    }
    res = Math.max(res, p2 - p1);
    check[arr[p1]]--;
  }

  return res;
}

console.log(solution(input));
