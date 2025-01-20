// BOJ_2307
// 도로검문

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
  const [n, m] = inputArr[0].split(' ').map(Number);
  const graph = Array.from({ length: n + 1 }, () => []);
  for (const el of inputArr.slice(1)) {
    const [a, b, t] = el.split(' ').map(Number);
    graph[a].push([b, t]);
    graph[b].push([a, t]);
  }

  const dijkstra = (notUsed) => {
    const dist = new Array(n + 1).fill(Infinity);
    const prev = new Array(n + 1).fill(0);
    const minHeap = new MinHeap();
    minHeap.heapPush([0, 1]);
    dist[1] = 0;

    while (minHeap.getSize()) {
      const [curDist, cur] = minHeap.heapPop();
      if (dist[cur] !== curDist) {
        continue;
      }

      for (const [nxt, nxtCost] of graph[cur]) {
        if (cur === notUsed[0] && nxt === notUsed[1]) {
          continue;
        }
        if (cur === notUsed[1] && nxt === notUsed[0]) {
          continue;
        }
        const nxtDist = curDist + nxtCost;
        if (dist[nxt] <= nxtDist) {
          continue;
        }
        dist[nxt] = nxtDist;
        minHeap.heapPush([nxtDist, nxt]);
        prev[nxt] = cur;
      }
    }

    return [dist[n], prev];
  };

  const [initialDist, prev] = dijkstra([-1, -1]);

  const usedPath = [];
  let curNode = n;
  while (prev[curNode] !== 0) {
    usedPath.push([prev[curNode], curNode]);
    curNode = prev[curNode];
  }

  let res = 0;
  for (const path of usedPath) {
    const retDist = dijkstra(path)[0];
    if (retDist === Infinity) {
      return -1;
    }
    res = Math.max(res, retDist - initialDist);
  }

  return res;
}

console.log(solution(input));
