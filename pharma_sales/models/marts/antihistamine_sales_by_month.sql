with source_data as (

    SELECT 
        Month,
        SUM(R06) as antihitamine_sales

    FROM {{ ref('pharma_sales_day') }}

    GROUP BY month

    ORDER BY month
)

SELECT *

FROM source_data