// 나머지가_1이_되는_수_찾기

function solution(n) {
  for (let i = 1; i < n; i++) {
    if (n % i === 1) {
      return i;
    }
  }
}
