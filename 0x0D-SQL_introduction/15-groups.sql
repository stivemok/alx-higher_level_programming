-- lists the number of records with the same score in second_table of database hbtn_0c_0 in MySQL server.
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score ORDER BY number DESC;
