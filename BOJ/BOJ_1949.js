// BOJ_1949
// 우수 마을

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function main(inputArr) {
  const n = Number(inputArr[0]);
  const arr = [-1, ...inputArr[1].split(' ').map(Number)];
  const tree = Array.from({ length: n + 1 }, () => []);
  const dp = Array.from({ length: n + 1 }, (_, i) => [arr[i], 0]);
  const vis = new Array(n + 1).fill(false);

  for (const el of inputArr.slice(2)) {
    const [u, v] = el.split(' ').map(Number);
    tree[u].push(v);
    tree[v].push(u);
  }

  const dfs = (curNode) => {
    vis[curNode] = true;

    for (const nxtNode of tree[curNode]) {
      if (vis[nxtNode]) {
        continue;
      }
      dfs(nxtNode);
      dp[curNode][0] += dp[nxtNode][1];
      dp[curNode][1] += Math.max(dp[nxtNode][0], dp[nxtNode][1]);
    }
  };

  dfs(1);

  return Math.max(...dp[1]);
}

console.log(main(input));
