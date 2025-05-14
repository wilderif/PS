// 가장_큰_수

function solution(numbers) {
  const res = numbers
    .map(String)
    .sort((a, b) => Number(b + a) - Number(a + b))
    .join('');

  return res[0] === '0' ? '0' : res;
}
