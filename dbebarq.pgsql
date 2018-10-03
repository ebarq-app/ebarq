--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.14
-- Dumped by pg_dump version 9.5.14

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: EBARQWebApp_addperformance; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."EBARQWebApp_addperformance" (
    id integer NOT NULL,
    "time" time without time zone NOT NULL,
    type character varying(100) NOT NULL,
    duration time without time zone NOT NULL,
    additional character varying(100) NOT NULL,
    horse_id integer NOT NULL
);


ALTER TABLE public."EBARQWebApp_addperformance" OWNER TO admin;

--
-- Name: EBARQWebApp_addperformance_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public."EBARQWebApp_addperformance_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."EBARQWebApp_addperformance_id_seq" OWNER TO admin;

--
-- Name: EBARQWebApp_addperformance_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public."EBARQWebApp_addperformance_id_seq" OWNED BY public."EBARQWebApp_addperformance".id;


--
-- Name: EBARQWebApp_addreminder; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."EBARQWebApp_addreminder" (
    id integer NOT NULL,
    event character varying(100) NOT NULL,
    "time" time without time zone NOT NULL,
    date date NOT NULL,
    notes character varying(250) NOT NULL,
    horse_id integer NOT NULL
);


ALTER TABLE public."EBARQWebApp_addreminder" OWNER TO admin;

--
-- Name: EBARQWebApp_addreminder_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public."EBARQWebApp_addreminder_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."EBARQWebApp_addreminder_id_seq" OWNER TO admin;

--
-- Name: EBARQWebApp_addreminder_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public."EBARQWebApp_addreminder_id_seq" OWNED BY public."EBARQWebApp_addreminder".id;


--
-- Name: EBARQWebApp_horse; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."EBARQWebApp_horse" (
    id integer NOT NULL,
    whorl character varying(100) NOT NULL,
    side_face character varying(100) NOT NULL,
    full_side character varying(100) NOT NULL,
    name character varying(50) NOT NULL,
    age integer NOT NULL,
    gender character varying(6) NOT NULL,
    date_of_birth date NOT NULL,
    weight integer NOT NULL,
    height integer NOT NULL,
    horse_owner_id integer NOT NULL
);


ALTER TABLE public."EBARQWebApp_horse" OWNER TO admin;

--
-- Name: EBARQWebApp_horse_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public."EBARQWebApp_horse_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."EBARQWebApp_horse_id_seq" OWNER TO admin;

--
-- Name: EBARQWebApp_horse_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public."EBARQWebApp_horse_id_seq" OWNED BY public."EBARQWebApp_horse".id;


--
-- Name: EBARQWebApp_horseowner; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."EBARQWebApp_horseowner" (
    id integer NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    user_id_id integer NOT NULL
);


ALTER TABLE public."EBARQWebApp_horseowner" OWNER TO admin;

--
-- Name: EBARQWebApp_horseowner_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public."EBARQWebApp_horseowner_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."EBARQWebApp_horseowner_id_seq" OWNER TO admin;

--
-- Name: EBARQWebApp_horseowner_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public."EBARQWebApp_horseowner_id_seq" OWNED BY public."EBARQWebApp_horseowner".id;


--
-- Name: EBARQWebApp_question; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."EBARQWebApp_question" (
    id integer NOT NULL,
    question character varying(100) NOT NULL,
    answer character varying(100) NOT NULL,
    horse_id integer NOT NULL
);


ALTER TABLE public."EBARQWebApp_question" OWNER TO admin;

--
-- Name: EBARQWebApp_question_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public."EBARQWebApp_question_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."EBARQWebApp_question_id_seq" OWNER TO admin;

--
-- Name: EBARQWebApp_question_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public."EBARQWebApp_question_id_seq" OWNED BY public."EBARQWebApp_question".id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO admin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO admin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO admin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO admin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO admin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO admin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO admin;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO admin;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO admin;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO admin;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO admin;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO admin;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO admin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO admin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO admin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO admin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO admin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO admin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO admin;

--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."EBARQWebApp_addperformance" ALTER COLUMN id SET DEFAULT nextval('public."EBARQWebApp_addperformance_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."EBARQWebApp_addreminder" ALTER COLUMN id SET DEFAULT nextval('public."EBARQWebApp_addreminder_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."EBARQWebApp_horse" ALTER COLUMN id SET DEFAULT nextval('public."EBARQWebApp_horse_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."EBARQWebApp_horseowner" ALTER COLUMN id SET DEFAULT nextval('public."EBARQWebApp_horseowner_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."EBARQWebApp_question" ALTER COLUMN id SET DEFAULT nextval('public."EBARQWebApp_question_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Data for Name: EBARQWebApp_addperformance; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."EBARQWebApp_addperformance" (id, "time", type, duration, additional, horse_id) FROM stdin;
\.


--
-- Name: EBARQWebApp_addperformance_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public."EBARQWebApp_addperformance_id_seq"', 1, false);


--
-- Data for Name: EBARQWebApp_addreminder; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."EBARQWebApp_addreminder" (id, event, "time", date, notes, horse_id) FROM stdin;
\.


--
-- Name: EBARQWebApp_addreminder_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public."EBARQWebApp_addreminder_id_seq"', 1, false);


--
-- Data for Name: EBARQWebApp_horse; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."EBARQWebApp_horse" (id, whorl, side_face, full_side, name, age, gender, date_of_birth, weight, height, horse_owner_id) FROM stdin;
1	operaHouse_I7of4vJ.jpg	parking_5zLCmhH.jpg	AD10.png	Bobbie	12	Male	2006-08-01	21	31	1
\.


--
-- Name: EBARQWebApp_horse_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public."EBARQWebApp_horse_id_seq"', 1, true);


--
-- Data for Name: EBARQWebApp_horseowner; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."EBARQWebApp_horseowner" (id, first_name, last_name, user_id_id) FROM stdin;
1	Eggo	Beggo	1
\.


--
-- Name: EBARQWebApp_horseowner_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public."EBARQWebApp_horseowner_id_seq"', 1, true);


--
-- Data for Name: EBARQWebApp_question; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."EBARQWebApp_question" (id, question, answer, horse_id) FROM stdin;
\.


--
-- Name: EBARQWebApp_question_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public."EBARQWebApp_question_id_seq"', 1, false);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add horse	1	add_horse
2	Can change horse	1	change_horse
3	Can delete horse	1	delete_horse
4	Can view horse	1	view_horse
5	Can add horse owner	2	add_horseowner
6	Can change horse owner	2	change_horseowner
7	Can delete horse owner	2	delete_horseowner
8	Can view horse owner	2	view_horseowner
9	Can add question	3	add_question
10	Can change question	3	change_question
11	Can delete question	3	delete_question
12	Can view question	3	view_question
13	Can add add performance	4	add_addperformance
14	Can change add performance	4	change_addperformance
15	Can delete add performance	4	delete_addperformance
16	Can view add performance	4	view_addperformance
17	Can add add reminder	5	add_addreminder
18	Can change add reminder	5	change_addreminder
19	Can delete add reminder	5	delete_addreminder
20	Can view add reminder	5	view_addreminder
21	Can add log entry	6	add_logentry
22	Can change log entry	6	change_logentry
23	Can delete log entry	6	delete_logentry
24	Can view log entry	6	view_logentry
25	Can add permission	7	add_permission
26	Can change permission	7	change_permission
27	Can delete permission	7	delete_permission
28	Can view permission	7	view_permission
29	Can add group	8	add_group
30	Can change group	8	change_group
31	Can delete group	8	delete_group
32	Can view group	8	view_group
33	Can add user	9	add_user
34	Can change user	9	change_user
35	Can delete user	9	delete_user
36	Can view user	9	view_user
37	Can add content type	10	add_contenttype
38	Can change content type	10	change_contenttype
39	Can delete content type	10	delete_contenttype
40	Can view content type	10	view_contenttype
41	Can add session	11	add_session
42	Can change session	11	change_session
43	Can delete session	11	delete_session
44	Can view session	11	view_session
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 44, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$120000$3daSIeUYpouC$oTsd/9F07cUA+r5dnmQd/qbZ2KeH3XO0WPt8mwKwQjA=	2018-09-29 15:23:35.13159+10	f	test3	Eggo	Beggo	ebor2482@fakemail.com	f	t	2018-09-29 15:22:55.278056+10
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	EBARQWebApp	horse
2	EBARQWebApp	horseowner
3	EBARQWebApp	question
4	EBARQWebApp	addperformance
5	EBARQWebApp	addreminder
6	admin	logentry
7	auth	permission
8	auth	group
9	auth	user
10	contenttypes	contenttype
11	sessions	session
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 11, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2018-09-29 15:21:10.616481+10
2	auth	0001_initial	2018-09-29 15:21:11.674376+10
3	EBARQWebApp	0001_initial	2018-09-29 15:21:12.154276+10
4	EBARQWebApp	0002_addperformance_addreminder	2018-09-29 15:21:12.465539+10
5	admin	0001_initial	2018-09-29 15:21:12.732688+10
6	admin	0002_logentry_remove_auto_add	2018-09-29 15:21:12.773409+10
7	admin	0003_logentry_add_action_flag_choices	2018-09-29 15:21:12.813737+10
8	contenttypes	0002_remove_content_type_name	2018-09-29 15:21:12.920349+10
9	auth	0002_alter_permission_name_max_length	2018-09-29 15:21:12.954368+10
10	auth	0003_alter_user_email_max_length	2018-09-29 15:21:12.997931+10
11	auth	0004_alter_user_username_opts	2018-09-29 15:21:13.039503+10
12	auth	0005_alter_user_last_login_null	2018-09-29 15:21:13.097615+10
13	auth	0006_require_contenttypes_0002	2018-09-29 15:21:13.108285+10
14	auth	0007_alter_validators_add_error_messages	2018-09-29 15:21:13.148508+10
15	auth	0008_alter_user_username_max_length	2018-09-29 15:21:13.276475+10
16	auth	0009_alter_user_last_name_max_length	2018-09-29 15:21:13.320612+10
17	sessions	0001_initial	2018-09-29 15:21:13.510268+10
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 17, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
eab94je9awcylb1r1714l9iqx80110o3	MDNiNTAxMGM0NTEwY2IwYjZlNDZmZjc0OGMyM2VjNWZhMTM0NjU0NDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyNDc2YWIxNzc4NzdjOTljZWMxMWJiMzYxOGM0MGFjOGQwMTQ5ZmYzIn0=	2018-10-13 16:23:35.164816+11
\.


--
-- Name: EBARQWebApp_addperformance_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."EBARQWebApp_addperformance"
    ADD CONSTRAINT "EBARQWebApp_addperformance_pkey" PRIMARY KEY (id);


--
-- Name: EBARQWebApp_addreminder_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."EBARQWebApp_addreminder"
    ADD CONSTRAINT "EBARQWebApp_addreminder_pkey" PRIMARY KEY (id);


--
-- Name: EBARQWebApp_horse_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."EBARQWebApp_horse"
    ADD CONSTRAINT "EBARQWebApp_horse_pkey" PRIMARY KEY (id);


--
-- Name: EBARQWebApp_horseowner_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."EBARQWebApp_horseowner"
    ADD CONSTRAINT "EBARQWebApp_horseowner_pkey" PRIMARY KEY (id);


--
-- Name: EBARQWebApp_question_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."EBARQWebApp_question"
    ADD CONSTRAINT "EBARQWebApp_question_pkey" PRIMARY KEY (id);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: EBARQWebApp_addperformance_horse_id_ed7011c8; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX "EBARQWebApp_addperformance_horse_id_ed7011c8" ON public."EBARQWebApp_addperformance" USING btree (horse_id);


--
-- Name: EBARQWebApp_addreminder_horse_id_448834bc; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX "EBARQWebApp_addreminder_horse_id_448834bc" ON public."EBARQWebApp_addreminder" USING btree (horse_id);


--
-- Name: EBARQWebApp_horse_horse_owner_id_7a4c754f; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX "EBARQWebApp_horse_horse_owner_id_7a4c754f" ON public."EBARQWebApp_horse" USING btree (horse_owner_id);


--
-- Name: EBARQWebApp_horseowner_user_id_id_1a4f714f; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX "EBARQWebApp_horseowner_user_id_id_1a4f714f" ON public."EBARQWebApp_horseowner" USING btree (user_id_id);


--
-- Name: EBARQWebApp_question_horse_id_aa918b9e; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX "EBARQWebApp_question_horse_id_aa918b9e" ON public."EBARQWebApp_question" USING btree (horse_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: EBARQWebApp_addperfo_horse_id_ed7011c8_fk_EBARQWebA; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."EBARQWebApp_addperformance"
    ADD CONSTRAINT "EBARQWebApp_addperfo_horse_id_ed7011c8_fk_EBARQWebA" FOREIGN KEY (horse_id) REFERENCES public."EBARQWebApp_horse"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: EBARQWebApp_addremin_horse_id_448834bc_fk_EBARQWebA; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."EBARQWebApp_addreminder"
    ADD CONSTRAINT "EBARQWebApp_addremin_horse_id_448834bc_fk_EBARQWebA" FOREIGN KEY (horse_id) REFERENCES public."EBARQWebApp_horse"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: EBARQWebApp_horse_horse_owner_id_7a4c754f_fk_EBARQWebA; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."EBARQWebApp_horse"
    ADD CONSTRAINT "EBARQWebApp_horse_horse_owner_id_7a4c754f_fk_EBARQWebA" FOREIGN KEY (horse_owner_id) REFERENCES public."EBARQWebApp_horseowner"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: EBARQWebApp_horseowner_user_id_id_1a4f714f_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."EBARQWebApp_horseowner"
    ADD CONSTRAINT "EBARQWebApp_horseowner_user_id_id_1a4f714f_fk_auth_user_id" FOREIGN KEY (user_id_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: EBARQWebApp_question_horse_id_aa918b9e_fk_EBARQWebApp_horse_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."EBARQWebApp_question"
    ADD CONSTRAINT "EBARQWebApp_question_horse_id_aa918b9e_fk_EBARQWebApp_horse_id" FOREIGN KEY (horse_id) REFERENCES public."EBARQWebApp_horse"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

