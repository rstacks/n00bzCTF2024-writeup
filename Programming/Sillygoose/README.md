# Sillygoose

## Description

There's no way you can guess my favorite number, you silly goose.

<code>nc 24.199.110.35 41199</code>

## Attachments

[sillygoose.py](attachments/sillygoose.py)

## Solution

- After connecting to the provided <code>nc</code> interface, we must guess a random number
between 0 and 10<sup>100</sup>. After guessing, we are told whether our answer is too small or too large,
then prompted to guess again. According to the provided source code, guessing the correct number
will yield the flag, but we must do so within 500 guesses and in less than 60 seconds.

- Given these constraints and the enormous range of possible guesses, completing this challenge
by hand is not feasible. So, I used the
[binary search algorithm](https://en.wikipedia.org/wiki/Binary_search) to quickly zero in on the
correct number. Here is a brief explanation of this algorithm: the first guess is the number halfway
between the minimum and maximum possible guesses (5<sup>99</sup> in this case). If this guess is too high, then
the next guess will be the number halfway between 0 and 5<sup>99</sup>. If this guess is too low, then
the next guess will be halfway between 5<sup>99</sup> and 10<sup>100</sup>. These decisions are repeated for each
subsequent guess, quickly narrowing the range in which the correct number resides until it is found.

- I wrote a [Python script](binary_searcher.py) that implements this algorithm. It uses
[nclib](https://nclib.readthedocs.io/en/latest/) to connect to the provided <code>nc</code>
interface and send/receive data. The script runs until it detects that the flag has been printed
by the <code>nc</code> interface.

## Flag

n00bz{y0u_4r3_4_sm4rt_51l1y_g0053}
