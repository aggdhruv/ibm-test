select A.owner_id, O.owner_name, count(CAM.category_id) as category_count
from owner O, article A, category_article_mapping CAM       
where O.owner_id = A.owner_id and A.article_id = CAM.article_id
group by O.owner_id