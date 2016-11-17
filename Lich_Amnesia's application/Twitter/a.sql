SELECT     Id,    (CASE        WHEN            t1.son IS NOT NULL                AND t1.P_id IS NOT NULL        THEN            'inner'        WHEN t1.son IS NULL THEN 'leaf'        ELSE 'root'    END) AS typeFROM    (SELECT         t1.Id AS Id, t1.P_id AS P_id, t2.Id AS son    FROM        tree AS t1    LEFT JOIN tree AS t2 ON t1.Id = t2.P_id) AS t1GROUP BY IdORDER BY Id