// 문자열_밀기

function solution(A, B) {
  const n = A.length;

  for (let i = 0; i < n; i++) {
    const tmp = A.substr(n - i, n) + A.substr(0, n - i);

    if (tmp === B) {
      return i;
    }
  }

  return -1;
}
