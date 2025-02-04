// 개표

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
  const t = Number(inputArr[0]);
  const res = [];

  for (const el of inputArr.slice(1).map(Number)) {
    let tmp = '';
    tmp += '++++ '.repeat(Math.floor(el / 5));
    tmp += '|'.repeat(el % 5);
    res.push(tmp);
  }

  return res.join('\n');
}
