// BOJ_21276
// 계보 복원가 호석

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const names = inputArr[1].split(' ');
  const m = Number(inputArr[2]);

  const graph = new Map();
  const indeg = new Map();
  for (const name of names) {
    graph.set(name, new Set());
    indeg.set(name, 0);
  }

  for (const el of inputArr.splice(3)) {
    const [c, p] = el.split(' ');
    graph.set(p, graph.get(p).add(c));
    indeg.set(c, indeg.get(c) + 1);
  }

  const resRoot = [];
  const resRel = [];

  const stack = [];
  for (const el of indeg) {
    if (el[1] === 0) {
      stack.push(el[0]);
      resRoot.push(el[0]);
    }
  }

  while (stack.length) {
    const cur = stack.pop();
    const children = [];
    for (const nxt of graph.get(cur)) {
      indeg.set(nxt, indeg.get(nxt) - 1);
      if (indeg.get(nxt) === 0) {
        children.push(nxt);
        stack.push(nxt);
      }
    }

    resRel.push([cur, children.length, children.sort().join(' ')]);
  }

  const res = [];
  res.push(resRoot.length);
  res.push(resRoot.sort().join(' '));
  for (const el of resRel.sort((a, b) => (a[0] < b[0] ? -1 : 1))) {
    res.push(el.join(' '));
  }

  return res.join('\n');
}

console.log(solution(input));
