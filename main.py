DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS student_group; 
DROP TABLE IF EXISTS kafedra;


CREATE TABLE kafedra
(
    kafedra_id int PRIMARY KEY,
    name_ text NOT NULL,
    dekanat text NOT NULL
);


INSERT INTO kafedra VALUES (111, 'Programming' , 'IT');
INSERT INTO kafedra VALUES (222, 'Fizika' , 'Science');

CREATE TABLE student_group 
(
    s_grop_id int PRIMARY KEY,
    name_ text NOT NULL,
    kafedra_id int REFERENCES kafedra(kafedra_id)  NOT NULL
);

INSERT INTO student_group VALUES (11 , 'BIBA2201' , 111);
INSERT INTO student_group VALUES (22 , 'BIBA2202' , 111);
INSERT INTO student_group VALUES (33 , 'BOBA2201' , 222);
INSERT INTO student_group VALUES (44 , 'BOBA2202' , 222);

CREATE TABLE student 
(
    student_id int PRIMARY KEY,
    fl_name text NOT NULL,
    seria_pasporta text NOT NULL,
    group_id int REFERENCES student_group(s_grop_id) NOT NULL
);

INSERT INTO student VALUES (1 , 'Vovan Opasnyy' , '43927654108' , 11);
INSERT INTO student VALUES (2 , 'Lubava Mirnaya' , '45372840572' , 11);
INSERT INTO student VALUES (3 , 'Patric Bikinbotom' , '56932650157' , 11);
INSERT INTO student VALUES (4 , 'Julia Nogty' , '45628991062' , 11);
INSERT INTO student VALUES (5 , 'Pavel Vlazhnayasalfetka' , 52628474032 , 11);

INSERT INTO student VALUES (6 , 'Fufel Krikbara' , '76903982012' , 22);
INSERT INTO student VALUES (7 , 'Andrey Losangeles' , '20457540280' , 22);
INSERT INTO student VALUES (8 , 'Aleksey Blatnoy' , '77777777777' , 22);
INSERT INTO student VALUES (9 , 'Edik Kopchik' , '39764934743' , 22);
INSERT INTO student VALUES (10 , 'Zhanna Poyasnica' , '30398473241' , 22);


INSERT INTO student VALUES (11 , 'Viktoria Nalevayka' , '30398473241' , 33);
INSERT INTO student VALUES (12 , 'Grigoriy Otlevayka' , '30398473241' , 33);
INSERT INTO student VALUES (13 , 'Julia Vernigora' , '30398473241' , 33);
INSERT INTO student VALUES (14 , 'Komila Somelye' , '30398473241' , 33);
INSERT INTO student VALUES (15 , 'Nurik Armani' , '30398473241' , 33);


INSERT INTO student VALUES (16 , 'Vika Paricmaherskaya' , '43638292362' , 44);
INSERT INTO student VALUES (17 , 'Dmitriy Chicagobulls' , '32674527211' , 44);
INSERT INTO student VALUES (18 , 'Kirill Smisharik' , '56384921753' , 44);
INSERT INTO student VALUES (19 , 'Snoop Dog' , '82845960943' , 44);
INSERT INTO student VALUES (20 , 'Truwer MuzTV' , '37437255430' , 44);
