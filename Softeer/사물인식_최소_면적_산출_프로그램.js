// 사물인식_최소_면적_산출_프로그램

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const inputArr = [];

rl.on('line', (line) => {
  inputArr.push(line);
});

rl.on('close', () => {
  console.log(solution(inputArr));
  process.exit(0);
});

function solution(inputArr) {
  const [n, k] = inputArr[0].split(' ').map(Number);
  const arr = Array.from({ length: k + 1 }, () => []);

  for (const el of inputArr.slice(1)) {
    const [a, b, c] = el.split(' ').map(Number);
    arr[c].push([a, b]);
  }

  let res = 2000 * 2000;

  const backtracking = (color, minX, minY, maxX, maxY) => {
    if (color === k + 1) {
      res = (maxX - minX) * (maxY - minY);
      return;
    }

    for (const [x, y] of arr[color]) {
      const newMinX = Math.min(minX, x);
      const newMinY = Math.min(minY, y);
      const newMaxX = Math.max(maxX, x);
      const newMaxY = Math.max(maxY, y);

      if ((newMaxX - newMinX) * (newMaxY - newMinY) >= res) {
        continue;
      }

      backtracking(color + 1, newMinX, newMinY, newMaxX, newMaxY);
    }
  };

  backtracking(1, 1001, 1001, -1001, -1001);

  return res;
}
