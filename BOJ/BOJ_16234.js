// BOJ_16234
// 인구 이동

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function main(inputArr) {
  const [n, l, r] = inputArr[0].split(' ').map(Number);
  const board = inputArr.slice(1).map((el) => el.split(' ').map(Number));

  const bfs = (vis, start) => {
    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];
    const group = { groupTotal: board[start[0]][start[1]], coord: [start] };
    let q = [start];

    while (q.length) {
      const nq = [];
      for (const [x, y] of q) {
        for (let d = 0; d < 4; d++) {
          const nx = x + dx[d];
          const ny = y + dy[d];

          if (!(0 <= nx && nx < n && 0 <= ny && ny < n)) {
            continue;
          }
          if (vis[nx][ny]) {
            continue;
          }
          const diff = Math.abs(board[x][y] - board[nx][ny]);
          if (diff < l || diff > r) {
            continue;
          }

          vis[nx][ny] = true;
          nq.push([nx, ny]);
          group.groupTotal += board[nx][ny];
          group.coord.push([nx, ny]);
        }
      }

      q = nq;
    }

    return group;
  };

  const findGroup = () => {
    const groupArr = [];
    const vis = Array.from({ length: n }, () => new Array(n).fill(false));

    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (vis[i][j]) {
          continue;
        }
        vis[i][j] = true;
        const tmp = bfs(vis, [i, j]);
        if (tmp.coord.length > 1) {
          groupArr.push(tmp);
        }
      }
    }

    return groupArr;
  };

  const move = (groupArr) => {
    for (const { coord, groupTotal } of groupArr) {
      const tmp = Math.floor(groupTotal / coord.length);
      for (const [x, y] of coord) {
        board[x][y] = tmp;
      }
    }
  };

  let res = 0;
  while (true) {
    const groupArr = findGroup();
    if (!groupArr.length) {
      break;
    }
    res++;
    move(groupArr);
  }

  return res;
}

console.log(main(input));
