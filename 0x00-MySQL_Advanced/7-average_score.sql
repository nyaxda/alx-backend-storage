--  script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE total_score FLOAT DEFAULT 0;
    DECLARE total_projects INT DEFAULT 0;
    DECLARE average_score FLOAT DEFAULT 0;

    SELECT IFNULL(SUM(score), 0) INTO total_score
        FROM corrections
        WHERE corrections.user_id = user_id;

    SELECT IFNULL(COUNT(*), 0) INTO total_projects
        FROM corrections
        WHERE corrections.user_id = user_id;

    SET average_score = IF(total_projects = 0, 0, total_score / total_projects);
    
    UPDATE users
        SET users.average_score = average_score
        WHERE users.id = user_id;
END //

DELIMITER ;
