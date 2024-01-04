/*
For any two users, the app needs to quickly show a list of the friends they have in common.
Given two usernames, lovelytrust487 and exceptionalinspiration482, find the user IDs of their
mutual friends. A mutual friend is a user that both lovelytrust487 and exceptionalinspiration482
count among their friends.

Ensure your query uses the index automatically created on primary key columns of the friends table.
 This index is called sqlite_autoindex_friends_1.

Need a hint?
Recall that, in SQL, you can use certain keywords to find the intersection of two groups. See Week 1’s notes for a refresher.

*/

EXPLAIN QUERY PLAN
SELECT "frusername"  as "username" FROM (
SELECT frID , users.username as "frusername" from (
SELECT friends.friend_id as "frID" from users
JOIN friends ON(friends.user_id = users.id)
WHERE users.id=(SELECT id FROM users WHERE username="lovelytrust487")

INTERSECT

SELECT friends.friend_id from users
JOIN friends ON(friends.user_id = users.id)
WHERE users.id=(SELECT id FROM users WHERE username="exceptionalinspiration482"))
JOIN users ON (users.id=frID)
);
