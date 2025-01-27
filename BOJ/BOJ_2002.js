// BOJ_2002
// 추월

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const n = Number(inputArr[0]);
  let line = 1;

  const inMap = new Map();
  const outMap = new Map();
  while (line <= n) {
    inMap.set(line, inputArr[line]);
    outMap.set(inputArr[line + n], line);
    line++;
  }

  let cnt = 0;
  let prev = 0;
  for (let i = 1; i <= n; i++) {
    const tmp = outMap.get(inMap.get(i));
    if (tmp > prev) {
      cnt++;
      prev = tmp;
    }
  }

  return n - cnt;
}

console.log(solution(input));
