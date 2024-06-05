// 직사각형_넓이_구하기

function solution(dots) {
  dots.sort((a, b) => a[0] - b[0]);
  return Math.abs(dots[0][0] - dots[3][0]) * Math.abs(dots[0][1] - dots[1][1]);
}
