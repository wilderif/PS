// BOJ_14567
// 선수과목 (Prerequisite)

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const [n, m] = inputArr[0].split(' ').map(Number);
  const graph = Array.from({ length: n + 1 }, () => []);
  const indeg = new Array(n + 1).fill(0);
  const res = new Array(n + 1).fill(0);

  for (const el of inputArr.slice(1)) {
    const [a, b] = el.split(' ').map(Number);
    graph[a].push(b);
    indeg[b]++;
  }

  let stack = [];
  let cnt = 1;
  for (let i = 1; i <= n; i++) {
    if (indeg[i] === 0) {
      stack.push(i);
      res[i] = cnt;
    }
  }

  while (stack.length) {
    const nxtStack = [];
    cnt++;
    for (const cur of stack) {
      for (const nxt of graph[cur]) {
        indeg[nxt]--;
        if (indeg[nxt] === 0) {
          nxtStack.push(nxt);
          res[nxt] = cnt;
        }
      }
    }
    stack = nxtStack;
  }

  return res.slice(1).join(' ');
}

console.log(solution(input));
