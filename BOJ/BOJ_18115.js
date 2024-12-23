// BOJ_18115
// 카드 놓기

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

class Node {
  constructor(data) {
    this.data = data;
    this.prev = null;
    this.next = null;
  }
}

class Deque {
  constructor() {
    this.front = null;
    this.back = null;
    this.length = 0;
  }

  pushFront(data) {
    const node = new Node(data);
    if (this.isEmpty()) {
      this.front = node;
      this.back = node;
    } else {
      this.front.prev = node;
      node.next = this.front;
      this.front = node;
    }
    this.length++;
  }
  popFront() {
    if (this.isEmpty()) {
      return;
    } else {
      const ret = this.front.data;
      if (this.length === 1) {
        this.front = null;
        this.back = null;
      } else {
        this.front = this.front.next;
        this.front.prev = null;
      }
      this.length--;
      return ret;
    }
  }

  pushBack(data) {
    const node = new Node(data);
    if (this.isEmpty()) {
      this.front = node;
      this.back = node;
    } else {
      this.back.next = node;
      node.prev = this.back;
      this.back = node;
    }
    this.length++;
  }
  popBack() {
    if (this.isEmpty()) {
      return;
    } else {
      const ret = this.back.data;
      if (this.length === 1) {
        this.front = null;
        this.back = null;
      } else {
        this.back = this.back.prev;
        this.back.next = null;
      }
      this.length--;
      return ret;
    }
  }

  isEmpty() {
    return this.length === 0;
  }
}

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const arr = inputArr[1].split(" ").map((el) => Number(el));
  const res = new Array(n);
  const tmpArr = [];
  const deque = new Deque();
  for (let i = 1; i <= n; i++) {
    deque.pushBack(i);
  }

  for (const i of arr) {
    if (i === 1) {
      tmpArr.push(deque.popBack());
    } else if (i === 2) {
      const tmp = deque.popBack();
      tmpArr.push(deque.popBack());
      deque.pushBack(tmp);
    } else {
      tmpArr.push(deque.popFront());
    }
  }

  for (let i = 0; i < n; i++) {
    res[n - tmpArr[i]] = n - i;
  }

  return res.join(" ");
}

console.log(solution(input));
