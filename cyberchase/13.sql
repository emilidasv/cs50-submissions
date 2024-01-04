/* Choose your own question*
which season has most eposides*/
SELECT max(episode_in_season) FROM episodes WHERE season > 2 AND season < 5;
