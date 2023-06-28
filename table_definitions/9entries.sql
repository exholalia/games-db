CREATE TABLE entries (
  entry_id integer not null primary key AUTOINCREMENT,
  game_id integer not null,
  console_id integer not null,
  price real,
  rating numeric,
  hours_played real,
  FOREIGN KEY (game_id) REFERENCES games(game_id),
  FOREIGN KEY (console_id) REFERENCES platforms(console_id)
);