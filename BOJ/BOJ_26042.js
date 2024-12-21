// BOJ_26042
// 식당 입구 대기 줄

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

function solution(inputArr) {
  const n = Number(inputArr[0]);

  const queue = [];
  let head = 0;
  let tail = 0;

  let res1 = 0;
  let res2 = 0;
  for (let i = 0; i < n; i++) {
    const [a, b] = inputArr[i + 1].split(" ");
    if (b) {
      queue.push(b);
      tail++;
    } else {
      head++;
    }

    if (res1 <= tail - head) {
      if (res1 === tail - head) {
        res2 = Math.min(res2, queue[tail - 1]);
      } else {
        res2 = queue[tail - 1];
      }
      res1 = tail - head;
    }
  }
  console.log(res1, res2);
}

// console.log(solution(input));
solution(input);
