// BOJ_3044
// 자전거 경주 준비하기

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const [n, m] = inputArr[0].split(' ').map(Number);
  const oldGraph = Array.from({ length: n + 1 }, () => new Array());
  const oldGraphReverse = Array.from({ length: n + 1 }, () => new Array());

  for (const el of inputArr.slice(1)) {
    const [ini, ter] = el.split(' ').map(Number);
    oldGraph[ini].push(ter);
    oldGraphReverse[ter].push(ini);
  }

  const findReachable = (start, graph) => {
    const vis = new Array(n + 1).fill(false);
    const stack = [start];
    const reachable = new Set();
    vis[start] = true;
    reachable.add(start);

    while (stack.length) {
      const cur = stack.pop();
      for (const nxt of graph[cur]) {
        if (vis[nxt]) {
          continue;
        }
        vis[nxt] = true;
        reachable.add(nxt);
        stack.push(nxt);
      }
    }

    return reachable;
  };

  const reachableFrom1 = findReachable(1, oldGraph);
  if (!reachableFrom1.has(2)) {
    return 0;
  }
  const reachableTo2 = findReachable(2, oldGraphReverse);

  const validPath = new Set();
  for (const el of reachableFrom1) {
    if (reachableTo2.has(el)) {
      validPath.add(el);
    }
  }

  const newGraph = Array.from({ length: n + 1 }, () => new Array());
  const indeg = new Array(n + 1).fill(0);

  for (const el of validPath) {
    for (const nxt of oldGraph[el]) {
      if (!validPath.has(nxt)) {
        continue;
      }
      newGraph[el].push(nxt);
      indeg[nxt]++;
    }
  }

  const mem = new Array(n + 1).fill(0n);
  mem[1] = 1n;
  const stack = [];
  for (let i = 1; i <= n; i++) {
    if (indeg[i] === 0) {
      stack.push(i);
    }
  }

  while (stack.length) {
    const cur = stack.pop();
    for (nxt of newGraph[cur]) {
      indeg[nxt]--;
      mem[nxt] = mem[nxt] + mem[cur];
      if (indeg[nxt] === 0) {
        if (nxt === 2) {
          return mem[2].toString().slice(-9);
        }
        stack.push(nxt);
      }
    }
  }

  return 'inf';
}

console.log(solution(input));
