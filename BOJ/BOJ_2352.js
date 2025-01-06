// BOJ_2352
// 반도체 설계

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
      if (array[mid] <= target) {
        left = mid + 1;
      } else {
        right = mid;
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

  return mem.length;
}

console.log(solution(input));
