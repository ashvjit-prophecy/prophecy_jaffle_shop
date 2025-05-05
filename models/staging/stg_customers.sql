WITH source AS (

  {#-
  Normally we would select from the table here, but we are using seeds to load
  our data in this project
  #}
  SELECT * 
  
  FROM {{ ref('raw_customers')}}

),

renamed AS (

  SELECT 
    id AS customer_id,
    first_name,
    last_name,
    concat(first_name, last_name)
  
  FROM source

),

Reformat_1 AS (

  SELECT concat(first_name, last_name) AS some_column
  
  FROM source AS in0

)

SELECT *

FROM renamed
