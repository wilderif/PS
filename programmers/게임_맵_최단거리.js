// 게임_맵_최단거리

function solution(maps) {
  const n = maps.length;
  const m = maps[0].length;

  const bfs = (start) => {
    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];
    const vis = Array.from({ length: n }, () => new Array(m).fill(false));
    let q = [start];
    vis[start[0]][start[1]] = true;
    let depth = 1;

    while (q.length) {
      const nq = [];
      depth++;
      for (const [x, y] of q) {
        for (let d = 0; d < 4; d++) {
          const nx = x + dx[d];
          const ny = y + dy[d];

          if (!(0 <= nx && nx < n && 0 <= ny && ny < m)) {
            continue;
          }
          if (maps[nx][ny] === 0) {
            continue;
          }
          if (vis[nx][ny]) {
            continue;
          }
          vis[nx][ny] = true;
          nq.push([nx, ny]);
        }
      }

      if (vis[n - 1][m - 1]) {
        return depth;
      }

      q = nq;
    }

    return -1;
  };

  return bfs([0, 0]);
}
