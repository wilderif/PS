// 삼각형의_완성조건_(2)

function solution(sides) {
  const diff = Math.abs(sides[0] - sides[1]);
  const sum = sides[0] + sides[1];

  return sum - diff - 1;
}
