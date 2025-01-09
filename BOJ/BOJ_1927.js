// BOJ_1927
// 최소 힙

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

function solution(inputArr) {
  const heap = new Array(100001).fill(0);
  let size = 0;

  const heapPush = (item) => {
    heap[++size] = item;
    let nodeIdx = size;
    while (true) {
      const parrentNodeIdx = Math.floor(nodeIdx / 2);
      if (heap[nodeIdx] < heap[parrentNodeIdx]) {
        [heap[nodeIdx], heap[parrentNodeIdx]] = [
          heap[parrentNodeIdx],
          heap[nodeIdx],
        ];

        nodeIdx = parrentNodeIdx;
      } else {
        break;
      }
    }
  };

  const heapPop = () => {
    if (!size) {
      return 0;
    }

    const ret = heap[1];
    [heap[1], heap[size]] = [heap[size], heap[1]];
    size--;

    let nodeIdx = 1;
    while (true) {
      const childNodeIdx1 = nodeIdx * 2;
      const childNodeIdx2 = nodeIdx * 2 + 1;
      let swapIdx = null;

      if (childNodeIdx1 <= size && heap[childNodeIdx1] < heap[nodeIdx]) {
        swapIdx = childNodeIdx1;
      }
      if (
        childNodeIdx2 <= size &&
        heap[childNodeIdx2] <
          (swapIdx === null ? heap[nodeIdx] : heap[childNodeIdx1])
      ) {
        swapIdx = childNodeIdx2;
      }

      if (swapIdx === null) {
        break;
      }

      [heap[nodeIdx], heap[swapIdx]] = [heap[swapIdx], heap[nodeIdx]];
      nodeIdx = swapIdx;
    }

    return ret;
  };

  const n = Number(inputArr[0]);
  const cmdArr = inputArr.slice(1).map(Number);
  const res = [];

  for (el of cmdArr) {
    if (el === 0) {
      res.push(heapPop());
    } else {
      heapPush(el);
    }
  }

  return res.join('\n');
}

console.log(solution(input));
