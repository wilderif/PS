// BOJ_15683
// 감시

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

function solution(inputArr) {
  const directions = {
    1: [[[-1, 0]], [[1, 0]], [[0, -1]], [[0, 1]]],
    2: [
      [
        [-1, 0],
        [1, 0],
      ],
      [
        [0, 1],
        [0, -1],
      ],
    ],
    3: [
      [
        [-1, 0],
        [0, -1],
      ],
      [
        [-1, 0],
        [0, 1],
      ],
      [
        [1, 0],
        [0, -1],
      ],
      [
        [1, 0],
        [0, 1],
      ],
    ],
    4: [
      [
        [-1, 0],
        [1, 0],
        [0, -1],
      ],
      [
        [-1, 0],
        [1, 0],
        [0, 1],
      ],
      [
        [-1, 0],
        [0, -1],
        [0, 1],
      ],
      [
        [1, 0],
        [0, -1],
        [0, 1],
      ],
    ],
    5: [
      [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1],
      ],
    ],
  };

  const [n, m] = inputArr[0].split(' ').map((el) => Number(el));
  const board = inputArr.slice(1).map((row) => row.split(' ').map(Number));

  const cctvArr = [];
  let wallCnt = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (board[i][j] !== 0 && board[i][j] !== 6) {
        cctvArr.push([board[i][j], i, j]);
      }
      if (board[i][j] === 6) {
        wallCnt++;
      }
    }
  }

  const cctvCnt = cctvArr.length;
  const direction = new Array(cctvCnt).fill(0);
  let res = n * m;

  const checkDirection = (tmpBoard, x, y, dir) => {
    for (let [dx, dy] of dir) {
      let nx = x;
      let ny = y;
      while (0 <= nx && nx < n && 0 <= ny && ny < m) {
        if (board[nx][ny] === 6) {
          break;
        }
        tmpBoard[nx][ny] = false;
        nx += dx;
        ny += dy;
      }
    }
  };

  const check = () => {
    const tmpBoard = new Array(n);
    for (let i = 0; i < n; i++) {
      tmpBoard[i] = new Array(m).fill(true);
    }

    for (let i = 0; i < cctvCnt; i++) {
      checkDirection(
        tmpBoard,
        cctvArr[i][1],
        cctvArr[i][2],
        directions[cctvArr[i][0]][direction[i]]
      );
    }

    let ret = 0;
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < m; j++) {
        if (tmpBoard[i][j]) {
          ret++;
        }
      }
    }

    ret -= wallCnt;

    if (ret < res) {
      res = ret;
    }
  };

  const backTracking = (idx) => {
    if (idx === cctvCnt) {
      check();
      return;
    }

    const cctvType = cctvArr[idx][0];
    for (let i = 0; i < directions[cctvType].length; i++) {
      direction[idx] = i;
      backTracking(idx + 1);
    }
  };

  backTracking(0);

  return res;
}

console.log(solution(input));
