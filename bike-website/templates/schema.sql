
drop table if exists StationsStatic;
create table StationsStatic (
  station int primary key,
  name varchar(255),
  address varchar(255),
  lat decimal(8,6),
  lng decimal(8,6),
  banking boolean,
  bonus boolean,
  contract_name varchar(255),
  bike_stands int
);
drop table if exists StationsDynamic;
create table StationsDynamic (
  station int,
  status varchar(255),
  available_bike_stands int,
  available_bikes int,
  last_update int,
  index updated (last_update),
  index updated_station (last_update, station),
  index station_updated (station, last_update)
);
drop table if exists WeatherJSON;
create table WeatherJSON (
    dt int primary key,
    main text, 
    description text, 
    icon varchar(32), 
    temp decimal(4,1),
    json text character set utf8
);
