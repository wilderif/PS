// 근무_시간

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
  let res = 0;
  for (const el of inputArr) {
    const [start, end] = el.split(' ');
    const [startH, startM] = start.split(':');
    const [endH, endM] = end.split(':');
    res += (endH - startH) * 60 + (endM - startM);
  }

  return res;
}
