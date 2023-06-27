CREATE TABLE consoles (
  key integer not null primary key AUTOINCREMENT,
  name text not null
)

INSERT INTO consoles (name) Values ("Steam");
INSERT INTO consoles (name) Values ("Playstation");
INSERT INTO consoles (name) Values ("Nintendo Switch");