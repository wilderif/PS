// BOJ_14267
// 회사 문화 1

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function main(inputArr) {
  const [n, m] = inputArr[0].split(' ').map(Number);
  const tree = Array.from({ length: n + 1 }, () => []);
  const dp = new Array(n + 1).fill(0);
  const vis = new Array(n + 1).fill(false);

  inputArr[1].split(' ').map((val, idx) => {
    if (idx === 0) {
      return;
    }
    const tmp = Number(val);
    // tree[idx + 1].push(tmp);
    tree[tmp].push(idx + 1);
  });

  for (const el of inputArr.slice(2, 2 + m)) {
    const [i, w] = el.split(' ').map(Number);
    dp[i] += w;
  }

  const dfs = (curNode) => {
    vis[curNode] = true;
    for (const nxtNode of tree[curNode]) {
      if (vis[nxtNode]) {
        continue;
      }
      dp[nxtNode] += dp[curNode];
      dfs(nxtNode);
    }
  };

  dfs(1);

  return dp.slice(1).join(' ');
}

console.log(main(input));
