// BOJ_1365
// 꼬인 전깃줄

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const arr = inputArr[1].split(' ').map(Number);

  const binarySearch = (array, target) => {
    let left = 0;
    let right = array.length;

    while (left < right) {
      const mid = Math.floor((left + right) / 2);
      if (array[mid] > target) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }

    return left;
  };

  const mem = [];
  for (const el of arr) {
    if (el > mem[mem.length - 1]) {
      mem.push(el);
    } else {
      mem[binarySearch(mem, el)] = el;
    }
  }

  return n - mem.length;
}

console.log(solution(input));
