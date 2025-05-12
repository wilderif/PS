// 더_맵게

class MinHeap {
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

  heapPush(val) {
    this.heap.push(val);
    this.shiftUp();
  }

  heapPop() {
    if (this.getSize() === 0) {
      return false;
    }

    this.swap(1, this.getSize());
    const ret = this.heap.pop();
    this.shiftDown();

    return ret;
  }

  shiftUp() {
    let idx = this.getSize();
    while (idx > 1) {
      const parentIdx = Math.floor(idx / 2);
      if (this.heap[idx] > this.heap[parentIdx]) {
        break;
      }
      this.swap(idx, parentIdx);
      idx = parentIdx;
    }
  }

  shiftDown() {
    let idx = 1;
    while (idx * 2 <= this.getSize()) {
      const leftChildIdx = idx * 2;
      const rightChildIdx = idx * 2 + 1;

      const swapIdx =
        rightChildIdx <= this.getSize() &&
        this.heap[rightChildIdx] < this.heap[leftChildIdx]
          ? rightChildIdx
          : leftChildIdx;

      if (this.heap[idx] < this.heap[swapIdx]) {
        break;
      }

      this.swap(idx, swapIdx);
      idx = swapIdx;
    }
  }

  swap(idx1, idx2) {
    [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
  }
}

function solution(scoville, K) {
  const minHeap = new MinHeap();
  scoville.forEach((val) => {
    minHeap.heapPush(val);
  });

  let cnt = 0;
  while (minHeap.getSize() >= 2 && minHeap.peek() < K) {
    cnt++;
    const tmp1 = minHeap.heapPop();
    const tmp2 = minHeap.heapPop();
    minHeap.heapPush(tmp1 + tmp2 * 2);
  }

  if (minHeap.peek() >= K) {
    return cnt;
  }
  return -1;
}
