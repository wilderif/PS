// BOJ_2156
// 포도주 시식

const fs = require('fs');
// const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
// const input = fs.readFileSync(filePath).toString().trim().split('\n');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const arr = [];

  for (let i = 1; i <= n; i++) {
    arr.push(Number(inputArr[i]));
  }

  if (n === 1) {
    return arr[0];
  }
  if (n === 2) {
    return arr[0] + arr[1];
  }

  const mem = new Array(n);
  mem[0] = arr[0];
  mem[1] = arr[0] + arr[1];
  mem[2] = Math.max(arr[0] + arr[1], arr[0] + arr[2], arr[1] + arr[2]);
  for (let i = 3; i < n; i++) {
    mem[i] = Math.max(
      mem[i - 1],
      mem[i - 2] + arr[i],
      mem[i - 3] + arr[i - 1] + arr[i]
    );
  }

  return mem[n - 1];
}

console.log(solution(input));
