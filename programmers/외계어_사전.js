// 외계어_사전

function solution(spell, dic) {
  spell = new Set(spell);

  for (s of dic) {
    const tmpSpell = new Set(spell);
    let flag = true;
    s = s.split("");

    for (c of s) {
      if (!spell.has(c) || !tmpSpell.has(c)) {
        flag = false;
        break;
      }
      tmpSpell.delete(c);
    }

    if (tmpSpell.size) {
      continue;
    }

    if (flag) {
      return 1;
    }
  }

  return 2;
}
