-- 1. Convert the database
ALTER DATABASE hbtn_0c_0 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- 2. Convert the table and all its character columns
ALTER TABLE hbtn_0c_0.first_table 
CONVERT TO CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- 3. Specifically convert the 'name' field
ALTER TABLE hbtn_0c_0.first_table 
MODIFY name VARCHAR(256) 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

