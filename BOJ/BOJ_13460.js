// BOJ_13460
// 구슬 탈출 2

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function main(inputArr) {
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];

  const [n, m] = inputArr[0].split(' ').map(Number);
  const board = inputArr.slice(1).map((el) => el.split(''));

  const move = (rStart, bStart, direction) => {
    let rPos = rStart;
    let bPos = bStart;

    let rInHole = false;
    let bInHole = false;

    while (true) {
      let rMoved = false;
      let bMoved = false;

      while (!rInHole) {
        const rnx = rPos[0] + direction[0];
        const rny = rPos[1] + direction[1];

        if (board[rnx][rny] === '#') {
          break;
        }
        if (board[rnx][rny] === 'O') {
          rInHole = true;
          rPos = [rnx, rny];
          break;
        }
        if (rnx === bPos[0] && rny === bPos[1]) {
          break;
        }

        rMoved = true;
        rPos = [rnx, rny];
      }

      while (!bInHole) {
        const bnx = bPos[0] + direction[0];
        const bny = bPos[1] + direction[1];

        if (board[bnx][bny] === '#') {
          break;
        }
        if (board[bnx][bny] === 'O') {
          bInHole = true;
          bPos = [bnx, bny];
          break;
        }
        if (bnx === rPos[0] && bny === rPos[1]) {
          break;
        }

        bMoved = true;
        bPos = [bnx, bny];
      }

      if (!rMoved && !bMoved) {
        break;
      }
    }

    return [rInHole, bInHole, rPos, bPos];
  };

  const coordToKey = (c1, c2) => {
    return [c1.join(), c2.join()].join();
  };

  const bfs = (rStart, bStart) => {
    let q = [[rStart, bStart]];
    const vis = new Set();
    vis.add(coordToKey(rStart, bStart));
    let cnt = 0;

    while (q.length) {
      const nq = [];
      cnt += 1;

      for (const [curR, curB] of q) {
        for (let d = 0; d < 4; d++) {
          const [rInHole, bInHole, newR, newB] = move(curR, curB, [
            dx[d],
            dy[d],
          ]);

          if (bInHole) {
            continue;
          }
          if (rInHole) {
            return cnt;
          }

          const nKey = coordToKey(newR, newB);
          if (vis.has(nKey)) {
            continue;
          }
          vis.add(nKey);
          nq.push([newR, newB]);
        }
      }

      if (cnt === 10) {
        return -1;
      }

      q = nq;
    }

    return -1;
  };

  let rStart = null;
  let bStart = null;

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (board[i][j] === 'R') {
        rStart = [i, j];
      }
      if (board[i][j] === 'B') {
        bStart = [i, j];
      }
    }
  }

  return bfs(rStart, bStart);
}

console.log(main(input));
