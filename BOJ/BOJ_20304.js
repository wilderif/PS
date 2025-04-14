// BOJ_20304
// 비밀번호 제작

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function main(inputArr) {
  const n = Number(inputArr[0]);
  const m = Number(inputArr[1]);
  const arr = inputArr[2].split(' ').map(Number);
  const bitRange = Math.floor(Math.log2(n)) + 1;

  const bfs = (start) => {
    const vis = new Array(n + 1).fill(-1);
    for (const s of start) {
      vis[s] = 0;
    }
    let q = [...start];
    let depth = 1;

    while (q.length) {
      const nq = [];

      for (const cur of q) {
        for (let i = 0; i < bitRange; i++) {
          const tmp = cur ^ (1 << i);

          if (tmp > n) {
            continue;
          }
          if (vis[tmp] !== -1) {
            continue;
          }
          vis[tmp] = depth;
          nq.push(tmp);
        }
      }

      depth++;
      q = nq;
    }

    return vis;
  };

  const res = bfs(arr);

  return Math.max(...res);
}

console.log(main(input));
s;
