// BOJ_1655
// 가운데를 말해요

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

class BaseHeap {
  constructor() {
    this.heap = [null];
  }

  getSize() {
    return this.heap.length - 1;
  }

  peek() {
    if (this.getSize() === 0) {
      return false;
    }

    return this.heap[1];
  }

  swap(idx1, idx2) {
    [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
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
}

class MinHeap extends BaseHeap {
  constructor() {
    super();
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

  bubbleUp() {
    let idx = this.getSize();
    while (idx !== 1) {
      const parentIdx = this.getParentIdx(idx);
      if (this.heap[idx] >= this.heap[parentIdx]) {
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

      let swapIdx =
        rightChildIdx <= this.getSize() &&
        this.heap[rightChildIdx] < this.heap[leftChildIdx]
          ? rightChildIdx
          : leftChildIdx;

      if (this.heap[idx] <= this.heap[swapIdx]) {
        break;
      }
      this.swap(idx, swapIdx);
      idx = swapIdx;
    }
  }
}

class MaxHeap extends BaseHeap {
  constructor() {
    super();
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

  bubbleUp() {
    let idx = this.getSize();
    while (idx !== 1) {
      const parentIdx = this.getParentIdx(idx);
      if (this.heap[idx] <= this.heap[parentIdx]) {
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

      let swapIdx =
        rightChildIdx <= this.getSize() &&
        this.heap[rightChildIdx] > this.heap[leftChildIdx]
          ? rightChildIdx
          : leftChildIdx;

      if (this.heap[idx] >= this.heap[swapIdx]) {
        break;
      }
      this.swap(idx, swapIdx);
      idx = swapIdx;
    }
  }
}

function solution(inputArr) {
  const minHeap = new MinHeap();
  const maxHeap = new MaxHeap();

  const n = Number(inputArr[0]);
  const res = [];
  let flag = true;
  for (const el of inputArr.slice(1).map(Number)) {
    if (flag) {
      if (minHeap.getSize() && el > minHeap.peek()) {
        maxHeap.heapPush(minHeap.heapPop());
        minHeap.heapPush(el);
      } else {
        maxHeap.heapPush(el);
      }
    } else {
      if (maxHeap.getSize() && el < maxHeap.peek()) {
        minHeap.heapPush(maxHeap.heapPop());
        maxHeap.heapPush(el);
      } else {
        minHeap.heapPush(el);
      }
    }

    flag = !flag;
    res.push(maxHeap.peek());
  }

  return res.join('\n');
}

console.log(solution(input));
