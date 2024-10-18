// 팩토리얼

function solution(n) {
  let tmp = 1;
  for (let i = 1; i <= 11; i++) {
    tmp *= i;
    if (tmp > n) {
      return i - 1;
    }
  }
}

console.log(solution(1));
