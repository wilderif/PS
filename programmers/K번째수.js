// K번째수

function solution(array, commands) {
  const res = [];

  for (const [i, j, k] of commands) {
    res.push(array.slice(i - 1, j).sort((a, b) => a - b)[k - 1]);
  }

  return res;
}
