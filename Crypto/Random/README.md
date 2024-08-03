# Random

## Description

I hid my password behind an impressive sorting machine. The machine is very luck based,
or **is it**?!?!?!?

<code>nc challs.n00bzunit3d.xyz 10418</code>

## Attachments

[server.cpp](attachments/server.cpp)

## Solution

- I started by examining the source code behind the provided <code>nc</code> interface. The user
is asked to provide a string with at least 10 unique characters. That string is then shuffled
and passed to the function <code>amazingcustomsortingalgorithm()</code>.

- This function checks if the characters of the shuffled string are in alphabetical order. If they are,
then the flag is revealed. Otherwise, the string is shuffled again and the function repeats. If
<code>amazingcustomsortingalgorithm()</code> completes 69 repetitions without
finding a sorted string, the program ends and the flag is not revealed.

- The challenge description and parts of the source code hint that the random shuffling of the string
is not truly random. Indeed, the source code uses <code>std::random_shuffle()</code> to shuffle
the string. By default, this function uses <code>rand()</code> in order to randomize the swaps that
take place during the shuffle. In C++, one must "seed" the <code>rand()</code> function before using
it. If <code>rand()</code> is not seeded with a new number, then it will return the
**exact same sequence** every time it is used.

- As we can see in <code>server.cpp</code>, there is no seeding that occurs before
<code>random_shuffle()</code> is called. Sure enough, every time I provided the string
"abcdefghij" to the <code>nc</code> interface, it was *always* randomly shuffled to "edhiafcbgj."

- This means that we know exactly how <code>random_shuffle()</code> will affect our input. This
enables us to strategically input a specific string that we know will be "randomly" shuffled
to a sorted string. I wrote a [Python script](mapper.py) to determine such a string. See the script
itself for a more detailed explanation, but basically, I examined where the characters of the
original input ended up as they were shuffled, then used that information to reverse engineer
a string that would be "shuffled" to a string in alphabetical order.

- Providing the string "ehgbaficdj" to the <code>nc</code> interface caused it to shuffle to
"abcdefghij." Since the shuffled string was in alphabetical order, the server gave me the flag.

## Flag

n00bz{5up3r_dup3r_ultr4_54f3_p455w0rd_807b258fa855}
