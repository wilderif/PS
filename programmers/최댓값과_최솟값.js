// 최댓값과_최솟값

function solution(s) {
  const arr = s
    .split(" ")
    .map((item) => Number(item))
    .sort((a, b) => a - b);

  return `${arr[0]} ${arr[arr.length - 1]}`;
}
