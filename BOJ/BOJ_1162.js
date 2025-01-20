// BOJ_1162
// 도로포장

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

class MinHeap {
  constructor() {
    this.heap = [null];
    this.compare = (a, b) => a[0] - b[0];
  }

  peek() {
    if (this.getSize === 0) {
      return false;
    } else {
      return this.heap[1];
    }
  }

  getSize() {
    return this.heap.length - 1;
  }

  swap(idx1, idx2) {
    [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
  }

  bubbleUp() {
    let idx = this.getSize();
    while (idx > 1) {
      const parentIdx = Math.floor(idx / 2);
      if (this.compare(this.heap[parentIdx], this.heap[idx]) <= 0) {
        break;
      }
      this.swap(idx, parentIdx);
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
      if (this.compare(this.heap[idx], this.heap[swapIdx]) <= 0) {
        break;
      }
      this.swap(idx, swapIdx);
      idx = swapIdx;
    }
  }

  heapPush(val) {
    this.heap.push(val);
    this.bubbleUp();
  }

  heapPop() {
    if (this.getSize() === 0) {
      return false;
    }
    this.swap(1, this.getSize());
    const ret = this.heap.pop();
    this.bubbleDown();
    return ret;
  }
}

function solution(inputArr) {
  const [n, m, k] = inputArr[0].split(' ').map(Number);
  const graph = Array.from({ length: n + 1 }, () => new Map());

  for (const el of inputArr.slice(1)) {
    const [a, b, c] = el.split(' ').map(Number);
    if (!graph[a].has(b) || graph[a].get(b) > c) {
      graph[a].set(b, c);
      graph[b].set(a, c);
    }
  }

  const dist = Array.from({ length: k + 1 }, () =>
    new Array(n + 1).fill(Infinity)
  );

  const minHeap = new MinHeap();
  minHeap.heapPush([0, 1, 0]);
  for (let i = 0; i <= k; i++) {
    dist[i][1] = 0;
  }

  while (minHeap.getSize()) {
    const [curCost, cur, delCnt] = minHeap.heapPop();
    if (dist[delCnt][cur] !== curCost) {
      continue;
    }

    for (const [nxt, nxtCost] of graph[cur].entries()) {
      const cost = curCost + nxtCost;
      if (dist[delCnt][nxt] > cost) {
        dist[delCnt][nxt] = cost;
        minHeap.heapPush([cost, nxt, delCnt]);
      }
      if (delCnt === k) {
        continue;
      }
      if (dist[delCnt + 1][nxt] > curCost) {
        dist[delCnt + 1][nxt] = curCost;
        minHeap.heapPush([curCost, nxt, delCnt + 1]);
      }
    }
  }

  let res = Infinity;
  for (let i = 0; i <= k; i++) {
    res = Math.min(res, dist[i][n]);
  }

  return res;
}

console.log(solution(input));
