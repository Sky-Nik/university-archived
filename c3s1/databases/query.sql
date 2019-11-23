# "На яких факультетах всі заняття проводять тільки викладачі з КНУ?
SELECT DISTINCT G.FACULTET

FROM G

WHERE NOT EXISTS (
  SELECT *  # групи з того ж факультету що і G (4:6) у яких є пари з викладачами не з КНУ

  FROM G GY

  WHERE GY.FACULTET = G.FACULTET
    AND GY.KG NOT IN (
      SELECT KG  # ключі груп у яких немає пар з викладачами не з КНУ

      FROM G

      WHERE NOT EXISTS (
        SELECT *  # пари групи із ключем G.KG (13:14) які ведуть викладачі не з КНУ

        FROM R

        WHERE G.KG = R.KG
          AND R.KL NOT IN (
            SELECT KL  # ключі лекторів з КНУ

            FROM L

            WHERE ORG = "КНУ"
          )
      )
    )
) 
  AND G.KG IN (
    SELECT KG  # ключі груп у яких є хоча б якісь заняття
    
    FROM R
  )
;