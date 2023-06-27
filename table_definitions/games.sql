CREATE TABLE games (
  game_id integer not null primary key AUTOINCREMENT,
  name text not null,
  description text,
  publisher text,
  publish_date text,
  series text,
  series_number numeric
)