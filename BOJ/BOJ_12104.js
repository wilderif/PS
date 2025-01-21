// BOJ_12104
// 순환 순열

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const a = inputArr[0] + inputArr[0];
  const b = inputArr[1];
  const lps = failure(b);

  let res = 0;
  let j = 0;
  for (let i = 0; i < a.length - 1; i++) {
    while (j > 0 && a[i] !== b[j]) {
      j = lps[j - 1];
    }
    if (a[i] === b[j]) {
      j++;
    }
    if (j === b.length) {
      res++;
    }
  }

  return res;
}

function failure(pattern) {
  const lps = new Array(pattern.length).fill(0);
  let j = 0;
  for (let i = 1; i < pattern.length; i++) {
    while (j > 0 && pattern[i] !== pattern[j]) {
      j = lps[j - 1];
    }
    if (pattern[i] === pattern[j]) {
      lps[i] = ++j;
    }
  }

  return lps;
}

console.log(solution(input));
