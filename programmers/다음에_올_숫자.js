// 다음에_올_숫자

function solution(common) {
  const isArithmetic = common[0] + common[2] === common[1] * 2;
  if (isArithmetic) {
    return common[common.length - 1] + (common[1] - common[0]);
  }
  return common[common.length - 1] * (common[1] / common[0]);
}
