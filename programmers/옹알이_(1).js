// 옹알이_(1)

function solution(babbling) {
  let res = 0;

  const check = (babb) => {
    if (babb.length > 10) {
      return false;
    }
    const used = new Array(4).fill(false);
    for (let i = 0; i < babb.length; i++) {
      if (babb[i] === "a") {
        if (used[0]) {
          return false;
        } else {
          used[0] = true;
        }
        if (babb[i + 1] && babb[i + 1] === "y") {
          if (babb[i + 2] && babb[i + 2] === "a") {
            i += 2;
          } else {
            return false;
          }
        } else {
          return false;
        }
      } else if (babb[i] === "y") {
        if (used[1]) {
          return false;
        } else {
          used[1] = true;
        }
        if (babb[i + 1] && babb[i + 1] === "e") {
          i += 1;
        } else {
          return false;
        }
      } else if (babb[i] === "w") {
        if (used[2]) {
          return false;
        } else {
          used[2] = true;
        }
        if (babb[i + 1] && babb[i + 1] === "o") {
          if (babb[i + 2] && babb[i + 2] === "o") {
            i += 2;
          } else {
            return false;
          }
        } else {
          return false;
        }
      } else if (babb[i] === "m") {
        if (used[3]) {
          return false;
        } else {
          used[3] = true;
        }
        if (babb[i + 1] && babb[i + 1] === "a") {
          i += 1;
        } else {
          return false;
        }
      } else {
        return false;
      }
    }

    return true;
  };

  for (const s of babbling) {
    if (check(s)) {
      res++;
    }
    console.log(check(s));
    console.log();
  }

  return res;
}
