// BOJ_12100
// 2048 (Easy)

const fs = require('fs');
// const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
// const input = fs.readFileSync(filePath).toString().trim().split('\n');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const board = inputArr.slice(1).map((el) => el.split(' ').map(Number));

  let res = 0;
  const action = new Array(5);

  const moveOne = (one) => {
    const newOne = new Array(n).fill(0);
    let toMove = 0;

    for (let i = 0; i < n; i++) {
      if (one[i] === 0) {
        continue;
      }
      if (newOne[toMove] === one[i]) {
        newOne[toMove] = one[i] * 2;
        toMove++;
      } else {
        if (newOne[toMove] !== 0) {
          toMove++;
        }
        newOne[toMove] = one[i];
      }
    }

    return newOne;
  };

  /**
   * dir
   * 0: left
   * 1: right
   * 2: up
   * 3: down
   */
  const move = (tmpBoard, dir) => {
    if (dir === 0) {
      for (let i = 0; i < n; i++) {
        const one = [...tmpBoard[i]];
        const newOne = moveOne(one);
        tmpBoard[i] = newOne;
      }
    }
    if (dir === 1) {
      for (let i = 0; i < n; i++) {
        const one = [...tmpBoard[i]].reverse();
        const newOne = moveOne(one).reverse();
        tmpBoard[i] = newOne;
      }
    }
    if (dir === 2) {
      for (let i = 0; i < n; i++) {
        const one = new Array(n);
        for (let j = 0; j < n; j++) {
          one[j] = tmpBoard[j][i];
        }
        const newOne = moveOne(one);
        for (let j = 0; j < n; j++) {
          tmpBoard[j][i] = newOne[j];
        }
      }
    }
    if (dir === 3) {
      for (let i = 0; i < n; i++) {
        const one = new Array(n);
        for (let j = 0; j < n; j++) {
          one[j] = tmpBoard[j][i];
        }
        const newOne = moveOne(one.reverse()).reverse();
        for (let j = 0; j < n; j++) {
          tmpBoard[j][i] = newOne[j];
        }
      }
    }
  };

  const check = () => {
    const tmpBoard = board.map((el) => [...el]);
    action.forEach((val) => {
      move(tmpBoard, val);
    });

    tmpBoard.forEach((row) => {
      row.forEach((val) => {
        if (val > res) {
          res = val;
        }
      });
    });
  };

  const backtracking = (idx) => {
    if (idx === 5) {
      check();
      return;
    }
    for (let i = 0; i < 4; i++) {
      action[idx] = i;
      backtracking(idx + 1);
    }
  };

  backtracking(0);

  return res;
}

console.log(solution(input));
