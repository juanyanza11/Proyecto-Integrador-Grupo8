drop table USUARIO;
drop table TWEET;
drop table URL_TWEET;
drop table MEDIA_TWEET;
drop table MENCIONES;
drop table HASHTAG;
drop table AUXILIAR;


CREATE TABLE USUARIO (
        id_user NUMBER,
         from_user      		 VARCHAR2(50),
         user_lang     			 VARCHAR2(10),
         from_user_id_str   	 NUMBER,
         profile_image_url       VARCHAR2(500),
         user_followers_count    NUMBER,
         user_friends_count  	 NUMBER,
         user_location 			 VARCHAR2(200),
        constraint pk_id_user PRIMARY KEY (id_user)
);

CREATE TABLE TWEET (
         id_str      		 NUMBER PRIMARY KEY,
         text     			 VARCHAR2(700),
         created_at   	 VARCHAR2(600),
         time       VARCHAR2(100),
         geo_coordinates    varchar2(100),
         in_reply_to_user_id_str  	 NUMBER,
         in_reply_to_screen_name 	 VARCHAR2(50),
         in_reply_to_status_id_str   NUMBER,
         status_url  			 VARCHAR2(400),
         from_user_id_str NUMBER,
         constraint fk_from_user_id_str FOREIGN KEY(from_user_id_str)
                   REFERENCES USUARIOS(FROM_USER_ID_STR)
);

CREATE TABLE MEDIA_TWEET (
         media_url      		 NUMBER,
         id_str1     			 NUMBER,
         display_url   	 VARCHAR2(600),
         tipo          VARCHAR2(80),
         expanded_url VARCHAR2(500),
         constraint fk_id_str1 FOREIGN KEY(id_str1)
                   REFERENCES TWEET(id_str)
);

CREATE TABLE HASHTAG (
         text_h      		 VARCHAR2(700),
         id_str2     			 NUMBER,
         constraint fk_id_str2 FOREIGN KEY(id_str2)
                   REFERENCES TWEET(id_str)
);

CREATE TABLE MENCIONES
(
    id_mentions NUMBER,
    id_str3     NUMBER,
    screen_name VARCHAR2(600),
    name        VARCHAR2(80),
    constraint fk_id_str3 FOREIGN KEY (id_str3)
        REFERENCES TWEET(id_str),
    constraint pk_id_men PRIMARY KEY (id_mentions)

);

CREATE TABLE URL_TWEET (
         url_id      		 NUMBER,
         id_str4     	        NUMBER,
         status_url   	 VARCHAR2(600),
         source          VARCHAR2(80),
         profile_image_url VARCHAR2(500),
         constraint fk_id_str4 FOREIGN KEY(id_str4)
                   REFERENCES TWEET(id_str),
         constraint pk_url_id PRIMARY KEY (url_id)
);

//* Inserción de datos en la tabla USUARIO*//

insert into USUARIO (id_user, from_user, user_lang, from_user_id_str, profile_image_url,
                     user_followers_count,user_friends_count, user_location)
select distinct ROWNUM,from_user, user_lang, from_user_id_str, profile_image_url,
                user_followers_count,user_friends_count, user_location
from AUXILIAR;
commit;

//* Inserción de datos en la tabla USUARIO*//

insert into TWEET (id_str, text, created_at, time, geo_coordinates, in_reply_to_user_id_str, in_reply_to_screen_name, in_reply_to_status_id_str, status_url, from_user_id_str)
select distinct a.id_str, a.TEXTONEW, a.CREATED_AT, a.TIME, a.GEO_COORDINATES, a.IN_REPLY_TO_USER_ID_STR, a.IN_REPLY_TO_SCREEN_NAME, a.IN_REPLY_TO_STATUS_ID_STR,a.STATUS_URL,a.FROM_USER_ID_STR
from AUXILIAR a;
commit;

//*
SELECT from_user, COUNT(*) AS RecuentoFilas
FROM AUXILIAR
GROUP BY from_user
HAVING COUNT(*) > 1
ORDER BY FROM_USER DESC;

SELECT FROM_USER_ID_STR, COUNT(*) AS RecuentoFilas
FROM AUXILIAR
GROUP BY FROM_USER_ID_STR
HAVING COUNT(*) > 1
ORDER BY FROM_USER_ID_STR;
*//

select FROM_user, user_lang FROM USUARIO
where user_lang = 'pl';