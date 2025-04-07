// BOJ_19585
// 전설

const fs = require('fs');
const filePath = process.platform === 'linux' ? 0 : './input.txt';
const input = fs.readFileSync(filePath, 'utf-8').trim().split('\n');

class TrieNode {
  constructor() {
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

  search(word, nicknameSet) {
    let curNode = this.root;

    for (let i = 0; i < Math.min(word.length - 1, 1000); i++) {
      const char = word[i];
      if (!curNode.children.hasOwnProperty(char)) {
        return false;
      }
      curNode = curNode.children[char];
      if (curNode.isEndOfWord) {
        const nickname = word.slice(i + 1);
        if (nicknameSet.has(nickname)) {
          return true;
        }
      }
    }

    return false;
  }
}

function main(inputArr) {
  const [c, n] = inputArr[0].split(' ').map(Number);
  const trie = new Trie();
  const nicknameSet = new Set();

  let line = 1;

  for (let i = 0; i < c; i++) {
    trie.insert(inputArr[line++]);
  }
  for (let i = 0; i < n; i++) {
    nicknameSet.add(inputArr[line++]);
  }

  const res = [];

  let q = Number(inputArr[line++]);
  while (q--) {
    res.push(trie.search(inputArr[line++], nicknameSet));
  }

  return res
    .map((val) => {
      return val === true ? 'Yes' : 'No';
    })
    .join('\n');
}

console.log(main(input));
