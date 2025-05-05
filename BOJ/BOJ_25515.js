// BOJ_25515
// 트리 노드 합의 최댓값

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function main(inputArr) {
  const n = Number(inputArr[0]);
  const graph = Array.from({ length: n }, () => []);
  for (const el of inputArr.slice(1, inputArr.length - 1)) {
    const [u, v] = el.split(' ').map(Number);
    graph[u].push(v);
    graph[v].push(u);
  }
  const valArr = inputArr[inputArr.length - 1].split(' ').map(Number);
  const dp = new Array(n).fill(0);
  const vis = new Array(n).fill(false);

  function dfs(curNode) {
    vis[curNode] = true;
    dp[curNode] += valArr[curNode];

    for (const nxtNode of graph[curNode]) {
      if (vis[nxtNode]) {
        continue;
      }

      dfs(nxtNode);
      if (dp[nxtNode] > 0) {
        dp[curNode] += dp[nxtNode];
      }
    }
  }

  dfs(0);

  return dp[0];
}

console.log(main(input));
