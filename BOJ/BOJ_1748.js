// BOJ_1748
// 수 이어 쓰기 1

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

function solution(inputArr) {
  const n = Number(inputArr[0]);
  let nn = n;
  let res = 0;
  let cnt = 0;
  while (nn) {
    cnt++;
    nn = Math.floor(nn / 10);
  }

  let mul = 9;
  for (let i = 1; i < cnt; i++) {
    res += mul * i;
    mul *= 10;
  }

  res += cnt * (n - 10 ** (cnt - 1) + 1);

  return res;
}

console.log(solution(input));
