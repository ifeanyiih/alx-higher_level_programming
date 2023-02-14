-- Import in hbtn_0c_0 database this table dum
USE hbtn_0c_0;
SOURCE temperatures.sql;

SELECT DISTINCT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
