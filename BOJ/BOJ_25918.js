// BOJ_25918
// 북극곰은 괄호를 찢어

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const s = inputArr[1].split("");

  let res = 0;
  const stack = [];

  for (const c of s) {
    if (c === "(") {
      if (stack.length === 0) {
        stack.push(c);
      } else {
        if (stack[stack.length - 1] === "(") {
          stack.push(c);
        } else {
          stack.pop();
        }
      }
    }
    if (c === ")") {
      if (stack.length === 0) {
        stack.push(c);
      } else {
        if (stack[stack.length - 1] === ")") {
          stack.push(c);
        } else {
          stack.pop();
        }
      }
    }
    res = Math.max(res, stack.length);
  }

  if (stack.length) {
    return -1;
  }

  return res;
}

console.log(solution(input));
