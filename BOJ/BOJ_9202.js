// BOJ_9202
// Boggle

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

class TrieNode {
  constructor() {
    this.children = new Map();
    this.isEndOfWord = false;
    this.point = 0;
  }
}

class Trie {
  constructor() {
    this.root = new TrieNode();
  }

  insert(word) {
    let curNode = this.root;
    for (const char of word) {
      if (!curNode.children.has(char)) {
        curNode.children.set(char, new TrieNode());
      }
      curNode = curNode.children.get(char);
    }

    curNode.isEndOfWord = true;
    curNode.point = this.getPoint(word.length);
  }

  search(word) {
    let curNode = this.root;

    for (const char of word) {
      if (!curNode.children.has(char)) {
        return [false, 0, false];
      }
      curNode = curNode.children.get(char);
    }

    return [curNode.isEndOfWord, curNode.point, true];
  }

  getPoint(wordLength) {
    if (wordLength <= 2) return 0;
    if (wordLength <= 4) return 1;
    if (wordLength === 5) return 2;
    if (wordLength === 6) return 3;
    if (wordLength === 7) return 5;
    if (wordLength === 8) return 11;
  }
}

function solveCase(trie, board) {
  const dx = [-1, -1, -1, 1, 1, 1, 0, 0];
  const dy = [-1, 0, 1, -1, 0, 1, -1, 1];
  const used = Array.from({ length: 4 }, () => new Array(4).fill(false));

  const backtracking = (x, y, used, curWord, tmp_res) => {
    if (curWord.length > 8) {
      return;
    }

    [isEndOfWord, point, isPrefix] = trie.search(curWord);
    if (!isPrefix) {
      return;
    }
    if (isEndOfWord) {
      const curWordString = curWord.join('');
      if (!tmp_res.foundWords.has(curWordString)) {
        tmp_res.totalPoint += point;
        if (
          curWord.length > tmp_res.longestWord.length ||
          (curWord.length === tmp_res.longestWord.length &&
            curWordString < tmp_res.longestWord)
        ) {
          tmp_res.longestWord = curWordString;
        }
        tmp_res.foundWords.add(curWordString);
      }
    }

    for (let d = 0; d < 8; d++) {
      const nx = x + dx[d];
      const ny = y + dy[d];
      if (!(0 <= nx && nx < 4 && 0 <= ny && ny < 4)) {
        continue;
      }
      if (used[nx][ny]) {
        continue;
      }
      used[nx][ny] = true;
      curWord.push(board[nx][ny]);
      backtracking(nx, ny, used, curWord, tmp_res);
      used[nx][ny] = false;
      curWord.pop(board[nx][ny]);
    }
  };

  const tmp_res = {
    totalPoint: 0,
    longestWord: '',
    foundWords: new Set(),
  };

  for (let x = 0; x < 4; x++) {
    for (let y = 0; y < 4; y++) {
      used[x][y] = true;
      const curWord = [board[x][y]];
      backtracking(x, y, used, curWord, tmp_res);
      used[x][y] = false;
    }
  }

  return tmp_res;
}

function solution(inputArr) {
  const w = Number(inputArr[0]);
  const trie = new Trie();
  let line = 1;
  while (line < 1 + w) {
    trie.insert(inputArr[line++]);
  }
  line++;

  const res = [];
  let b = Number(inputArr[line++]);
  while (b--) {
    const board = [];
    for (i = 0; i < 4; i++) {
      board.push(inputArr[line++].split(''));
    }
    line++;

    const tmp_res = solveCase(trie, board);

    res.push(
      [tmp_res.totalPoint, tmp_res.longestWord, tmp_res.foundWords.size].join(
        ' '
      )
    );
  }

  return res.join('\n');
}

console.log(solution(input));
