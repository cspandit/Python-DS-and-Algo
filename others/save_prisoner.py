"""A jail has a number of prisoners and a number of treats to pass out to them.
Their jailer decides the fairest way to divide the treats is to seat the prisoners around a circular table
in sequentially numbered chairs. A chair number will be drawn from a hat. Beginning with the prisoner in that chair,
one candy will be handed to each prisoner sequentially around the table until all have been distributed.

The jailer is playing a little joke, though. The last piece of candy looks like all the others,
but it tastes awful. Determine the chair number occupied by the prisoner who will receive that candy.

For example, there are 7(n) prisoners and 19(m) pieces of candy. The prisoners arrange themselves in seats
numbered 1 to 7. Let’s suppose 2(s) is drawn from the hat. Prisoners receive candy at positions
2, 3, 4, 5, 6, 7, 1, 2, ...
The prisoner to be warned sits in chair number 6.
Calculation :
reminder = n%m = 19%7 = 5. If distribution was started at 1, then after distributing 2 among all 7 prisoner 5 more will
be left.  Now say prisoner start distributing from 2 => 2,3,4,5,6[Answer] => (r+s-1) => 5+2-1=6

There can be situation when s is say 7 then 5+7-1 = 11(is not valid seat number), so formula becomes (r+s-1)%n
When remainder is zero position is n
"""
def prison_game(n,m,s):
    r = m%n
    return (r+s-1)%n if (r+s-1)%n != 0 else n

print(prison_game(7,19,2))