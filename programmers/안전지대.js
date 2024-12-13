// 안전지대

function solution(board) {
  const dx = [0, 0, -1, -1, -1, 1, 1, 1];
  const dy = [-1, 1, 0, -1, 1, -1, 0, 1];

  const n = board.length;

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (board[i][j] === 1) {
        for (let k = 0; k < 8; k++) {
          const nx = i + dx[k];
          const ny = j + dy[k];
          if (0 <= nx && nx < n && 0 <= ny && ny < n) {
            if (board[nx][ny] === 0) {
              board[nx][ny] = 2;
            }
          }
        }
      }
    }
  }

  let res = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (board[i][j] === 0) {
        res++;
      }
    }
  }

  return res;
}
