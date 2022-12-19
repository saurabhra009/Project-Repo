CREATE TABLE
    IF NOT EXISTS IS601_Orders(
        id int AUTO_INCREMENT PRIMARY KEY,
        user_id int,        
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
        total_price int,
        address varchar(255),
        payment_method varchar(255),
        money_received float,
        number_of_items int,
        FOREIGN KEY (user_id) REFERENCES IS601_Users(id)
    )