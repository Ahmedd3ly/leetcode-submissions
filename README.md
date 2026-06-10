# 💻 LeetCode Problem Solving Hub

Welcome to my central repository for tracking LeetCode algorithm progressions. All challenges are fetched, tested locally, and submitted completely via the command line.

---

## 📊 Progress Dashboard

![Total Solved](https://img.shields.io/badge/Solved-6%20%2F%20150-blue?style=for-the-badge&logo=leetcode)
![Easy](https://img.shields.io/badge/Easy-3-brightgreen?style=for-the-badge)
![Medium](https://img.shields.io/badge/Medium-2-orange?style=for-the-badge)
![Hard](https://img.shields.io/badge/Hard-1-red?style=for-the-badge)

### 📈 Current Milestone Tracks
- [ ] **Arrays & Hashing** (11 completed)
- [ ] **Two Pointers** (2 completed)
- [ ] **Linked List** (1 completed)
- [ ] **Sliding Window** (1 completed)
- [ ] **Top K / Heap Problems** (1 completed)
---

## 🗂️ Interactive Problem Index

*Click on a difficulty tier below to expand the list of solved algorithms.*

<details>
<summary>🟢 <b>Easy Tier Solutions</b> (Click to expand)</summary>
<br>

| # | Problem | Category | Language | Solution File |
|---|---|---|---|---|
| 1 | Two Sum | Array | Python | [1.two-sum.py](./Easy/Array/1.two-sum.py) |
| 121 | Best Time to Buy and Sell Stock | Array | Python | [121.best-time-to-buy-and-sell.py](./Easy/Array/121.best-time-to-buy-and-sell.py) |
| 125 | Valid Palindrome | Two Pointers | Python | [125.valid-palindrome.py](./Easy/Two%20Pointers/125.valid-palindrome.py) |
| 217 | Contains Duplicate | Array | Python | [217.contains-duplicate.py](./Easy/Array/217.contains-duplicate.py) |
| 242 | Valid Anagram | Hash Table | Python | [242.valid-anagram.py](./Easy/Hash%20Table/242.valid-anagram.py) |

</details>

<details>
<summary>🟡 <b>Medium Tier Solutions</b> (Click to expand)</summary>
<br>

| # | Problem | Category | Language | Solution File |
|---|---|---|---|---|
| 2 | Add Two Numbers | Linked List | Python | [2.add-two-numbers.py](./Medium/Linked%20List/2.add-two-numbers.py) |
| 3 | Longest Substr. Without Repeating Chars | Hash Table | Python | [3.longest-substring-without-repeating-characters.py](./Medium/Hash%20Table/3.longest-substring-without-repeating-characters.py) |
| 11 | Container With Most Water | Array / Two Pointers | Python | [11.container-with-most-water.py](./Medium/Array/11.container-with-most-water.py) |
| 15 | 3Sum | Array / Two Pointers | Python | [15.3sum.py](./Medium/Array/15.3sum.py) |
| 36 | Valid Sudoku | Hash Table | Python | [36.valid-sudoku.py](./Medium/Array/36.valid-sudoku.py) |
| 49 | Group Anagrams | Hash Table | Python | [49.group-anagrams.py](./Medium/Array/49.group-anagrams.py) |
| 128 | Longest Consecutive Sequence | Array / Hash Table | Python | [128.longest-consecutive-sequence.py](./Medium/Array/128.longest-consecutive-sequence.py) |
| 167 | Two Sum II - Input Array Is Sorted | Array / Two Pointers | Python | [167.two-sum-ii-input-array-is-sorted.py](./Medium/Array/167.two-sum-ii-input-array-is-sorted.py) |
| 238 | Product of Array Except Self | Array | Python | [238.product-of-array-except-self.py](./Medium/Array/238.product-of-array-except-self.py) |
| 271 | Encode and Decode Strings | Array / Design | Python | [271.encode-and-decode-strings.py](./Medium/Array/271.encode-and-decode-strings.py) |
| 347 | Top K Frequent Elements | Array / Hash Table | Python | [347.top-k-frequent-elements.py](./Medium/Array/347.top-k-frequent-elements.py) |

</details>

<details>
<summary>🔴 <b>Hard Tier Solutions</b> (Click to expand)</summary>
<br>

| # | Problem | Category | Language | Solution File |
|---|---|---|---|---|
| 42 | Trapping Rain Water | Array | Python | [42.trapping-rain-water.py](./Hard/Array/42.trapping-rain-water.py) |

</details>

---

## 🛠️ Local Environment Workflow

This repository runs seamlessly inside a decoupled Linux workflow using the following pipeline setup:

* **CLI Orchestration:** `@night-slayer18/leetcode-cli`
* **Editor Environment:** Neovim / LazyVim 
* **Execution Runtime:** Local file token encryption configuration

To pull a fresh problem and work locally:
```bash
leetcode pick <problem-id>
```

Run local tests:

```bash
leetcode test <problem-id>
```

Submit directly from terminal:

```bash
leetcode submit <problem-id>
```
