// BOJ_2617
// 구슬 찾기

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const [n, m] = inputArr[0].split(' ').map(Number);
  const edges = inputArr.slice(1).map((el) => el.split(' ').map(Number));
  const graph1 = Array.from({ length: n + 1 }, () => new Array());
  const graph2 = Array.from({ length: n + 1 }, () => new Array());
  const target = (n + 1) / 2;
  edges.forEach((el) => {
    graph1[el[0]].push(el[1]);
    graph2[el[1]].push(el[0]);
  });

  const check = (v, graph) => {
    const stack = [v];
    const vis = new Array(n + 1).fill(false);
    let cnt = 0;
    while (stack.length) {
      const cur = stack.pop();

      for (let nxt of graph[cur]) {
        if (vis[nxt]) {
          continue;
        }
        vis[nxt] = true;
        stack.push(nxt);
        cnt++;
      }
      if (cnt >= target) {
        return true;
      }
    }
    return false;
  };

  let res = 0;
  for (let i = 1; i < n + 1; i++) {
    if (check(i, graph1)) {
      res++;
      continue;
    }
    if (check(i, graph2)) {
      res++;
    }
  }

  return res;
}

console.log(solution(input));
