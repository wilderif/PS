// 완주하지_못한_선수

function solution(participant, completion) {
  const pMap = new Map();
  for (const p of participant) {
    pMap.set(p, pMap.has(p) ? pMap.get(p) + 1 : 1);
  }
  for (const c of completion) {
    pMap.set(c, pMap.get(c) - 1);
  }

  for (const [key, value] of pMap) {
    if (value !== 0) {
      return key;
    }
  }
}
