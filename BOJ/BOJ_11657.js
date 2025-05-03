// BOJ_11657
// 타임머신

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function main(inputArr) {
  const [n, m] = inputArr[0].split(' ').map(Number);
  const edges = [];

  for (const el of inputArr.slice(1)) {
    const [a, b, c] = el.split(' ').map(Number);
    edges.push({ s: a, d: b, w: c });
  }

  function bellmanFord(start) {
    const dist = new Array(n + 1).fill(Infinity);
    dist[start] = 0;

    for (let i = 1; i < n + 1; i++) {
      let updated = false;

      for (const { s, d, w } of edges) {
        if (dist[s] === Infinity) {
          continue;
        }

        const newDist = dist[s] + w;

        if (newDist < dist[d]) {
          dist[d] = newDist;
          updated = true;
          if (i === n) {
            return -1;
          }
        }
      }

      if (!updated) {
        break;
      }
    }

    return dist
      .slice(2)
      .map((val) => (val === Infinity ? -1 : val))
      .join('\n');
  }

  return bellmanFord(1);
}

console.log(main(input));
