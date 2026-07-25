---
name: sql-queries
description: Pull records with SQL. OmniSkill Legal crew — writes correct, safe queries for audits, discovery, and reporting, with the join and aggregation traps called out.
disable-model-invocation: true
---

# SQL Queries

> Pull records with SQL · OmniSkill Legal crew

Getting the right records out of a database — for an audit, a discovery request, a compliance report, or an operational question.

## 1. Understand the schema before writing

Never write a query against an assumed schema. Inspect first:

```sql
-- Postgres
\d table_name
SELECT column_name, data_type, is_nullable
FROM information_schema.columns WHERE table_name = 'orders';
```

Establish: primary and foreign keys, which columns are nullable, whether deletes are soft (`deleted_at`) or hard, and the timezone convention on timestamps. Each of these silently changes results.

## 2. The traps that produce wrong answers

**Soft deletes.** If the schema has `deleted_at`, every query needs `WHERE deleted_at IS NULL` unless deleted rows are wanted. Forgetting this inflates every count.

**Fan-out on joins.** Joining a one-to-many relationship multiplies rows. `SUM(orders.total)` after joining line items sums each order once per line item. Aggregate in a subquery or CTE first, then join.

**NULL semantics.** `NULL = NULL` is not true. `NOT IN (subquery)` returns *no rows* if the subquery yields a single NULL — use `NOT EXISTS`. Aggregates skip NULLs, so `AVG` over a column with NULLs divides by a smaller count than expected.

**`COUNT(*)` vs `COUNT(col)`.** The first counts rows; the second counts non-NULL values.

**Timezones.** `created_at` in UTC bucketed by local day shifts records across boundaries. Convert explicitly: `created_at AT TIME ZONE 'UTC' AT TIME ZONE 'America/New_York'`.

**Inclusive ranges.** `BETWEEN '2026-01-01' AND '2026-01-31'` on a timestamp excludes almost all of January 31. Use `>= start AND < next_day`.

**Implicit type coercion.** Comparing a string column to a number can silently cast and full-scan, or error, depending on engine.

## 3. Write it safely

**Read-only by default.** For audit and discovery work, connect with a read-only role. If a mutation is genuinely required, that is a separate, explicitly confirmed action.

**Never build SQL by string concatenation with untrusted input.** Use parameterised queries — this is injection prevention, not style.

**Test the shape before the full run.** Run with `LIMIT 10` first and check the columns and row shape are what was intended. Then remove the limit.

**Check the plan on anything large.** `EXPLAIN ANALYZE` before running a query over millions of rows on a production replica. A sequential scan on a large table can lock up a shared database.

Prefer a read replica for analytical work. Long analytical queries on a primary compete with the application.

## 4. Structure for review

Legal and audit output gets scrutinised, so the query must be readable:

```sql
WITH active_customers AS (
    SELECT id, email, created_at
    FROM customers
    WHERE deleted_at IS NULL
      AND created_at >= '2026-01-01'
),
order_totals AS (
    SELECT customer_id, SUM(total) AS lifetime_value, COUNT(*) AS order_count
    FROM orders
    WHERE status = 'completed' AND deleted_at IS NULL
    GROUP BY customer_id          -- aggregate BEFORE joining, to avoid fan-out
)
SELECT c.id, c.email, COALESCE(o.lifetime_value, 0) AS lifetime_value
FROM active_customers c
LEFT JOIN order_totals o ON o.customer_id = c.id
ORDER BY lifetime_value DESC;
```

CTEs over nested subqueries. Comment the non-obvious filter, not the obvious one.

## 5. Data minimisation

For a legal or compliance pull, select only the columns actually needed. Exporting a full table when three fields were requested creates a new personal-data problem while solving a records problem. Route handling questions to `/omniskill:compliance`.

## 6. Deliver

Verify the row count is plausible before sending. State the exact query, the database and environment, and the timestamp it ran — a result set without its query cannot be reproduced or checked.

Export tabular results via `/omniskill:xlsx`.

## Checks before delivering

- Schema inspected, not assumed.
- Soft deletes handled.
- No fan-out in aggregates.
- Date ranges half-open; timezone stated.
- Only necessary columns selected.
- Query, environment, and run time recorded alongside the results.
