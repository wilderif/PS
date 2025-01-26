// 성적_평균

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
  const [n, k] = inputArr[0].split(' ').map(Number);
  const arr = [0, ...inputArr[1].split(' ').map(Number)];

  for (let i = 0; i < arr.length; i++) {
    if (i) {
      arr[i] += arr[i - 1];
    }
  }

  const res = [];
  for (const el of inputArr.slice(2)) {
    const [a, b] = el.split(' ').map(Number);
    res.push(((arr[b] - arr[a - 1]) / (b - a + 1)).toFixed(2));
  }

  return res.join('\n');
}
