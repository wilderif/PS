// BOJ_2610
// 회의준비

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const m = Number(inputArr[1]);
  const graph = Array.from({ length: n + 1 }, () =>
    new Array(n + 1).fill(Infinity)
  );

  for (const el of inputArr.slice(2)) {
    const [a, b] = el.split(' ').map(Number);
    graph[a][b] = 1;
    graph[b][a] = 1;
  }

  for (let i = 1; i <= n; i++) {
    graph[i][i] = 0;
  }

  for (let k = 0; k <= n; k++) {
    for (let s = 0; s <= n; s++) {
      for (let d = 0; d <= n; d++) {
        if (graph[s][d] > graph[s][k] + graph[k][d]) {
          graph[s][d] = graph[s][k] + graph[k][d];
        }
      }
    }
  }

  const group = new Map();
  const groupRes = new Map();
  for (let i = 1; i <= n; i++) {
    let tmpGroup = [];
    let tmp = 0;
    for (let j = 1; j <= n; j++) {
      if (graph[i][j] !== Infinity) {
        tmpGroup.push(j);
        tmp = Math.max(graph[i][j], tmp);
      }
    }
    const groupKey = tmpGroup.join();
    if (!group.has(groupKey) || group.get(groupKey) > tmp) {
      group.set(groupKey, tmp);
      groupRes.set(groupKey, i);
    }
  }

  const res = [0];
  for (let el of groupRes.values()) {
    res.push(el);
  }
  res.sort((a, b) => a - b);
  res[0] = groupRes.size;

  return res.join('\n');
}

console.log(solution(input));
