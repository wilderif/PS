// BOJ_16948
// 데스 나이트

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const [r1, c1, r2, c2] = inputArr[1].split(' ').map((el) => Number(el));
  const dx = [-2, -2, 0, 0, 2, 2];
  const dy = [-1, 1, -2, 2, -1, 1];

  const board = [];
  for (let i = 0; i < n; i++) {
    board.push(new Array(n).fill(false));
  }

  let queue = [];
  queue.push([r1, c1]);
  let dist = 0;
  while (queue.length) {
    const newQueue = [];
    dist++;
    for (const cur of queue) {
      for (let d = 0; d < 6; d++) {
        const nx = cur[0] + dx[d];
        const ny = cur[1] + dy[d];
        if (nx === r2 && ny === c2) {
          return dist;
        }
        if (0 <= nx && nx < n && 0 <= ny && ny < n) {
          if (!board[nx][ny]) {
            board[nx][ny] = true;
            newQueue.push([nx, ny]);
          }
        }
      }
    }

    queue = newQueue;
  }

  return -1;
}

console.log(solution(input));
