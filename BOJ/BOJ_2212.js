// BOJ_2212
// 센서

const fs = require('fs');
// const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
// const input = fs.readFileSync(filePath).toString().trim().split('\n');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const N = Number(inputArr[0]);
  const K = Number(inputArr[1]);
  if (K > N) {
    return 0;
  }
  const arr = inputArr[2]
    .split(' ')
    .map(Number)
    .sort((a, b) => a - b);

  const dist = new Array(N - 1).fill(0);
  for (let i = 0; i < N - 1; i++) {
    dist[i] = arr[i + 1] - arr[i];
  }
  dist.sort((a, b) => b - a);

  let tmp = 0;
  for (let i = 0; i < K - 1; i++) {
    tmp += dist[i];
  }

  return arr[N - 1] - arr[0] - tmp;
}

console.log(solution(input));
