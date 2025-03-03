with source_data as (

    SELECT 
        *
    
    FROM {{ source('sales_source', 'sales_weekly') }}
)

SELECT *

FROM source_data
