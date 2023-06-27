CREATE TABLE consoles (
  console_id integer not null primary key,
  name text not null
)

INSERT INTO consoles (name) Values ("Steam");
INSERT INTO consoles (name) Values ("Playstation");
INSERT INTO consoles (name) Values ("Nintendo Switch");