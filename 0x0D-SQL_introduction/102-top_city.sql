-- Displays the top 3 cities temperature during July and August order by temperature
SELECT TOP 3 city, AVG(value) AS avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC;
