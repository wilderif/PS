// BOJ_1068
// 트리

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const parent = inputArr[1].split(' ').map(Number);
  const toDel = Number(inputArr[2]);
  const children = Array.from({ length: n }, () => new Array());
  let root = -1;
  for (let i = 0; i < n; i++) {
    if (parent[i] === -1) {
      root = i;
      continue;
    }
    children[parent[i]].push(i);
  }

  if (toDel === root) {
    return 0;
  }

  let res = 0;
  let stack = [root];

  while (stack.length) {
    const cur = stack.pop();
    let isLeaf = true;
    for (const nxt of children[cur]) {
      if (nxt === toDel) {
        continue;
      }
      isLeaf = false;
      stack.push(nxt);
    }
    if (isLeaf) {
      res++;
    }
  }

  return res;
}

console.log(solution(input));
