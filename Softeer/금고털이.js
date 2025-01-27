// 금고털이

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
  const [w, n] = inputArr[0].split(' ').map(Number);
  const arr = inputArr
    .slice(1)
    .map((el) => el.split(' ').map(Number))
    .sort((a, b) => b[1] - a[1]);
  let curW = 0;
  let res = 0;

  for (const [m, p] of arr) {
    if (curW + m < w) {
      curW += m;
      res += m * p;
    } else {
      res += (w - curW) * p;
      break;
    }
  }

  return res;
}
