// BOJ_15681
// 트리와 쿼리

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function main(inputArr) {
  const [n, r, q] = inputArr[0].split(' ').map(Number);
  const tree = Array.from({ length: n + 1 }, () => []);
  const dp = new Array(n + 1).fill(1);
  const vis = new Array(n + 1).fill(false);

  let line = 1;
  for (let i = 0; i < n - 1; i++) {
    const [u, v] = inputArr[line++].split(' ').map(Number);
    tree[u].push(v);
    tree[v].push(u);
  }

  const dfs = (curNode) => {
    vis[curNode] = true;

    for (const nxtNode of tree[curNode]) {
      if (vis[nxtNode]) {
        continue;
      }
      dp[curNode] += dfs(nxtNode);
    }

    return dp[curNode];
  };

  dfs(r);

  const res = [];
  for (let i = 0; i < q; i++) {
    res.push(dp[Number(inputArr[line++])]);
  }

  return res.join('\n');
}

console.log(main(input));
