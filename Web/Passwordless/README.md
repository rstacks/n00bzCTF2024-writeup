# Passwordless

## Description

Tired of storing passwords? No worries! This super secure website is passwordless!

http://24.199.110.35:40150

## Attachments

[app.py](attachments/app.py)

## Solution

- I started by examining the provided <code>app.py</code> to see how the website worked. It seems
that after the user provides a username, they are given a <code>uid</code> value and redirected
to a webpage that corresponds with that <code>uid</code>. If the <code>uid</code> matches that of
the admin, then the flag is revealed on that webpage.

- The admin's username is "admin123" according to the source code, but the website will stop us
if we attempt to provide this username. So, I decided to try accessing the admin's <code>uid</code>
page directly. To do this, we need to figure out the admin's <code>uid</code>, and <code>app.py</code>
gives us everything we need for this.

- I wrote a very short [Python script](get_uid.py) of my own to determine the admin's
<code>uid</code>. The website generates a <code>uid</code> like this:

```
uid = uuid.uuid5(leet,username)
```

- In my script, I provided "admin123" as the <code>username</code> and copied the value of
<code>leet</code> from the source code. This revealed the admin's <code>uid</code>:
3c68e6cc-15a7-59d4-823c-e7563bbb326c.

- I navigated to http://24.199.110.35:40150/3c68e6cc-15a7-59d4-823c-e7563bbb326c, and the flag
was revealed.

## Flag

n00bz{1337-13371337-1337-133713371337-1337}
