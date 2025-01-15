// BOJ_1967
// 트리의 지름

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const graph = Array.from({ length: n + 1 }, () => new Array());
  for (const el of inputArr.splice(1)) {
    const [p, c, w] = el.split(' ').map(Number);
    graph[p].push([c, w]);
    graph[c].push([p, w]);
  }

  const dfs = (node) => {
    const vis = new Array(n + 1).fill(false);
    const stack = [[node, 0]];
    vis[node] = true;
    const ret = [-1, -1];

    while (stack.length) {
      const [cur, curW] = stack.pop();
      let isLeaf = true;
      for (const [nxt, nxtW] of graph[cur]) {
        if (vis[nxt]) {
          continue;
        }
        stack.push([nxt, curW + nxtW]);
        vis[nxt] = true;
        isLeaf = false;
      }

      if (isLeaf) {
        if (ret[1] < curW) {
          ret[0] = cur;
          ret[1] = curW;
        }
      }
    }

    return ret;
  };

  const startNode = dfs(1)[0];

  return dfs(startNode)[1];
}

console.log(solution(input));
