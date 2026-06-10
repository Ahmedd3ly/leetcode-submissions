# 💻 LeetCode Problem Solving Hub

Welcome to my central repository for tracking LeetCode algorithm progressions. All challenges are fetched, tested locally, and submitted completely via the command line.

---

## 📊 Progress Dashboard

![Total Solved](https://img.shields.io/badge/Solved-6%20%2F%20150-blue?style=for-the-badge&logo=leetcode)
![Easy](https://img.shields.io/badge/Easy-3-brightgreen?style=for-the-badge)
![Medium](https://img.shields.io/badge/Medium-2-orange?style=for-the-badge)
![Hard](https://img.shields.io/badge/Hard-1-red?style=for-the-badge)

### 📈 Current Milestone Tracks
- [ ] **Arrays & Hashing** (3 completed)
- [ ] **Two Pointers** (1 completed)
- [ ] **Linked List** (1 completed)
- [ ] **Sliding Window / Hash Table** (1 completed)

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

</details>

<details>
<summary>🟡 <b>Medium Tier Solutions</b> (Click to expand)</summary>
<br>

| # | Problem | Category | Language | Solution File |
|---|---|---|---|---|
| 2 | Add Two Numbers | Linked List | Python | [2.add-two-numbers.py](./Medium/Linked%20List/2.add-two-numbers.py) |
| 3 | Longest Substr. Without Repeating Chars | Hash Table | Python | [3.longest-substring-without-repeating-characters.py](./Medium/Hash%20Table/3.longest-substring-without-repeating-characters.py) |

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
