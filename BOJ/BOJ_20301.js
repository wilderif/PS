// BOJ_20301
// 반전 요세푸스

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
  const [n, k, m] = inputArr[0].split(" ").map((el) => Number(el));
  const deque = new Deque();
  for (let i = 1; i <= n; i++) {
    deque.pushBack(i);
  }

  let flag = true;
  let cnt = 0;
  while (deque.length) {
    const lotate = k % deque.length;
    for (let i = 0; i < lotate; i++) {
      if (flag) {
        deque.pushBack(deque.popFront());
      } else {
        deque.pushFront(deque.popBack());
      }
    }

    if (flag) {
      console.log(deque.popBack());
    } else {
      console.log(deque.popFront());
    }

    cnt++;
    if (cnt === m) {
      flag = !flag;
      cnt = 0;
    }
  }
}

solution(input);
// console.log(solution(input));
