select A.owner_id, O.owner_name, count(*) as article_count
from owner O, article A
where O.owner_id = A.owner_id
group by O.owner_id