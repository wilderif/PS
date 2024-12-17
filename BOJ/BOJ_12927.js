// BOJ_12927
// 배수 스위치

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

function solution(inputArr) {
  const inputStr = inputArr[0].split("");
  let cnt = 0;

  for (let i = 0; i < inputStr.length; i++) {
    if (inputStr[i] === "Y") {
      cnt++;
      for (let j = i; j < inputStr.length; j += i + 1) {
        if (inputStr[j] === "Y") {
          inputStr[j] = "N";
        } else {
          inputStr[j] = "Y";
        }
      }
    }
  }

  return cnt;
}

console.log(solution(input));
