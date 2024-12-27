// BOJ_9663
// N-Queen

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

function solution(inputArr) {
  const n = Number(inputArr[0]);

  const arr = new Array(n).fill(-1);
  const used = new Array(n).fill(false);
  let res = 0;

  const check = (col, row) => {
    for (let i = 0; i < col; i++) {
      const tmpCol = i;
      const tmpRow = arr[i];
      const slope = (tmpRow - row) / (tmpCol - col);
      if (slope === 1 || slope === -1) {
        return false;
      }
    }
    return true;
  };

  const backTracking = (idx) => {
    if (idx === n) {
      res++;
      return;
    }

    for (let i = 0; i < n; i++) {
      if (used[i]) {
        continue;
      }
      if (check(idx, i)) {
        arr[idx] = i;
        used[i] = true;
        backTracking(idx + 1);
        used[i] = false;
      }
    }
  };

  backTracking(0);

  return res;
}

console.log(solution(input));
