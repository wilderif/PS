// 나무_공격

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const inputArr = [];

rl.on('line', (line) => {
  inputArr.push(line);
});

rl.on('close', () => {
  console.log(solution(inputArr));
  process.exit(0);
});

function solution(inputArr) {
  const [n, m] = inputArr[0].split(' ').map(Number);
  const board = [0];
  for (const el of inputArr.slice(1, 1 + n)) {
    board.push(
      el
        .split(' ')
        .map(Number)
        .reduce((acc, cur) => {
          if (cur === 1) {
            return ++acc;
          }
          return acc;
        }, 0)
    );
  }

  const atack = new Array(n + 2).fill(0);
  for (const el of inputArr.slice(n + 1)) {
    const [x, y] = el.split(' ').map(Number);
    atack[x]++;
    atack[y + 1]--;
  }

  for (let i = 1; i <= n; i++) {
    atack[i] += atack[i - 1];
    board[i] = atack[i] > board[i] ? 0 : board[i] - atack[i];
  }

  return board.reduce((acc, cur) => acc + cur, 0);
}
