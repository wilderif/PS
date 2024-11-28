// 한_번만_등장한_문자

function solution(s) {
  const arr = s.split("");
  arr.sort();

  let res = "";
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === arr[i - 1] || arr[i] === arr[i + 1]) {
      continue;
    }
    res += arr[i];
  }

  return res;
}
