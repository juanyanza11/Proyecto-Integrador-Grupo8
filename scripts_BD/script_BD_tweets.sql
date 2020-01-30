drop table TWEET cascade constraints ;
drop table HASHTAG cascade constraints;

CREATE TABLE USUARIOS(
         from_user      		 VARCHAR2(50),
         user_lang     			 VARCHAR2(10),
         from_user_id_str   	 NUMBER,
         profile_image_url       VARCHAR2(500),
         user_followers_count    NUMBER,
         user_friends_count  	 NUMBER,
         user_location 			 VARCHAR2(200),
        constraint pk_from_user_id_str PRIMARY KEY (from_user_id_str)
);

CREATE TABLE TWEET (
         id_str               NUMBER PRIMARY KEY,
         text                  VARCHAR2(700),
         created_at        VARCHAR2(600),
         time       VARCHAR2(100),
         geo_coordinates    varchar2(100),
         in_reply_to_user_id_str       NUMBER,
         in_reply_to_screen_name      VARCHAR2(50),
         in_reply_to_status_id_str   NUMBER,
         status_url               VARCHAR2(400),
         from_user_id_str NUMBER,
         constraint fk_from_user_id_str FOREIGN KEY(from_user_id_str)
                   REFERENCES USUARIOS(FROM_USER_ID_STR)
);

CREATE TABLE HASHTAG (
         text_h               VARCHAR2(700),
         id_strH                  NUMBER,
         constraint id_strH FOREIGN KEY(id_strH)
         REFERENCES TWEET(id_str)
);

CREATE TABLE MENCIONES
(
    id_mentions NUMBER,
    id_strMen   NUMBER,
    screen_name VARCHAR2(600),
    name        VARCHAR2(80),
         constraint fk_id_strMen FOREIGN KEY(id_strMen)
         REFERENCES TWEET(id_str)
);

CREATE TABLE URL_TWEET (
         id_strU                 NUMBER,
         status_url        VARCHAR2(600),
         source          VARCHAR2(80),
         profile_image_url VARCHAR2(500),
         constraint fk_id_strU FOREIGN KEY(id_strU)
         REFERENCES TWEET(id_str)
);

CREATE TABLE MEDIA_TWEET (
         media_url               VARCHAR2(600),
         id_strM                  NUMBER,
         display_url        VARCHAR2(600),
         tipo          VARCHAR2(80),
         expanded_url VARCHAR2(800),
         constraint fk_id_strM FOREIGN KEY(id_strM)
         REFERENCES TWEET(id_str)
);

//------------------------------------INSERTS--------------------------
insert into USUARIOS (from_user, user_lang, from_user_id_str, profile_image_url, user_followers_count, user_friends_count, user_location)
select distinct from_user, user_lang, from_user_id_str,PROFILE_IMAGE_URL, USER_FOLLOWERS_COUNT, USER_FRIENDS_COUNT, USER_LOCATION
from AUXILIAR_USERS;
commit;

insert into TWEET (id_str, text, created_at, time, geo_coordinates, in_reply_to_user_id_str, in_reply_to_screen_name, in_reply_to_status_id_str, status_url, from_user_id_str)
select distinct id_str, TEXTONEW, CREATED_AT, TIME, GEO_COORDINATES, IN_REPLY_TO_USER_ID_STR, IN_REPLY_TO_SCREEN_NAME, IN_REPLY_TO_STATUS_ID_STR, STATUS_URL, FROM_USER_ID_STR
from AUXILIAR;
commit;


insert into MENCIONES (id_mentions, id_strMen, screen_name, name)
SELECT id_mentions, IDS, screen_name, NAME
from DATA_USER_MEN x, TWEET t
where x.ids = t.id_str;
commit;


insert into URL_TWEET(ID_STRU, STATUS_URL, SOURCE, PROFILE_IMAGE_URL)
SELECT DISTINCT x.IDS_STR, s.status_url, s.SOURCENEW, s.PROFILE_IMAGE_URL
from AUXILIAR_URLTWEET x, AUXILIAR s
where x.IDS_STR = s.id_str;
COMMIT;


insert into HASHTAG (id_strH, text_h)
SELECT DISTINCT ids, HASHTAGS
from "AUXILIAR_HASHTAGS" x, TWEET t
where x.ids = t.id_str;
COMMIT;

insert into MEDIA_TWEET(media_url, id_strM, display_url, tipo, expanded_url)
SELECT DISTINCT MEDIA_URL, IDS_STR, DISPLAY_URL,TYPE, EXPANDED_URL
from "AUXILIAR_MEDIA" x, TWEET t
where x.IDS_STR = t.id_str;
COMMIT;

