// BOJ_1956
// 운동

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const [v, e] = inputArr[0].split(' ').map(Number);
  const graph = Array.from({ length: v + 1 }, () =>
    new Array(v + 1).fill(Infinity)
  );

  for (const el of inputArr.slice(1)) {
    const [a, b, c] = el.split(' ').map(Number);
    graph[a][b] = c;
  }

  for (let k = 1; k <= v; k++) {
    for (let s = 1; s <= v; s++) {
      for (let d = 1; d <= v; d++) {
        if (graph[s][k] + graph[k][d] < graph[s][d]) {
          graph[s][d] = graph[s][k] + graph[k][d];
        }
      }
    }
  }

  let res = Infinity;
  for (let i = 1; i <= v; i++) {
    res = Math.min(res, graph[i][i]);
  }

  if (res === Infinity) {
    return -1;
  }
  return res;
}

console.log(solution(input));
