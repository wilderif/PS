// BOJ_2961
// 도영이가 만든 맛있는 음식

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const arr = inputArr.slice(1).map((el) => el.split(' ').map(Number));

  let res = Infinity;
  for (let i = 1; i < 2 ** n; i++) {
    let tmpS = 1;
    let tmpB = 0;
    for (let j = 0; j < n; j++) {
      if (i & (1 << j)) {
        tmpS *= arr[j][0];
        tmpB += arr[j][1];
      }
    }
    res = Math.min(res, Math.abs(tmpS - tmpB));
  }

  return res;
}

console.log(solution(input));
