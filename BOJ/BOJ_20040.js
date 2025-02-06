// BOJ_20040
// 사이클 게임

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const [n, m] = inputArr[0].split(' ').map(Number);
  const parent = new Array(n).fill(-1);

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

  let res = 0;

  inputArr.slice(1).forEach((el, idx) => {
    const [a, b] = el.split(' ').map(Number);
    if (!union(a, b) && res === 0) {
      res = idx + 1;
    }
  });

  return res;
}

console.log(solution(input));
s;
