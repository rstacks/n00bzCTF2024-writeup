# Vacation

## Description

My friend told me they were going on vacation, but they sent me this weird
PowerShell script instead of a postcard!

## Attachments

[run.ps1](attachments/run.ps1)

[output.txt](attachments/output.txt)

## Solution

- Looking at the provided PowerShell script, it seems that it reads the text in a file
called <code>flag.txt</code>, performs a XOR operation with a key of 3 on each character of
the flag, then places the result in <code>output.txt</code>.

- I took the text in <code>output.txt</code> to [CyberChef](https://gchq.github.io/CyberChef/) and
added XOR to the recipe with a key of 3. This yielded the flag.

## Flag

n00bz{from_paris_wth_xor}
