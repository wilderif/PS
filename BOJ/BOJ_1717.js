// BOJ_1717
// 집합의 표현

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const [n, m] = inputArr[0].split(' ').map(Number);
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

    // 경로 압축을 하면, 관리하는 rank값이 왜곡 되는 것 아닌가???
    if (parent[u] > parent[v]) {
      [u, v] = [v, u];
    }
    if (parent[u] === parent[v]) {
      parent[u]--;
    }
    // parent[u] += parent[v]; // size 활용한 방법
    parent[v] = u;

    return true;
  };

  const res = [];
  for (const el of inputArr.slice(1)) {
    const [comm, a, b] = el.split(' ').map(Number);
    if (comm === 0) {
      union(a, b);
    } else if (comm === 1) {
      if (find(a) === find(b)) {
        res.push('YES');
      } else {
        res.push('NO');
      }
    }
  }

  return res.join('\n');
}

console.log(solution(input));
