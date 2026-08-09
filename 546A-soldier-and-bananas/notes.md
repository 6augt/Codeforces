# 546A — Soldier and Bananas

![Rating](https://img.shields.io/badge/Rating-800-green)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Topic-Math-orange](https://img.shields.io/badge/Topic-Math-orange)
![Topic-Implementation-orange](https://img.shields.io/badge/Topic-Implementation-orange)

> You can find problem 546A [here](https://codeforces.com/problemset/problem/546/A).

## Instructions

> A soldier wants to buy `w` bananas in the shop. He has to pay `k` dollars for the first banana, `2k` dollars for the second one and so on (in other words, he has to pay `i · k` dollars for the `i`-th banana).
>
> He has `n` dollars. How many dollars does he have to borrow from his friend soldier to buy `w` bananas?
>
> **Input:**
> The first line contains three positive integers `k`, `n`, `w` (`1 ≤ k, w ≤ 1000`, `0 ≤ n ≤ 10⁹`), the cost of the first banana, the initial number of dollars the soldier has, and the number of bananas he wants.
>
> **Output:**
> Output one integer — the amount of dollars that the soldier must borrow from his friend. If he doesn't have to borrow money, output `0`.

## Steps to solve it

When it comes to Codeforces problems, I always try to understand what is being said first and then try to code it.

If someone were to ask me what steps they should take to solve any problem, I'd say:

1. Read through the instructions carefully. Take your time if needed.
2. Once you understand the majority of the problem, start by writing the required input from the problem.
3. Use logic and reasoning to go from the input to the required output.


## My Reasoning

Let's skim through the entire problem step by step!

> The first line contains three positive integers `k`, `n`, `w` (`1 ≤ k, w ≤ 1000`, `0 ≤ n ≤ 10⁹`).

OK. This essentially means that one line has to contain three integers. We can read them using `input()`.

Since the problem says that the three integers are given on the same line, we can use `.split()` to separate them and `map()` to convert them into integers.

❌ `a, b, c = input(), input(), input()`

✅ `k, n, w = map(int, input().split())`

The code states that:

* `w` is the number of bananas we want.
* `n` is the initial number of dollars we have.
* `k` is the cost of the first banana.

Now that we have the first line, we can continue our code!

> He has to pay `k` dollars for the first banana, `2k` dollars for the second one and so on.

If a problem says that something needs to increase by `1` for a certain amount of times, then we know we probably need to use a `for` loop!

In this case, our theory is proven by the problem statement itself:

> (In other words, he has to pay `i · k` dollars for the `i`-th banana.)

So, for every banana we want, we must multiply the cost of the first banana, `k`, by `i`!

✅ `for i in range(1, w + 1):`

❌ `for i in range(w):`

While `range(w)` could technically be used if we adjusted the calculation, it gives us the values `0, 1, 2, ..., w - 1`. The problem wants the banana numbers to start at `1`, so `range(1, w + 1)` is more convenient.

Now, there are several ways we can continue the `for` loop. In my case, I decided to create a new variable called `price`:

`price = k * i`

This calculates the price of the current banana. Since `i` increases by `1` every iteration, the price also increases by `k` each time.

With that done, it was time to simulate our character spending money to buy the aforementioned banana!

`n = n - price`

So, as `i` keeps increasing, `price` also increases, and our initial budget decreases.

Once we've bought all the desired bananas and the `for` loop ends, we can check how much money we have left:

`print(max(0, -n))`

If `n` is negative, `-n` represents the amount of money we need to borrow.

Otherwise, `n` is zero or positive, meaning we don't need to borrow anything. In that case, `max(0, -n)` gives us `0`.

## My mistakes

When trying to print the output, I actually made a slight error:

`print(abs(n))`

At first, I thought that if we had to borrow money and ended up with a negative `n`, we could simply use `abs(n)` to get the amount we owed.

For example, if `n = -20`, then `abs(n)` gives us `20`, which is correct.

However, this doesn't work if `n` is positive. If we have `$20` left, `abs(n)` would give us `20`, even though we don't need to borrow any money.

So instead, we need to make sure that we output `0` whenever `n` is positive:

`print(max(0, -n))`

## Solution

```python
k, n, w = map(int, input().split())

for i in range(1, w + 1):
    price = k * i
    n = n - price

print(max(0, -n))
```

## Final Thoughts

I'll be honest, I had to try twice before finally getting the correct answer in `solution.py`!

If you found another way to solve this problem, feel free to let me know! I'd love to hear how you approached it and see if there's anything I could learn from your solution.

Thanks for reading, and good luck with your next problem!

**Best regards,**
**6augt**

