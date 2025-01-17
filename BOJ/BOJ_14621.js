// BOJ_14621
// 나만 안되는 연애

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
  const [n, m] = inputArr[0].split(' ').map(Number);
  const arr = [null, ...inputArr[1].split(' ')];
  const graph = Array.from({ length: n + 1 }, () => new Map());
  for (const el of inputArr.slice(2)) {
    const [u, v, d] = el.split(' ').map(Number);
    if (arr[u] === arr[v]) {
      continue;
    }
    if (graph[u].has(v) && graph[u].get(v) <= d) {
      continue;
    }
    graph[u].set(v, d);
    graph[v].set(u, d);
  }

  let res = 0;
  const used = new Array(n + 1).fill(false);
  const minHeap = new MinHeap();
  used[1] = true;
  for (const e of graph[1]) {
    minHeap.heapPush(e);
  }

  while (minHeap.getSize()) {
    const [cur, curCost] = minHeap.heapPop();
    if (used[cur]) {
      continue;
    }
    used[cur] = true;
    res += curCost;

    for (const e of graph[cur]) {
      if (used[e[0]]) {
        continue;
      }
      minHeap.heapPush(e);
    }
  }

  for (let i = 1; i <= n; i++) {
    if (!used[i]) {
      return -1;
    }
  }

  return res;
}

console.log(solution(input));
