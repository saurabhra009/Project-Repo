-- Active: 1663209307387@@db.ethereallab.app@3306@sp2943
ALTER TABLE IS601_Orders
ADD COLUMN first_name varchar(30) not null AFTER user_id;
ALTER TABLE IS601_Orders
ADD COLUMN last_name varchar(30) not null AFTER first_name;
ALTER TABLE IS601_Orders
ADD COLUMN number_of_items int(30) not null AFTER money_received;