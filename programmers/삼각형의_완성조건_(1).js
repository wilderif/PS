// 삼각형의_완성조건_(1)

function solution(sides) {
  var answer = 0;
  sides.sort((a, b) => a - b);
  console.log(sides);
  if (sides[0] + sides[1] > sides[2]) {
    answer = 1;
  } else {
    answer = 2;
  }

  return answer;
}
