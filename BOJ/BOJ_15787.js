// BOJ_15787
// 기차가 어둠을 헤치고 은하수를

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const [n, m] = input[0].split(' ').map(Number);
  const trainArr = new Array(n + 1).fill(0);

  for (const el of inputArr.slice(1)) {
    const commnad = el.split(' ').map(Number);
    if (commnad[0] === 1) {
      trainArr[commnad[1]] |= 1 << (commnad[2] - 1);
    } else if (commnad[0] === 2) {
      trainArr[commnad[1]] &= ~(1 << (commnad[2] - 1));
    } else if (commnad[0] === 3) {
      trainArr[commnad[1]] <<= 1;
      trainArr[commnad[1]] &= ~(1 << 20);
    } else if (commnad[0] === 4) {
      trainArr[commnad[1]] >>= 1;
    }
  }

  const res = new Set();
  for (let i = 1; i <= n; i++) {
    res.add(trainArr[i]);
  }

  return res.size;
}

console.log(solution(input));
