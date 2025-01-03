// BOJ_9417
// 최대 GCD

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const resArr = [];

  for (let i = 0; i < n; i++) {
    const arr = inputArr[i + 1].split(' ').map(Number);
    let res = 0;
    for (let j = 0; j < arr.length; j++) {
      for (let k = j + 1; k < arr.length; k++) {
        let tmp = gdc(Math.abs(arr[j]), Math.abs(arr[k]));
        res = Math.max(res, tmp);
      }
    }

    resArr.push(res);
  }

  return resArr.join('\n');
}

function gdc(a, b) {
  if (b === 0) {
    return a;
  }
  return gdc(b, a % b);
}

console.log(solution(input));
