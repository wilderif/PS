// BOJ_22865
// 가장 먼 곳

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

class MinHeap {
  constructor() {
    this.heap = [null];
  }

  getSize() {
    return this.heap.length - 1;
  }

  heapPush(x) {
    this.heap.push(x);
    this.bubbleUp();
  }

  heapPop() {
    if (this.getSize() === 0) {
      return false;
    }

    [this.heap[1], this.heap[this.getSize()]] = [
      this.heap[this.getSize()],
      this.heap[1],
    ];

    const ret = this.heap.pop();

    this.bubbleDown();

    return ret;
  }

  bubbleUp() {
    let idx = this.getSize();
    while (idx > 1) {
      const parentIdx = Math.floor(idx / 2);
      if (this.heap[parentIdx][0] < this.heap[idx][0]) {
        break;
      }
      [this.heap[idx], this.heap[parentIdx]] = [
        this.heap[parentIdx],
        this.heap[idx],
      ];

      idx = parentIdx;
    }
  }

  bubbleDown() {
    let idx = 1;
    while (idx * 2 <= this.getSize()) {
      const leftChildIdx = idx * 2;
      const rightChildIdx = idx * 2 + 1;

      const swapIdx =
        rightChildIdx <= this.getSize() &&
        this.heap[rightChildIdx][0] < this.heap[leftChildIdx][0]
          ? rightChildIdx
          : leftChildIdx;

      if (this.heap[idx][0] <= this.heap[swapIdx][0]) {
        break;
      }

      [this.heap[idx], this.heap[swapIdx]] = [
        this.heap[swapIdx],
        this.heap[idx],
      ];

      idx = swapIdx;
    }
  }
}

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const [a, b, c] = inputArr[1].split(' ').map(Number);
  const m = Number(inputArr[2]);
  const graph = Array.from({ length: n + 1 }, () => new Map());

  for (const el of inputArr.slice(3)) {
    const [d, e, l] = el.split(' ').map(Number);
    if (!graph[d].has(e) || graph[d].get(e) > l) {
      graph[d].set(e, l);
      graph[e].set(d, l);
    }
  }

  const dijkstra = (start) => {
    const dist = new Array(n + 1).fill(Infinity);
    const minHeap = new MinHeap();
    minHeap.heapPush([0, start]);
    dist[start] = 0;

    while (minHeap.getSize()) {
      const [curDist, cur] = minHeap.heapPop();
      if (dist[cur] < curDist) {
        continue;
      }
      for (const [nxt, nxtDist] of graph[cur]) {
        const distance = curDist + nxtDist;
        if (distance > dist[nxt]) {
          continue;
        }
        dist[nxt] = distance;
        minHeap.heapPush([distance, nxt]);
      }
    }

    return dist;
  };

  const distA = dijkstra(a);
  const distB = dijkstra(b);
  const distC = dijkstra(c);

  let check = 0;
  let res = 0;
  for (let i = 1; i <= n; i++) {
    if (Math.min(distA[i], distB[i], distC[i]) > check) {
      check = Math.min(distA[i], distB[i], distC[i]);
      res = i;
    }
  }

  return res;
}

console.log(solution(input));
