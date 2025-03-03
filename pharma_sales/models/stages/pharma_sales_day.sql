with source_data as (

    SELECT 
        STRPTIME(datum, '%m/%d/%Y') transaction_date, -- example 1/2/2014
        M01AB,
        M01AE,
        N02BA,
        N02BE,
        N05B,
        N05C,
        R03,
        R06,
        Year,
        Month,
        Hour,
        Weekday_Name
    
    FROM {{ source('sales_source', 'sales_daily') }}
)

SELECT *

FROM source_data




