// BOJ_16900
// 이름 정하기

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const [s, k] = inputArr[0]
    .split(' ')
    .map((val, idx) => (idx === 1 ? Number(val) : val));
  const sLen = s.length;

  const lps = failure(s);
  return sLen + (sLen - lps[sLen - 1]) * (k - 1);
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
