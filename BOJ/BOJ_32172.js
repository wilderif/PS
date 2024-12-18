// BOJ_32172
// 현권이와 신기한 수열

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const numSet = new Set();
  numSet.add(0);

  let prev = 0;
  for (let i = 1; i < n + 1; i++) {
    let next = prev - i;
    if (prev - i < 0 || numSet.has(prev - i)) {
      next = prev + i;
    }

    numSet.add(next);
    prev = next;
  }

  return prev;
}

console.log(solution(input));
