// BOJ_16562
// 친구비

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function main(inputArr) {
  function find(x) {
    if (parent[x] < 0) {
      return x;
    }

    return (parent[x] = find(parent[x]));
  }

  function union(u, v) {
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
  }

  const [n, m, k] = inputArr[0].split(' ').map(Number);
  const cost = [0, ...inputArr[1].split(' ').map(Number)];
  const parent = new Array(n + 1).fill(-1);
  const groupcost = new Array(n + 1).fill(Infinity);

  for (const el of inputArr.slice(2)) {
    const [v, w] = el.split(' ').map(Number);
    union(v, w);
  }

  for (let i = 1; i < n + 1; i++) {
    const curRoot = find(i);

    groupcost[curRoot] = Math.min(groupcost[curRoot], cost[i]);
  }

  const res = groupcost.reduce(
    (acc, cur) => (cur === Infinity ? acc : acc + cur),
    0
  );

  return res <= k ? res : 'Oh no';
}

console.log(main(input));
