/* hash of oops! is 982c0381c279d139fd221fce974916e7
*/
/*SELECT password password from users where username = 'admin';
e10adc3949ba59abbe56e057f20f883e
select count(*) from user_logs;
51
*/
UPDATE users SET password='982c0381c279d139fd221fce974916e7' WHERE username = 'admin';
/*select count(*) from user_logs;
52*/
delete from user_logs WHERE new_password ='982c0381c279d139fd221fce974916e7';

/*UPDATE users SET password=(SELECT password FROM users WHERE username='emily33')
WHERE username = 'admin';
*/
/*UPDATE user_logs SET old_username='emily33' WHERE id=52;
UPDATE user_logs SET new_username='emily33' WHERE id=52;
*/
/*UPDATE user_logs SET old_password='e10adc3949ba59abbe56e057f20f883e' WHERE id=52;*/
INSERT INTO user_logs ("type", "old_username", "new_username", "old_password", "new_password")
VALUES ('update','emily33', 'emily33','e10adc3949ba59abbe56e057f20f883e', (SELECT password FROM users WHERE username='emily33'));

