CREATE TABLE platforms (
  console_id integer not null primary key,
  name text not null,
  owned boolean default false
);