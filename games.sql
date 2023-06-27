CREATE TABLE games (
  key integer not null primary key AUTOINCREMENT,
  name text not null,
  description text,
  rating numeric,
  played_status text check(played_status in ('Not started', 'Started', 'Gave up', 'Finished'))
)