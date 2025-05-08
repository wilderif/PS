// 가장_먼_노드

function solution(n, edge) {
  const graph = Array.from({ length: n + 1 }, () => []);
  for (const [u, v] of edge) {
    graph[u].push(v);
    graph[v].push(u);
  }

  const bfs = (start) => {
    const vis = new Array(n + 1).fill(false);
    let q = [start];
    vis[start] = true;

    while (q.length) {
      const nq = [];
      for (const cur of q) {
        for (const nxt of graph[cur]) {
          if (vis[nxt]) {
            continue;
          }
          vis[nxt] = true;
          nq.push(nxt);
        }
      }
      if (nq.length === 0) {
        return q.length;
      }
      q = nq;
    }
  };

  return bfs(1);
}
