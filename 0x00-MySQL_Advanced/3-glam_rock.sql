-- cript that lists all bands with Glam rock as their main style, ranked by their longevity
DROP VIEW IF EXISTS `GramRockView`;

CREATE VIEW GramRockView AS
SELECT band_name,
    (CASE
        WHEN split IS NULL THEN 2022 - formed
        WHEN split > 2022 THEN 2022 - formed
        ELSE split - formed
    END) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;

SELECT * FROM GramRockView;