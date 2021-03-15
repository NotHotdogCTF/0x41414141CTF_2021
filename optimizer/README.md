For this challenge we were given a ip and a port to netcat into

We are greeted with the message that we will be given a number of problems and we will need to give the minimum number of moves to solve

Level 1 is tower of hanoi. Unfortunately, the formatting is kind of wonky for this, but after some trial and error we can find that each number in the given list represents a disk

Fortunately, we do not need to know the position of the disks to solve this problem. The game tower of hanoi is a solved game and we know that the minimum number of moves is equal to (2**[num of disks])-1

After 25 stages of this we get to level 2

Level 2 is merge sort (kind of) we have to give the number of inversions in each array

We can do this iteratively relatively quickly by counting the number of smaller elements occuring after each element in the array

After 25 more stages of this we get our flag

Obviously, it would be insane to do all of this by hand so I created a program optimize.py to do this for me

flag{g077a_0pt1m1ze_3m_@ll}
