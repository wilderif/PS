// BOJ_20291
// 파일 정리

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const map = new Map();
  for (const s of inputArr.slice(1)) {
    const ext = s.split('.')[1];
    map.set(ext, (map.get(ext) || 0) + 1);
  }

  const mapArray = Array.from(map)
    .sort()
    .map((el) => {
      return el.join(' ');
    });

  return mapArray.join('\n');
}

console.log(solution(input));
