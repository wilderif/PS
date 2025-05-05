// BOJ_27501
// RGB트리

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function main(inputArr) {
  const n = Number(inputArr[0]);
  const graph = Array.from({ length: n + 1 }, () => []);
  for (const el of inputArr.slice(1, n)) {
    const [u, v] = el.split(' ').map(Number);
    graph[u].push(v);
    graph[v].push(u);
  }

  const valArr = [[-1, -1, -1]];
  for (const el of inputArr.slice(n)) {
    valArr.push(el.split(' ').map(Number));
  }

  const dp = Array.from({ length: n + 1 }, () => new Array(3).fill(0));
  const path = Array.from({ length: n + 1 }, () => new Array(3).fill(-1));
  const vis = new Array(n + 1).fill(false);

  function dfs(curNode) {
    vis[curNode] = true;
    for (let i = 0; i < 3; i++) {
      dp[curNode][i] = valArr[curNode][i];
    }

    for (const nxtNode of graph[curNode]) {
      if (vis[nxtNode]) {
        continue;
      }

      dfs(nxtNode);
      for (let i = 0; i < 3; i++) {
        // path: 부모 노드의 색에 따른 자신의 색
        // path[2][1] = 2 이면 2번 노드의 부모 노드가 1일 때 2번 노드는 2번 색
        if (dp[nxtNode][(i + 1) % 3] > dp[nxtNode][(i + 2) % 3]) {
          dp[curNode][i] += dp[nxtNode][(i + 1) % 3];
          path[nxtNode][i] = (i + 1) % 3;
        } else {
          dp[curNode][i] += dp[nxtNode][(i + 2) % 3];
          path[nxtNode][i] = (i + 2) % 3;
        }
      }
    }
  }

  function trace(curNode, curColor) {
    resColor[curNode] = curColor;
    for (const nxtNode of graph[curNode]) {
      if (resColor[nxtNode] !== -1) {
        continue;
      }
      trace(nxtNode, path[nxtNode][curColor]);
    }
  }

  dfs(1);
  let rootColor = -1;
  let resTotal = -1;
  for (let i = 0; i < 3; i++) {
    if (dp[1][i] > resTotal) {
      resTotal = dp[1][i];
      rootColor = i;
    }
  }

  const resColor = new Array(n + 1).fill(-1);
  trace(1, rootColor);

  return [
    resTotal,
    resColor
      .slice(1)
      .map((val) => (val === 0 ? 'R' : val === 1 ? 'G' : 'B'))
      .join(''),
  ].join('\n');
}

console.log(main(input));
