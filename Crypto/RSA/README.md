# RSA

## Description

The cryptography category is incomplete without RSA. So here is a simple RSA challenge. Have fun!

## Attachments

[encryption.txt](attachments/encryption.txt)

## Solution

- The attachment gives us the values of <code>e</code>, <code>n</code>, and <code>c</code>.
Since <code>e</code>'s value is very small, this is enough information to perform an RSA
decryption.

- I used [dcode.fr](https://www.dcode.fr/rsa-cipher) to decrypt the message. After entering the
given values for <code>e</code>, <code>n</code>, and <code>c</code>, I was able to get the flag.

## Flag

n00bz{crypt0_1s_1nc0mpl3t3_w1th0ut_rs4!!}
