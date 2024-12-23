// 정수내림차순으로_배치하기

function solution(n) {
  return Number(
    n
      .toString()
      .split("")
      .sort((a, b) => Number(b) - Number(a))
      .join("")
  );
}
