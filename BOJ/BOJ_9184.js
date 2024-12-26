// BOJ_9184
// 신나는 함수 실행

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

function solution(inputArr) {
  const w = (a, b, c) => {
    if (a <= 0 || b <= 0 || c <= 0) {
      return 1;
    }
    if (a > 20 || b > 20 || c > 20) {
      return w(20, 20, 20);
    }

    if (mem[a][b][c] !== null) {
      return mem[a][b][c];
    }

    if (a < b && b < c) {
      mem[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c);
      return mem[a][b][c];
    }

    mem[a][b][c] =
      w(a - 1, b, c) +
      w(a - 1, b - 1, c) +
      w(a - 1, b, c - 1) -
      w(a - 1, b - 1, c - 1);
    return mem[a][b][c];
  };

  const res = [];
  const mem = new Array(21);
  for (let i = 0; i < 21; i++) {
    mem[i] = new Array(21);
    for (let j = 0; j < 21; j++) {
      mem[i][j] = new Array(21).fill(null);
    }
  }

  for (let i = 0; i < inputArr.length - 1; i++) {
    const [a, b, c] = inputArr[i].split(' ').map((el) => Number(el));

    res.push(`w(${a}, ${b}, ${c}) = ${w(a, b, c)}`);
  }

  return res.join('\n');
}

console.log(solution(input));
