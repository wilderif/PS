// 369게임

function solution(order) {
  return order
    .toString()
    .split("")
    .reduce((acc, cur) => {
      cur = Number(cur);
      if (cur && cur % 3 === 0) {
        acc += 1;
      }
      return acc;
    }, 0);
}
