SELECT customer, SUM(amount_cents) AS paid_cents, COUNT(*) AS paid_orders
FROM orders
WHERE status = 'paid'
GROUP BY customer
ORDER BY paid_cents DESC, customer ASC;
