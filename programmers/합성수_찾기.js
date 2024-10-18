// 합성수_찾기

function solution(n) {
  if (n <= 3) {
    return 0;
  }

  let primes = new Array(n + 1).fill(true);
  primes[0] = false;
  primes[1] = false;

  for (let i = 2; i * i <= n; i++) {
    if (primes[i]) {
      for (let j = i * i; j <= n; j += i) {
        primes[j] = false;
      }
    }
  }

  return primes.filter((prime) => !prime).length - 2;
}

console.log(solution(15)); // 4
