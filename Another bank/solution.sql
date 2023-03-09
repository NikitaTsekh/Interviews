--Задача выполнялась в PostgreSQL
--Для выполнения задачи, исходные данные были экспортированы в SQL базу. Названия столбцов переименованы на английский. Базу прилагаю (Loco.sql файл)
--Чтобы работал Pivot_table, сначала делал:
--create extension tablefunc;
--Сам запрос:

select to_char(a.date, 'DD.MM.YYYY' ) AS period 
,a.sum,a.count,
b."0",b."1",b."2",b."3",b."4",b."5",b."6",b."7",
b."8",b."9",b."10",b."11",b."12",b."13",b."14",b."15",b."16",b."17",b."18",b."19",b."20"
from (SELECT date_of_contract_signature        as date,
             sum(cash_out_sum)                 as sum,
             count(date_of_contract_signature) as count
      FROM (SELECT DISTINCT ON (contract_id) date_of_contract_signature, cash_out_sum FROM loco_final) x
      GROUP BY date_of_contract_signature
      ORDER BY date_of_contract_signature) a
              LEFT OUTER JOIN (select *
                     from crosstab($$
SELECT date_of_contract_signature, date_of_report, sum(debt_90_plus) as sum from loco_final
GROUP BY 1, 2
order by 1, 2
$$, $$
select date_of_report from loco_final
group by date_of_report
order by date_of_report
$$) as ct(date timestamp, "0" float8, "1" float8, "2" float8, "3" float8, "4" float8, "5" float8,
                                 "6" float8, "7" float8, "8" float8, "9" float8, "10" float8, "11" float8, "12" float8,
                                 "13" float8, "14" float8, "15" float8, "16" float8, "17" float8, "18" float8, "19" float8,
                                 "20" float8)) b on a.date = b.date
order by a.date;
