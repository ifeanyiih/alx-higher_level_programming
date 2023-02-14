-- Import in hbtn_0c_0 database this table dum

SELECT DISTINCT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
