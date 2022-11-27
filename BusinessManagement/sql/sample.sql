
SELECT IF(name is not null, name,'N/A') as company_name FROM IS601_MP2_Employees e LEFT JOIN IS601_MP2_Companies c ON e.company_id = c.id ORDER BY company_name desc LIMIT 10


