// 구슬을_나누는_경우의_수

function solution(balls, share) {
  let res = 1;
  for (let i = 0; i < balls - share; i++) {
    res *= balls - i;
    res /= i + 1;
  }

  return res;
}
