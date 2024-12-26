// BOJ_17829
// 222-풀링

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const mat = [];
  for (let i = 1; i <= n; i++) {
    mat.push(inputArr[i].split(' ').map((el) => Number(el)));
  }

  const polling = (matrix, size) => {
    if (size === 1) {
      return matrix[0][0];
    }

    const halfSize = size / 2;

    const newMat = new Array(halfSize);
    for (let i = 0; i < halfSize; i++) {
      newMat[i] = new Array(halfSize);
    }

    for (let i = 0; i < halfSize; i++) {
      for (let j = 0; j < halfSize; j++) {
        const tmp = [];
        for (let k = 0; k < 2; k++) {
          for (let l = 0; l < 2; l++) {
            tmp.push(matrix[i * 2 + k][j * 2 + l]);
          }
        }
        newMat[i][j] = tmp.sort((a, b) => a - b)[2];
      }
    }

    return polling(newMat, halfSize);
  };

  return polling(mat, n);
}

console.log(solution(input));
