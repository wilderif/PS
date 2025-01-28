// A+B

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
  const t = Number(inputArr[0]);
  const res = [];

  inputArr
    .slice(1)
    .map((el) => el.split(' ').map(Number))
    .map((el, idx) => {
      res.push(`Case #${idx + 1}: ${el[0] + el[1]}`);
    });

  return res.join('\n');
}
