// BOJ_1613
// 역사

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const [n, k] = inputArr[0].split(' ').map(Number);
  const graph = Array.from({ length: n + 1 }, () =>
    new Array(n + 1).fill(Infinity)
  );

  for (const el of inputArr.slice(1, 1 + k)) {
    const [a, b] = el.split(' ').map(Number);
    graph[a][b] = 1;
    graph[b][a] = -1;
  }

  for (let k = 1; k <= n; k++) {
    for (let s = 1; s <= n; s++) {
      for (let d = 1; d <= n; d++) {
        if (graph[s][k] === 1 && graph[k][d] === 1) {
          graph[s][d] = 1;
        }
        if (graph[s][k] === -1 && graph[k][d] === -1) {
          graph[s][d] = -1;
        }
      }
    }
  }

  const res = [];
  for (const el of inputArr.slice(k + 2)) {
    const [a, b] = el.split(' ').map(Number);
    if (graph[a][b] === 1) {
      res.push(-1);
    } else if (graph[a][b] === -1) {
      res.push(1);
    } else {
      res.push(0);
    }
  }

  return res.join('\n');
}

console.log(solution(input));
