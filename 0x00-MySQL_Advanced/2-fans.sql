-- script that ranks country origins of bands, ordered by the number of (non-unique) fans
DROP VIEW IF EXISTS `CountryRank`;

CREATE VIEW CountryRank AS
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

SELECT * FROM CountryRank;