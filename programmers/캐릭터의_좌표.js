// 캐릭터의_좌표

function solution(keyinput, board) {
  const limit1 = (board[0] - 1) / 2;
  const limit2 = (board[1] - 1) / 2;
  const curPosition = [0, 0];

  for (const command of keyinput) {
    if (command === "left") {
      if (curPosition[0] !== -limit1) {
        curPosition[0] -= 1;
      }
    }
    if (command === "right") {
      if (curPosition[0] !== limit1) {
        curPosition[0] += 1;
      }
    }
    if (command === "up") {
      if (curPosition[1] !== limit2) {
        curPosition[1] += 1;
      }
    }
    if (command === "down") {
      if (curPosition[1] !== -limit2) {
        curPosition[1] -= 1;
      }
    }
  }

  return curPosition;
}
