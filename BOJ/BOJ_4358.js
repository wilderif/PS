// BOJ_4358
// 생태학

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const map = new Map();
  const total = inputArr.length;
  for (const s of inputArr) {
    map.set(s, (map.get(s) || 0) + 1);
  }

  const mapArray = Array.from(map)
    .sort()
    .map((el) => {
      return [el[0], ((el[1] / total) * 100).toFixed(4)].join(' ');
    });

  return mapArray.join('\n');
}

console.log(solution(input));
