import sqlite3

conn = sqlite3.connect('lab3bd.db')
curs = conn.cursor()

curs.execute('''CREATE TABLE IF NOT EXISTS vocab
             (id INTEGER PRIMARY KEY,
             person BOOLEAN,
             anim BOOLEAN,
             object BOOLEAN,
             food BOOLEAN,
             abstract BOOLEAN,
             croatian TEXT COLLATE NOCASE,
             ukrainian TEXT)''')

curs.execute('''INSERT INTO vocab VALUES
           (1, FALSE, FALSE, FALSE, FALSE, TRUE, 'Ime', "ім'я"),
           (2, FALSE, FALSE, FALSE, FALSE, TRUE, 'Oblak', 'хмара'),
           (3, FALSE, FALSE, FALSE, FALSE, TRUE, 'Planina', 'гора'),
           (4, FALSE, FALSE, FALSE, TRUE, FALSE, 'More', 'море'),
           (5, FALSE, FALSE, TRUE, FALSE, FALSE, 'Stol', 'стіл'),
           (6, TRUE, FALSE, FALSE, FALSE, FALSE, 'Matematika', 'математика'),
           (7, FALSE, FALSE, TRUE, FALSE, FALSE, 'Automobil', 'автомобіль'),
           (8, FALSE, TRUE, FALSE, FALSE, FALSE, 'Ptica', 'птах'),
           (9, FALSE, FALSE, FALSE, TRUE, FALSE, 'Jabuka', 'яблуко'),
           (10, FALSE, FALSE, FALSE, FALSE, TRUE, 'Ljubav', 'любов'),
           (11, FALSE, FALSE, FALSE, FALSE, TRUE, 'Bol', 'біль'),
           (12, FALSE, TRUE, FALSE, FALSE, FALSE, 'Eksperiment', 'експеримент'),
           (13, FALSE, FALSE, TRUE, FALSE, FALSE, 'Vatra', 'вогонь'),
           (14, TRUE, FALSE, FALSE, FALSE, FALSE, 'Sestra', 'сестра'),
           (15, FALSE, FALSE, TRUE, FALSE, FALSE, 'Dokument', 'документ'),
           (16, FALSE, FALSE, TRUE, FALSE, FALSE, 'Mozak', 'мозок'),
           (17, FALSE, FALSE, TRUE, FALSE, FALSE, 'Ulaznica', 'квиток'),
           (18, FALSE, FALSE, FALSE, FALSE, TRUE, 'Danas', 'сьогодні'),
           (19, FALSE, FALSE, FALSE, TRUE, FALSE, 'Čaj', 'чай'),
           (20, FALSE, TRUE, FALSE, FALSE, FALSE, 'Gavran', 'ворон'),
           (21, FALSE, FALSE, FALSE, FALSE, TRUE, 'Trenutak', 'мить'),
           (22, FALSE, FALSE, FALSE, TRUE, FALSE, 'Kruh', 'хліб'),
           (23, FALSE, FALSE, TRUE, FALSE, FALSE, 'Muškarac', 'чоловік'),
           (24, FALSE, FALSE, FALSE, FALSE, TRUE, 'Snijeg', 'сніг'),
           (25, FALSE, FALSE, FALSE, FALSE, TRUE, 'Smijeh', 'сміх'),
           (26, FALSE, FALSE, FALSE, FALSE, TRUE, 'Osmijeh', 'усмішка'),
           (27, FALSE, FALSE, FALSE, FALSE, TRUE, 'Tjedan', 'тиждень'),
           (28, FALSE, FALSE, TRUE, FALSE, FALSE, 'Zračna luka', 'аеропорт'),
           (29, FALSE, FALSE, TRUE, FALSE, FALSE, 'Činija', 'миска'),
           (30, TRUE, FALSE, FALSE, FALSE, FALSE, 'Žena', 'жінка'),
           (31, FALSE, FALSE, FALSE, TRUE, FALSE, 'Doručak', 'сніданок'),
           (32, FALSE, FALSE, FALSE, TRUE, FALSE, 'Kava', 'кава'),
           (33, FALSE, TRUE, FALSE, FALSE, FALSE, 'Mačka', 'кіт'),
           (34, FALSE, TRUE, FALSE, FALSE, FALSE, 'Pas', 'собака'),
           (35, FALSE, FALSE, TRUE, FALSE, FALSE, 'Most', 'міст'),
           (36, FALSE, FALSE, FALSE, FALSE, TRUE, 'Sreća', 'щастя'),
           (37, FALSE, TRUE, FALSE, FALSE, FALSE, 'Taran', 'тарган'),
           (38, FALSE, FALSE, TRUE, FALSE, FALSE, 'Autobus', 'автобус'),
           (39, FALSE, FALSE, TRUE, FALSE, FALSE, 'Cvijet', 'квітка'),
           (40, FALSE, FALSE, FALSE, FALSE, TRUE, 'Sat', 'година'),
           (41, FALSE, FALSE, FALSE, FALSE, TRUE, 'Sekunda', 'секунда'),
           (42, FALSE, FALSE, FALSE, TRUE, FALSE, 'Vino', 'вино'),
           (43, FALSE, FALSE, TRUE, FALSE, FALSE, 'Cigara', 'цигара'),
           (44, FALSE, TRUE, FALSE, FALSE, FALSE, 'Medvjed', 'ведмідь'),
           (45, FALSE, FALSE, FALSE, TRUE, FALSE, 'Voda', 'вода'),
           (46, FALSE, FALSE, FALSE, TRUE, FALSE, 'Mlijeko', 'молоко'),
           (47, FALSE, FALSE, TRUE, FALSE, FALSE, 'Kalendar', 'календар'),
           (48, TRUE, FALSE, FALSE, FALSE, FALSE, 'Učitelj', 'вчитель'),
           (49, FALSE, FALSE, FALSE, TRUE, FALSE, 'Med', 'мед'),
           (50, FALSE, FALSE, FALSE, TRUE, FALSE, 'Meso', "м'ясо")''')

conn.commit()
    root.mainloop()
