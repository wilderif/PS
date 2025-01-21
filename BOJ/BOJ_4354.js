// BOJ_4354
// 문자열 제곱

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const arr = inputArr.slice(0, -1);
  const res = [];

  for (const s of arr) {
    const lps = failure(s);
    const tmp = s.length - lps[s.length - 1];
    if (s.length % tmp) {
      res.push(1);
    } else {
      res.push(s.length / (s.length - lps[s.length - 1]));
    }
  }

  return res.join('\n');
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
