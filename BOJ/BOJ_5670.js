// BOJ_5670
// 휴대폰 자판

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

class TrieNode {
  constructor() {
    // key: char
    // value: TrieNode
    this.children = {};
    this.isEndOfWord = false;
  }
}

class Trie {
  constructor() {
    this.root = new TrieNode();
  }

  insert(word) {
    let curNode = this.root;
    for (const char of word) {
      if (!curNode.children.hasOwnProperty(char)) {
        curNode.children[char] = new TrieNode();
      }
      curNode = curNode.children[char];
    }
    curNode.isEndOfWord = true;
  }

  find(word) {
    let curNode = this.root;
    for (const char of word) {
      if (!curNode.children.hasOwnProperty(char)) {
        return false;
      }
      curNode = curNode.children[char];
    }
    return curNode.isEndOfWord;
  }

  // 첫 문자는 무조건 누름
  // 분기되는 경우 => Object.keys(curNode.children).length > 1
  // 현재 노드가 문자의 완성인 경우 => curNode.isEndOfWord
  calcButtonCount(word) {
    let curNode = this.root.children[word[0]];

    let ret = 1;
    for (const char of word.split('').slice(1)) {
      if (Object.keys(curNode.children).length > 1 || curNode.isEndOfWord) {
        ret++;
      }

      curNode = curNode.children[char];
    }

    return ret;
  }
}

function solution(inputArr) {
  const solve = (arr) => {
    const trie = new Trie();

    for (const s of arr) {
      trie.insert(s);
    }

    let ret = 0;

    for (const s of arr) {
      ret += trie.calcButtonCount(s);
    }

    return (ret / arr.length).toFixed(2);
  };

  let idx = 0;
  const res = [];
  while (idx < inputArr.length) {
    const n = Number(inputArr[idx]);
    res.push(solve(inputArr.slice(idx + 1, idx + n + 1)));
    idx += n + 1;
  }

  return res.join('\n');
}

console.log(solution(input));
