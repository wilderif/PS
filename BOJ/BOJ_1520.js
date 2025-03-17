// BOJ_1520
// 내리막 길

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const [n, m] = inputArr[0].split(' ').map(Number);
  const board = inputArr.slice(1).map((el) => el.split(' ').map(Number));
  const dp = Array.from({ length: n }, () => new Array(m).fill(-1));

  dp[n - 1][m - 1] = 1;

  const dfs = (coord) => {
    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];

    if (dp[coord[0]][coord[1]] !== -1) {
      return dp[coord[0]][coord[1]];
    }

    let ret = 0;

    for (let d = 0; d < 4; d++) {
      const nx = coord[0] + dx[d];
      const ny = coord[1] + dy[d];

      if (!(0 <= nx && nx < n && 0 <= ny && ny < m)) {
        continue;
      }
      if (board[nx][ny] >= board[coord[0]][coord[1]]) {
        continue;
      }

      ret += dfs([nx, ny]);
    }

    dp[coord[0]][coord[1]] = ret;
    return ret;
  };

  return dfs([0, 0]);
}

console.log(solution(input));
