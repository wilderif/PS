// BOJ_16934
// 게임 닉네임

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

class TrieNode {
  constructor() {
    this.children = {};
    this.endOfWordCount = 0;
  }
}

class Trie {
  constructor() {
    this.root = new TrieNode();
  }

  insert(word) {
    let curNode = this.root;
    let ret = '';
    let flag = false;
    for (const char of word) {
      if (!flag) {
        ret += char;
      }
      if (!curNode.children.hasOwnProperty(char)) {
        curNode.children[char] = new TrieNode();
        flag = true;
      }
      curNode = curNode.children[char];
    }
    curNode.endOfWordCount++;
    if (flag || curNode.endOfWordCount === 1) {
      return ret;
    }
    return word + curNode.endOfWordCount.toString();
  }
}

function solution(inputArr) {
  const n = Number(inputArr[0]);
  const trie = new Trie();
  const res = [];
  for (const w of inputArr.slice(1)) {
    res.push(trie.insert(w));
  }

  return res.join('\n');
}

console.log(solution(input));
