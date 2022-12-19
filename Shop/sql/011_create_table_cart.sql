-- Active: 1663209307387@@db.ethereallab.app@3306@sp2943
CREATE TABLE
    IF NOT EXISTS IS601_Cart(
        id int AUTO_INCREMENT PRIMARY KEY,
        product_id int,
        user_id int,
        quantity int DEFAULT 0,
        unit_price int DEFAULT 99999,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
        check (quantity >= 0),
        -- don't allow negative stock; I don't allow backorders
        check (unit_price >= 0),
        -- don't allow negative costs
        FOREIGN KEY (user_id) REFERENCES IS601_Users(id),
        FOREIGN KEY(product_id) REFERENCES IS601_Products(id),
        UNIQUE KEY (product_id, user_id)
    )