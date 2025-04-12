// BOJ_13344
// Chess Tournament

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function main(inputArr) {
  const find = (x) => {
    if (parent[x] < 0) {
      return x;
    }

    return (parent[x] = find(parent[x]));
  };

  const union = (u, v) => {
    u = find(u);
    v = find(v);

    if (u === v) {
      return false;
    }

    if (parent[u] > parent[v]) {
      [u, v] = [v, u];
    }
    if (parent[u] === parent[v]) {
      parent[u]--;
    }
    parent[v] = u;

    return true;
  };

  const [n, m] = inputArr[0].split(' ').map(Number);
  const graph = Array.from({ length: n }, () => []);
  const indeg = new Array(n).fill(0);
  const parent = new Array(n).fill(-1);

  for (const el of inputArr.slice(1)) {
    const [k, symbol, l] = el.split(' ').map((val, idx) => {
      if (idx === 1) {
        return val;
      }
      return Number(val);
    });

    if (symbol === '=') {
      union(k, l);
    }
  }

  for (const el of inputArr.slice(1)) {
    let [k, symbol, l] = el.split(' ').map((val, idx) => {
      if (idx === 1) {
        return val;
      }
      return Number(val);
    });

    if (symbol === '=') {
      continue;
    }

    if (symbol === '<') {
      [k, l] = [l, k];
    }

    const kGroup = find(k);
    const lGroup = find(l);
    if (kGroup === lGroup) {
      return 'inconsistent';
    }

    graph[kGroup].push(lGroup);
    indeg[lGroup]++;
  }

  const stack = [];
  for (let i = 0; i < n; i++) {
    const group = find(i);
    if (indeg[find(i)]) {
      continue;
    }
    stack.push(group);
  }

  while (stack.length) {
    const cur = stack.pop();
    for (const nxt of graph[cur]) {
      indeg[nxt]--;
      if (indeg[nxt] === 0) {
        if (cur === nxt) {
          return 'inconsistent';
        }
        stack.push(nxt);
      }
    }
  }

  for (let i = 0; i < n; i++) {
    const group = find(i);
    if (indeg[group] > 0) {
      return 'inconsistent';
    }
  }

  return 'consistent';
}

console.log(main(input));
