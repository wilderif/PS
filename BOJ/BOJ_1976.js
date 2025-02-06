// BOJ_1976
// 여행 가자

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const m = Number(inputArr[1]);

  const parent = new Array(n + 1).fill(-1);

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

  for (let i = 2; i < 2 + n; i++) {
    const tmpArr = inputArr[i].split(' ').map(Number);
    for (let j = 0; j < n; j++) {
      if (tmpArr[j]) {
        union(i - 1, j + 1);
      }
    }
  }

  const plan = inputArr[inputArr.length - 1].split(' ').map(Number);
  for (let i = 0; i < m - 1; i++) {
    if (find(plan[i]) !== find(plan[i + 1])) {
      return 'NO';
    }
  }

  return 'YES';
}

console.log(solution(input));
