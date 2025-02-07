// 우물_안_개구리

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
  const arr = [0, ...inputArr[1].split(' ').map(Number)];
  const check = new Array(n + 1).fill(true);

  for (const el of inputArr.slice(2)) {
    const [a, b] = el.split(' ').map(Number);
    if (!check[a] && !check[b]) {
      continue;
    }

    if (arr[a] >= arr[b]) {
      check[b] = false;
    }
    if (arr[a] <= arr[b]) {
      check[a] = false;
    }
  }

  return check.filter((el) => el).length - 1;
}
