// 바이러스

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
  let [k, p, n] = inputArr[0].split(' ').map(BigInt);

  while (n--) {
    k *= p;
    k %= 1000000007n;
  }

  return k.toString();
}
