// BOJ_1922
// 네트워크 연결

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

  getParentIdx(idx) {
    return Math.floor(idx / 2);
  }

  getLeftChildIdx(idx) {
    return idx * 2;
  }

  getRightChildIdx(idx) {
    return idx * 2 + 1;
  }

  peek() {
    return this.heap[1];
  }

  swap(idx1, idx2) {
    [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
  }

  bubbleUp() {
    let idx = this.getSize();
    while (idx !== 1) {
      const parentIdx = this.getParentIdx(idx);
      if (this.heap[idx][1] >= this.heap[parentIdx][1]) {
        break;
      }
      this.swap(idx, parentIdx);
      idx = parentIdx;
    }
  }

  bubbleDown() {
    let idx = 1;
    while (idx * 2 <= this.getSize()) {
      const [leftChildIdx, rightChildIdx] = [
        this.getLeftChildIdx(idx),
        this.getRightChildIdx(idx),
      ];
      const swapIdx =
        rightChildIdx <= this.getSize() &&
        this.heap[rightChildIdx][1] < this.heap[leftChildIdx][1]
          ? rightChildIdx
          : leftChildIdx;

      if (this.heap[idx][1] <= this.heap[swapIdx][1]) {
        break;
      }

      this.swap(idx, swapIdx);
      idx = swapIdx;
    }
  }

  heapPush(el) {
    this.heap.push(el);
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
  const n = Number(inputArr[0]);
  const m = Number(inputArr[1]);
  const graph = Array.from({ length: n + 1 }, () => []);
  for (const el of inputArr.slice(2)) {
    const [a, b, c] = el.split(' ').map(Number);
    if (a === b) {
      continue;
    }
    graph[a].push([b, c]);
    graph[b].push([a, c]);
  }

  const minHeap = new MinHeap();
  const used = new Set();
  let res = 0;

  for (const e of graph[1]) {
    minHeap.heapPush(e);
  }
  used.add(1);

  while (used.size < n) {
    const [cur, curCost] = minHeap.heapPop();
    if (used.has(cur)) {
      continue;
    }
    used.add(cur);
    res += curCost;

    for (const e of graph[cur]) {
      if (used.has(e[0])) {
        continue;
      }
      minHeap.heapPush(e);
    }
  }

  return res;
}

console.log(solution(input));
