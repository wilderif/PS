// BOJ_2213
// 트리의 독립집합

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function main(inputArr) {
  const n = Number(inputArr[0]);
  const arr = [0, ...inputArr[1].split(' ').map(Number)];
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
      dp[curNode][1] += Math.max(...dp[nxtNode]);
    }
  };

  const trace = (curNode, prevNode) => {
    if (!vis[prevNode] && dp[curNode][0] > dp[curNode][1]) {
      vis[curNode] = true;
      resNode.push(curNode);
    }

    for (const nxtNode of tree[curNode]) {
      if (nxtNode === prevNode) {
        continue;
      }
      trace(nxtNode, curNode);
    }
  };

  let res = 0;
  const resNode = [];
  dfs(1);
  res = Math.max(...dp[1]);

  for (let i = 0; i < n + 1; i++) {
    vis[i] = false;
  }
  trace(1, 0);

  return [res, resNode.sort((a, b) => a - b).join(' ')].join('\n');
}

console.log(main(input));
