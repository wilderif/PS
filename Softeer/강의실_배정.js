// 강의실_배정

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
  const n = Number(inputArr[0]);
  const arr = inputArr
    .slice(1)
    .map((el) => el.split(' ').map(Number))
    .sort((a, b) => a[1] - b[1]);

  let res = 0;
  let curTime = 0;
  for (const el of arr) {
    if (el[0] >= curTime) {
      res++;
      curTime = el[1];
    }
  }

  return res;
}
