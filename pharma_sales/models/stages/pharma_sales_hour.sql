with source_data as (

    SELECT 
        *
    
    FROM {{ source('sales_source', 'sales_hourly') }}
)

SELECT *

FROM source_data
