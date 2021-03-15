For this challenge we are given a c and n value and a file factorize.py

From this file we can see that this is a form of RSA encryption and can see the e value in plaintext

Thus, we can check if the encryption is easy to break by running it through RsaCtfTool

So python3 RsaCtfTool.py -n [n] -e [e] --uncipher [c]

This gives our flag


Later in the competition I learned that this was an unintended solution, so in the interest of the spirit of the ctf I opted to do it through the correct method: writing a factorization method

Thus, I wrote fermat.py
This uses fermat's factoring algorithm to get p and q from n

Next it calculates PHI and d

Finally it decrypts the message to hex

Either way:

flag{just_g0tta_f@ct0rize_1t4536}
