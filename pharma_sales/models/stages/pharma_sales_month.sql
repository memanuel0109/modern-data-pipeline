with source_data as (

    SELECT 
        *
    
    FROM {{ source('sales_source', 'sales_monthly') }}
)

SELECT *

FROM source_data
