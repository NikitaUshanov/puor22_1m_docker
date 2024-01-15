CREATE TABLE public.prices (
    id integer UNIQUE,
    property_type varchar(20),
    price decimal,
    location varchar(200),
    city varchar(50),
    baths integer,
    purpose varchar(20),
    bedrooms integer,
    Area_in_Marla decimal
);

\copy prices FROM '~/docker-entrypoint-initdb.d/csv/house_prices.csv' DELIMITER ',' CSV HEADER;