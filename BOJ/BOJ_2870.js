// BOJ_2870
// 수학숙제

const fs = require('fs');
// const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
// const input = fs.readFileSync(filePath).toString().trim().split('\n');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const sArr = [];
  for (let i = 1; i < n + 1; i++) {
    sArr.push(inputArr[i].split(''));
  }
  const res = [];
  for (const s of sArr) {
    let tmp = '';
    for (let i = 0; i < s.length; i++) {
      if (isNaN(s[i])) {
        if (tmp.length) {
          res.push(tmp);
          tmp = '';
        }
      } else {
        tmp += s[i];
      }
    }
    if (tmp.length) {
      res.push(tmp);
      tmp = '';
    }
  }

  return res
    .sort((a, b) => Number(a) - Number(b))
    .map((el) => {
      if (el.length > 1 && el[0] === '0') {
        let tmp = 0;
        for (let i = 0; i < el.length; i++) {
          if (el[i] !== '0') {
            tmp = i;
            break;
          }
        }
        if (tmp === 0) {
          return '0';
        }
        return el.split('').slice(tmp).join('');
      }
      return el;
    })
    .join('\n');
}

console.log(solution(input));
