UPDATE platforms
SET owned = 1
WHERE console_id = 6 
    OR console_id = 14
    OR console_id = 39
    OR console_id = 130
    OR console_id = 162
    OR console_id = 163
    OR console_id = 167
    OR console_id = 384
    OR console_id = 385;

CREATE VIEW my_platforms AS
    SELECT * FROM platforms
    WHERE owned = 1;