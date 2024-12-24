// BOJ_3187
// 양치기 꿍

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

function solution(inputArr) {
  const [r, c] = inputArr[0].split(' ').map((el) => Number(el));
  const board = [];
  for (let i = 1; i <= r; i++) {
    board.push(inputArr[i].split(''));
  }
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];

  let res = [0, 0];

  const vis = [];
  for (let i = 0; i < r; i++) {
    vis.push(new Array(c).fill(false));
  }

  const dfs = (start) => {
    let tmpV = 0;
    let tmpK = 0;
    const stack = [];
    stack.push(start);
    vis[start[0]][start[1]] = true;
    if (board[start[0]][start[1]] === 'v') {
      tmpV++;
    }
    if (board[start[0]][start[1]] === 'k') {
      tmpK++;
    }
    while (stack.length) {
      const cur = stack.pop();
      for (let d = 0; d < 4; d++) {
        const nx = cur[0] + dx[d];
        const ny = cur[1] + dy[d];

        if (
          nx < 0 ||
          nx >= r ||
          ny < 0 ||
          ny >= c ||
          board[nx][ny] === '#' ||
          vis[nx][ny]
        ) {
          continue;
        }

        vis[nx][ny] = true;
        if (board[nx][ny] === 'v') {
          tmpV++;
        }
        if (board[nx][ny] === 'k') {
          tmpK++;
        }
        stack.push([nx, ny]);
      }
    }

    if (tmpK > tmpV) {
      res[0] += tmpK;
    } else {
      res[1] += tmpV;
    }
  };

  for (let i = 0; i < r; i++) {
    for (let j = 0; j < c; j++) {
      if (board[i][j] !== '#' && !vis[i][j]) {
        dfs([i, j]);
      }
    }
  }

  return res.join(' ');
}

console.log(solution(input));
