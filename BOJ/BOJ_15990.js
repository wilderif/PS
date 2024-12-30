// BOJ_15990
// 1, 2, 3 더하기 5

const fs = require('fs');
// const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
// const input = fs.readFileSync(filePath).toString().trim().split('\n');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const t = Number(inputArr[0]);
  const arr = inputArr.slice(1).map(Number);
  const len = 100001;
  const mod = 1000000009;

  const mem1 = new Array(len).fill(0);
  const mem2 = new Array(len).fill(0);
  const mem3 = new Array(len).fill(0);
  mem1[1] = 1;
  mem2[2] = 1;
  mem1[3] = 1;
  mem2[3] = 1;
  mem3[3] = 1;
  for (let i = 4; i < len; i++) {
    mem1[i] = (mem2[i - 1] + mem3[i - 1]) % mod;
    mem2[i] = (mem1[i - 2] + mem3[i - 2]) % mod;
    mem3[i] = (mem1[i - 3] + mem2[i - 3]) % mod;
  }

  const res = [];
  for (const i of arr) {
    res.push((mem1[i] + mem2[i] + mem3[i]) % mod);
  }

  return res.join('\n');
}

console.log(solution(input));
