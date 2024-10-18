// 공_던지기

function solution(numbers, k) {
  k = 2 * k - 2;

  return numbers[k % numbers.length];
}
