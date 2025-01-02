// BOJ_1449
// 수리공 항승

const fs = require('fs');
// const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
// const input = fs.readFileSync(filePath).toString().trim().split('\n');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const [N, L] = inputArr[0].split(' ').map(Number);
  const arr = inputArr[1]
    .split(' ')
    .map(Number)
    .sort((a, b) => a - b);
  let res = 0;
  let end = -1;
  for (let i = 0; i < N; i++) {
    if (arr[i] <= end) {
      continue;
    }
    res++;
    end = arr[i] + L - 1;
  }

  return res;
}

console.log(solution(input));
