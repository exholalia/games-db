CREATE TABLE entries (
  entry_id integer not null primary key AUTOINCREMENT,
  FOREIGN KEY (game_id) REFERENCES games(game_id),
  FOREIGN KEY (console_is) REFERENCES games(console_id),
  price real,
  rating numeric,
  hours_played real
)