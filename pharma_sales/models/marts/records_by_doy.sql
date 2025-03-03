with source_data as (

    SELECT 
        weekday_name,
        COUNT(*) as record_count

    FROM {{ ref('pharma_sales_day') }}

    GROUP BY weekday_name
)

SELECT *

FROM source_data