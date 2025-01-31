// BOJ_4195
// 친구 네트워크

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  let t = Number(inputArr[0]);
  let line = 1;

  const res = [];
  while (t--) {
    const f = Number(inputArr[line]);

    const parentMap = new Map();
    const sizeMap = new Map();

    const find = (x) => {
      if (parentMap.get(x) !== x) {
        parentMap.set(x, find(parentMap.get(x)));
      }
      return parentMap.get(x);
    };

    const union = (u, v) => {
      u = find(u);
      v = find(v);

      if (u === v) {
        return sizeMap.get(u);
      }

      if (sizeMap.get(u) < sizeMap.get(v)) {
        [u, v] = [v, u];
      }

      sizeMap.set(u, sizeMap.get(u) + sizeMap.get(v));
      parentMap.set(v, u);

      return sizeMap.get(u);
    };

    for (const el of inputArr.slice(line + 1, line + f + 1)) {
      const [a, b] = el.split(' ');
      if (!parentMap.get(a)) {
        parentMap.set(a, a);
        sizeMap.set(a, 1);
      }
      if (!parentMap.get(b)) {
        parentMap.set(b, b);
        sizeMap.set(b, 1);
      }

      res.push(union(a, b));
    }

    line += f + 1;
  }

  return res.join('\n');
}

console.log(solution(input));
