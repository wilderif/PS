// 8단_변속기

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
  const arr = inputArr[0].split(' ').map(Number);
  let asc = true;
  let desc = true;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== i + 1) {
      asc = false;
    }
    if (arr[i] !== 8 - i) {
      desc = false;
    }
    if (!asc && !desc) {
      return 'mixed';
    }
  }

  if (asc) {
    return 'ascending';
  }
  return 'descending';
}
