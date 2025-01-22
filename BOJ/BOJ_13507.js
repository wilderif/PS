// BOJ_13507
// 좋은 부분 문자열의 개수

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const s = inputArr[0];
  const goodCharArray = inputArr[1].split('').map(Number);
  const k = Number(inputArr[2]);

  const checkGoodChar = (c) => {
    return goodCharArray[c.charCodeAt() - 'a'.charCodeAt()];
  };

  const check = new Set();
  for (let i = 0; i < s.length; i++) {
    let curWord = '';
    let badCnt = 0;
    for (let j = i; j < s.length; j++) {
      if (!checkGoodChar(s[j])) {
        badCnt++;
      }
      if (badCnt > k) {
        break;
      }

      curWord += s[j];
      check.add(curWord);
    }
  }

  return check.size;
}

console.log(solution(input));
