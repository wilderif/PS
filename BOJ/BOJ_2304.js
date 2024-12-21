// BOJ_2304
// 창고 다각형

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

function solution(inputArr) {
  const n = inputArr[0];
  const arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(inputArr[i + 1].split(" ").map((el) => Number(el)));
  }

  arr.sort((a, b) => a[0] - b[0]);

  let cur1 = [0, 0];
  let cur2 = [0, 0];
  let res = 0;
  for (let i = 0; i < n; i++) {
    if (arr[i][1] > cur1[1]) {
      res += (arr[i][0] - cur1[0]) * cur1[1];
      cur1 = arr[i];
    }

    const reversedIdx = n - i - 1;
    if (arr[reversedIdx][1] >= cur2[1]) {
      res += (cur2[0] - arr[reversedIdx][0]) * cur2[1];
      cur2 = arr[reversedIdx];
    }
  }

  res += cur1[1];

  return res;
}

console.log(solution(input));
