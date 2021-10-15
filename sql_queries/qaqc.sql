create table example as (

	select geocode::text from raw.census2020mcd_p1 c2020mcd_p1
)