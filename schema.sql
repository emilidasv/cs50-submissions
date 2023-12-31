CREATE TABLE "ingridients" (
    "ingridient_id" INTEGER,
    "name" TEXT,
    "prize_per_unit" NUMERIC,
    "unit" TEXT NOT NULL,
    PRIMARY KEY("ingridient_id")
);


CREATE TABLE "customer" (
    "customer_id" INTEGER,
    "first_name" TEXT,
    "last_name" TEXT,
    PRIMARY KEY("customer_id")
);


CREATE TABLE "orders" (
    order_id INTEGER,
    donut_id INTEGER,
    amount INTEGER,
    customer_id INTEGER,
    PRIMARY KEY("order_id")
    FOREIGN KEY("customer_id") REFERENCES "customers"("customer_id"),
    FOREIGN KEY("donut_id") REFERENCES "donuts"("donut_id")
);

CREATE TABLE "donuts" (
    donut_id INTEGER,
    donuts_name TEXT
    price NUMERIC,
    is_gluten_free BOOLEAN,
    PRIMARY KEY("donut_id")
);

CREATE TABLE "receipe" (
    receipe_id INTEGER,
    donut_id INTEGER,
    ingridient_id INTEGER,
    PRIMARY KEY("donut_id","ingridient_id"),
    FOREIGN KEY("donut_id") REFERENCES "donuts"("donut_id"),
    FOREIGN KEY("ingridient_id") REFERENCES "ingridients"("ingridient_id")

);

CREATE TABLE "history" (
    history_id INTEGER,
    order_id INTEGER,
    PRIMARY KEY("history_id"),
    FOREIGN KEY("order_id") REFERENCES "orders"("order_id")
);


