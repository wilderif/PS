// BOJ_1915
// 가장 큰 정사각형

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const [n, m] = inputArr[0].split(' ').map(Number);
  const board = inputArr.slice(1).map((el) => el.split('').map(Number));

  const check = (x, y) => {
    const dx = [-1, -1, 0];
    const dy = [-1, 0, -1];

    if (!(1 <= x && x < n && 1 <= y && y < m)) {
      return 1;
    }

    let tmp = Infinity;
    for (let d = 0; d < 3; d++) {
      const nx = x + dx[d];
      const ny = y + dy[d];

      if (board[nx][ny] === 0) {
        return 1;
      }

      tmp = Math.min(tmp, board[nx][ny]);
    }

    return tmp + 1;
  };

  let res = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (board[i][j]) {
        board[i][j] = check(i, j);
      }
      res = Math.max(res, board[i][j]);
    }
  }

  return res * res;
}

console.log(solution(input));
