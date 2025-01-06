// BOJ_2512
// 예산

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const arr = inputArr[1]
    .split(' ')
    .map(Number)
    .sort((a, b) => a - b);
  const m = Number(inputArr[2]);

  const sumArr = arr.reduce((acc, val, idx) => {
    if (idx === 0) {
      acc.push(val);
    } else {
      acc.push(val + acc[idx - 1]);
    }
    return acc;
  }, []);

  const lowerBound = (target) => {
    let left = 0;
    let right = n;

    while (left < right) {
      const mid = Math.floor((left + right) / 2);
      if (arr[mid] < target) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }

    return left;
  };

  const calc = (target) => {
    const idx = lowerBound(target);
    if (idx === 0) {
      return n * target;
    }
    if (idx === n) {
      return sumArr[n - 1];
    }
    return sumArr[idx - 1] + (n - idx) * target;
  };

  let left = 1;
  let right = arr[n - 1];

  while (left < right) {
    const mid = Math.floor((left + right + 1) / 2);

    if (calc(mid) > m) {
      right = mid - 1;
    } else {
      left = mid;
    }
  }

  return left;
}

console.log(solution(input));
