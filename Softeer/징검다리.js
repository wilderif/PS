// 징검다리

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
  const arr = inputArr[1].split(' ').map(Number);
  const mem = new Array(n).fill(1);

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < i; j++) {
      if (arr[i] > arr[j]) {
        mem[i] = Math.max(mem[i], mem[j] + 1);
      }
    }
  }

  return Math.max(...mem);
}
