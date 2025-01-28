// 장애물_인식_프로그램

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const inputArr = [];

rl.on('line', (line) => {
  inputArr.push(line.trim());
});

rl.on('close', () => {
  console.log(solution(inputArr));
  process.exit(0);
});

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const board = [];
  for (const el of inputArr.slice(1)) {
    board.push(el.split('').map(Number));
  }

  const used = Array.from({ length: n }, () => new Array(n).fill(false));
  const res = [];

  const dfs = (start) => {
    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];

    const stack = [];
    stack.push(start);
    used[start[0]][start[1]] = true;
    let ret = 1;

    while (stack.length) {
      const cur = stack.pop();
      for (let d = 0; d < 4; d++) {
        const nx = cur[0] + dx[d];
        const ny = cur[1] + dy[d];

        if (0 <= nx && nx < n && 0 <= ny && ny < n) {
          if (board[nx][ny] === 0) {
            continue;
          }
          if (used[nx][ny]) {
            continue;
          }
          stack.push([nx, ny]);
          used[nx][ny] = true;
          ret++;
        }
      }
    }

    return ret;
  };

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (board[i][j] === 1 && used[i][j] === false) {
        res.push(dfs([i, j]));
      }
    }
  }

  return [res.length, ...res.sort((a, b) => a - b)].join('\n');
}
