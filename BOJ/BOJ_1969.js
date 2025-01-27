// BOJ_1969
// DNA

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const [n, m] = inputArr[0].split(' ').map(Number);
  const strArr = inputArr.slice(1);

  let resCnt = 0;
  const resStr = [];
  for (let i = 0; i < m; i++) {
    const cntMap = new Map();

    for (let j = 0; j < n; j++) {
      const curChar = strArr[j][i];
      cntMap.set(curChar, cntMap.get(curChar) ? cntMap.get(curChar) + 1 : 1);
    }

    const cntArr = Array.from(cntMap).sort((a, b) => {
      if (a[1] === b[1]) {
        return a[0] < b[0] ? -1 : 1;
      }
      return b[1] - a[1];
    });

    resStr.push(cntArr[0][0]);
    resCnt += n - cntArr[0][1];
  }

  const res = [resStr.join(''), resCnt];

  return res.join('\n');
}

console.log(solution(input));
