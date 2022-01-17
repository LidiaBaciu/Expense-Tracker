DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS address;
DROP TABLE IF EXISTS user_address;
DROP TABLE IF EXISTS income_type;
DROP TABLE IF EXISTS income;
DROP TABLE IF EXISTS spending_type;
DROP TABLE IF EXISTS spending_category;
DROP TABLE IF EXISTS spending;
DROP TABLE IF EXISTS saving_type;
DROP TABLE IF EXISTS saving;

CREATE TABLE user (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    birthday TEXT
);

CREATE TABLE address (
    address_id INTEGER PRIMARY KEY AUTOINCREMENT,
    street TEXT,
    street_no NUMBER(7),
    city TEXT NOT NULL,
    country TEXT NOT NULL
);

CREATE TABLE user_address (
    user_id INTEGER,
    address_id INTEGER,
    FOREIGN KEY (user_id) references user(user_id),
    FOREIGN KEY (address_id) references address(address_id)
);

CREATE TABLE income_type (
    income_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    income_type TEXT NOT NULL
);

CREATE TABLE income (
    income_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL, 
    income_type_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    amount REAL NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (income_type_id) REFERENCES income_type(income_type_id)
);

CREATE TABLE spending_type (
    spending_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    spending_type TEXT NOT NULL,
    goal REAL NOT NULL
);

CREATE TABLE spending_category (
    spending_category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE spending (
    spending_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL, 
    spending_type_id INTEGER NOT NULL,
    spending_category_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    amount REAL NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (spending_type_id) REFERENCES spending_type(spending_type_id),
    FOREIGN KEY (spending_category_id) REFERENCES spending_category(spending_category_id)
);

CREATE TABLE saving_type (
    saving_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    saving_type TEXT NOT NULL,
    goal REAL NOT NULL
);

CREATE TABLE saving (
    saving_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL, 
    saving_type_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    amount REAL NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (saving_type_id) REFERENCES saving_type(saving_type_id)
);