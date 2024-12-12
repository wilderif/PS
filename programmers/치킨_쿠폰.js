// 치킨_쿠폰

function solution(chicken) {
  let res = 0;
  let coupon = chicken;

  while (1) {
    if (coupon < 10) {
      return res;
    }
    const tmp = Math.floor(coupon / 10);
    res += tmp;
    coupon %= 10;
    coupon += tmp;
  }
}
