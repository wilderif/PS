// 평행

function solution(dots) {
  for (let i = 1; i < 4; i++) {
    grad1 = (dots[0][1] - dots[i][1]) / (dots[0][0] - dots[i][0]);
    tmpY = 0;
    tmpX = 0;
    for (let j = 1; j < 4; j++) {
      if (j === i) {
        continue;
      }
      tmpY = -tmpY - dots[j][1];
      tmpX = -tmpX - dots[j][0];
    }

    grad2 = tmpY / tmpX;

    if (grad1 === grad2) {
      return 1;
    }
  }
  return 0;
}
