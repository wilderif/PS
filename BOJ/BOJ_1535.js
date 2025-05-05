// BOJ_1535
// 안녕

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function main(inputArr) {
  const n = Number(inputArr[0]);
  const lArr = inputArr[1].split(' ').map(Number);
  const jArr = inputArr[2].split(' ').map(Number);

  const dp = new Array(101).fill(0);

  for (let i = 0; i < n; i++) {
    for (let j = 100; j > lArr[i]; j--) {
      dp[j] = Math.max(dp[j - lArr[i]] + jArr[i], dp[j]);
    }
  }

  return Math.max(...dp);
}

console.log(main(input));
