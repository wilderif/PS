// 유한소수_판별하기

function solution(a, b) {
  let devider = 2;
  while (devider <= a && devider <= b) {
    if (a % devider === 0 && b % devider === 0) {
      a /= devider;
      b /= devider;
    } else {
      devider++;
    }
  }

  while (b % 2 === 0) {
    b /= 2;
  }

  while (b % 5 === 0) {
    b /= 5;
  }

  return b === 1 ? 1 : 2;
}
