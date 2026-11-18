CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer TEXT NOT NULL,
    amount_cents INTEGER NOT NULL,
    status TEXT NOT NULL
);
