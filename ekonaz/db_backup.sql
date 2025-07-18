--
-- PostgreSQL database dump
--

-- Dumped from database version 17.5
-- Dumped by pg_dump version 17.5

-- Started on 2025-07-12 17:10:01

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- TOC entry 5002 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 222 (class 1259 OID 16399)
-- Name: city_; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.city_ (
    id bigint NOT NULL,
    name_ character varying(255) NOT NULL
);


ALTER TABLE public.city_ OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16398)
-- Name: city_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.city_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.city_id_seq OWNER TO postgres;

--
-- TOC entry 5003 (class 0 OID 0)
-- Dependencies: 221
-- Name: city_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.city_id_seq OWNED BY public.city_.id;


--
-- TOC entry 224 (class 1259 OID 16406)
-- Name: district_; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.district_ (
    id bigint NOT NULL,
    name_ character varying(255) NOT NULL,
    city_id bigint NOT NULL
);


ALTER TABLE public.district_ OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16405)
-- Name: district_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.district_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.district_id_seq OWNER TO postgres;

--
-- TOC entry 5004 (class 0 OID 0)
-- Dependencies: 223
-- Name: district_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.district_id_seq OWNED BY public.district_.id;


--
-- TOC entry 220 (class 1259 OID 16390)
-- Name: firm_; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.firm_ (
    id bigint NOT NULL,
    name_ character varying(255) NOT NULL,
    city_id bigint,
    district_id bigint,
    tax_office_id bigint,
    nace_id bigint,
    create_ timestamp without time zone,
    delete_ timestamp without time zone,
    address_ character varying(255),
    telephone_ character varying(255),
    fax_ character varying(255),
    email_ character varying(255),
    type_firm character varying(255),
    tax_ character varying(255),
    web_ character varying(255),
    sgk_sicil character varying(255),
    payment_ character varying(255),
    ceo_name character varying(255),
    ceo_email character varying(255),
    ceo_cell character varying(255),
    logo_media_id bigint,
    active_ boolean DEFAULT true NOT NULL
);


ALTER TABLE public.firm_ OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16389)
-- Name: firm_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.firm_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.firm_id_seq OWNER TO postgres;

--
-- TOC entry 5005 (class 0 OID 0)
-- Dependencies: 219
-- Name: firm_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.firm_id_seq OWNED BY public.firm_.id;


--
-- TOC entry 240 (class 1259 OID 17248)
-- Name: language_; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.language_ (
    id bigint NOT NULL,
    name_ character varying(255),
    short_ character varying(255)
);


ALTER TABLE public.language_ OWNER TO postgres;

--
-- TOC entry 239 (class 1259 OID 17247)
-- Name: language__id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.language__id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.language__id_seq OWNER TO postgres;

--
-- TOC entry 5006 (class 0 OID 0)
-- Dependencies: 239
-- Name: language__id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.language__id_seq OWNED BY public.language_.id;


--
-- TOC entry 230 (class 1259 OID 16963)
-- Name: media_; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.media_ (
    id bigint NOT NULL,
    create_ timestamp without time zone,
    media_type_id bigint,
    path_id bigint,
    name_ character varying(255),
    delete_ timestamp without time zone,
    active_ boolean DEFAULT true NOT NULL
);


ALTER TABLE public.media_ OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 16962)
-- Name: media_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.media_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.media_id_seq OWNER TO postgres;

--
-- TOC entry 5007 (class 0 OID 0)
-- Dependencies: 229
-- Name: media_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.media_id_seq OWNED BY public.media_.id;


--
-- TOC entry 232 (class 1259 OID 16982)
-- Name: media_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.media_type (
    id bigint NOT NULL,
    name_ character varying(255)
);


ALTER TABLE public.media_type OWNER TO postgres;

--
-- TOC entry 231 (class 1259 OID 16981)
-- Name: media_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.media_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.media_type_id_seq OWNER TO postgres;

--
-- TOC entry 5008 (class 0 OID 0)
-- Dependencies: 231
-- Name: media_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.media_type_id_seq OWNED BY public.media_type.id;


--
-- TOC entry 227 (class 1259 OID 16938)
-- Name: nace_; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.nace_ (
    id bigint NOT NULL,
    name_ character varying(255) NOT NULL,
    code_ character varying(15) NOT NULL,
    description_ character varying(511) NOT NULL
);


ALTER TABLE public.nace_ OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 16946)
-- Name: nace_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.nace_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.nace_id_seq OWNER TO postgres;

--
-- TOC entry 5009 (class 0 OID 0)
-- Dependencies: 228
-- Name: nace_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.nace_id_seq OWNED BY public.nace_.id;


--
-- TOC entry 234 (class 1259 OID 16994)
-- Name: path_; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.path_ (
    id bigint NOT NULL,
    name_ character varying(255) NOT NULL
);


ALTER TABLE public.path_ OWNER TO postgres;

--
-- TOC entry 233 (class 1259 OID 16993)
-- Name: path_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.path_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.path_id_seq OWNER TO postgres;

--
-- TOC entry 5010 (class 0 OID 0)
-- Dependencies: 233
-- Name: path_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.path_id_seq OWNED BY public.path_.id;


--
-- TOC entry 226 (class 1259 OID 16442)
-- Name: tax_office; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tax_office (
    id bigint NOT NULL,
    name_ character varying(255) NOT NULL,
    city_id bigint NOT NULL,
    district_id bigint NOT NULL
);


ALTER TABLE public.tax_office OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 16441)
-- Name: tax_office_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tax_office_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tax_office_id_seq OWNER TO postgres;

--
-- TOC entry 5011 (class 0 OID 0)
-- Dependencies: 225
-- Name: tax_office_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tax_office_id_seq OWNED BY public.tax_office.id;


--
-- TOC entry 236 (class 1259 OID 17008)
-- Name: user_; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_ (
    id bigint NOT NULL,
    user_group_id bigint NOT NULL,
    language_id bigint,
    name_ character varying(255),
    tckno_ character varying(11),
    certificate_number character varying(255),
    title_ character varying(255),
    email_ character varying(255),
    pasword_ character varying(32),
    logo_media_id bigint,
    active_ boolean DEFAULT true NOT NULL
);


ALTER TABLE public.user_ OWNER TO postgres;

--
-- TOC entry 235 (class 1259 OID 17007)
-- Name: user__id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user__id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user__id_seq OWNER TO postgres;

--
-- TOC entry 5012 (class 0 OID 0)
-- Dependencies: 235
-- Name: user__id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user__id_seq OWNED BY public.user_.id;


--
-- TOC entry 241 (class 1259 OID 17268)
-- Name: user_firm; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_firm (
    user_id bigint NOT NULL,
    firm_id bigint NOT NULL,
    create_ timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.user_firm OWNER TO postgres;

--
-- TOC entry 238 (class 1259 OID 17015)
-- Name: user_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_group (
    id bigint NOT NULL,
    name_ character varying(255),
    description_ character varying(511)
);


ALTER TABLE public.user_group OWNER TO postgres;

--
-- TOC entry 237 (class 1259 OID 17014)
-- Name: user_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_group_id_seq OWNER TO postgres;

--
-- TOC entry 5013 (class 0 OID 0)
-- Dependencies: 237
-- Name: user_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_group_id_seq OWNED BY public.user_group.id;


--
-- TOC entry 4800 (class 2604 OID 17052)
-- Name: city_ id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.city_ ALTER COLUMN id SET DEFAULT nextval('public.city_id_seq'::regclass);


--
-- TOC entry 4801 (class 2604 OID 17103)
-- Name: district_ id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.district_ ALTER COLUMN id SET DEFAULT nextval('public.district_id_seq'::regclass);


--
-- TOC entry 4798 (class 2604 OID 17043)
-- Name: firm_ id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.firm_ ALTER COLUMN id SET DEFAULT nextval('public.firm_id_seq'::regclass);


--
-- TOC entry 4811 (class 2604 OID 17251)
-- Name: language_ id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.language_ ALTER COLUMN id SET DEFAULT nextval('public.language__id_seq'::regclass);


--
-- TOC entry 4804 (class 2604 OID 16966)
-- Name: media_ id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.media_ ALTER COLUMN id SET DEFAULT nextval('public.media_id_seq'::regclass);


--
-- TOC entry 4806 (class 2604 OID 17188)
-- Name: media_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.media_type ALTER COLUMN id SET DEFAULT nextval('public.media_type_id_seq'::regclass);


--
-- TOC entry 4803 (class 2604 OID 17163)
-- Name: nace_ id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.nace_ ALTER COLUMN id SET DEFAULT nextval('public.nace_id_seq'::regclass);


--
-- TOC entry 4807 (class 2604 OID 17209)
-- Name: path_ id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.path_ ALTER COLUMN id SET DEFAULT nextval('public.path_id_seq'::regclass);


--
-- TOC entry 4802 (class 2604 OID 17140)
-- Name: tax_office id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tax_office ALTER COLUMN id SET DEFAULT nextval('public.tax_office_id_seq'::regclass);


--
-- TOC entry 4808 (class 2604 OID 17230)
-- Name: user_ id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_ ALTER COLUMN id SET DEFAULT nextval('public.user__id_seq'::regclass);


--
-- TOC entry 4810 (class 2604 OID 17237)
-- Name: user_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_group ALTER COLUMN id SET DEFAULT nextval('public.user_group_id_seq'::regclass);


--
-- TOC entry 4816 (class 2606 OID 17054)
-- Name: city_ city_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.city_
    ADD CONSTRAINT city_pkey PRIMARY KEY (id);


--
-- TOC entry 4818 (class 2606 OID 17105)
-- Name: district_ district_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.district_
    ADD CONSTRAINT district_pkey PRIMARY KEY (id);


--
-- TOC entry 4814 (class 2606 OID 17045)
-- Name: firm_ firm_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.firm_
    ADD CONSTRAINT firm_pkey PRIMARY KEY (id);


--
-- TOC entry 4834 (class 2606 OID 17255)
-- Name: language_ language__pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.language_
    ADD CONSTRAINT language__pkey PRIMARY KEY (id);


--
-- TOC entry 4824 (class 2606 OID 16968)
-- Name: media_ media_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.media_
    ADD CONSTRAINT media_pkey PRIMARY KEY (id);


--
-- TOC entry 4826 (class 2606 OID 17190)
-- Name: media_type media_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.media_type
    ADD CONSTRAINT media_type_pkey PRIMARY KEY (id);


--
-- TOC entry 4822 (class 2606 OID 17165)
-- Name: nace_ nace_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.nace_
    ADD CONSTRAINT nace_pkey PRIMARY KEY (id);


--
-- TOC entry 4828 (class 2606 OID 17211)
-- Name: path_ path_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.path_
    ADD CONSTRAINT path_pkey PRIMARY KEY (id);


--
-- TOC entry 4820 (class 2606 OID 17142)
-- Name: tax_office tax_office_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tax_office
    ADD CONSTRAINT tax_office_pkey PRIMARY KEY (id);


--
-- TOC entry 4830 (class 2606 OID 17232)
-- Name: user_ user__pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_
    ADD CONSTRAINT user__pkey PRIMARY KEY (id);


--
-- TOC entry 4836 (class 2606 OID 17273)
-- Name: user_firm user_firm_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_firm
    ADD CONSTRAINT user_firm_pkey PRIMARY KEY (user_id, firm_id);


--
-- TOC entry 4832 (class 2606 OID 17239)
-- Name: user_group user_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_group
    ADD CONSTRAINT user_group_pkey PRIMARY KEY (id);


--
-- TOC entry 4842 (class 2606 OID 17094)
-- Name: district_ district_city_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.district_
    ADD CONSTRAINT district_city_id_fkey FOREIGN KEY (city_id) REFERENCES public.city_(id) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 4837 (class 2606 OID 17074)
-- Name: firm_ firm_city_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.firm_
    ADD CONSTRAINT firm_city_id_fkey FOREIGN KEY (city_id) REFERENCES public.city_(id);


--
-- TOC entry 4838 (class 2606 OID 17120)
-- Name: firm_ firm_district_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.firm_
    ADD CONSTRAINT firm_district_id_fkey FOREIGN KEY (district_id) REFERENCES public.district_(id);


--
-- TOC entry 4839 (class 2606 OID 17290)
-- Name: firm_ firm_logo_media_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.firm_
    ADD CONSTRAINT firm_logo_media_id_fkey FOREIGN KEY (logo_media_id) REFERENCES public.media_(id) ON DELETE SET NULL;


--
-- TOC entry 4840 (class 2606 OID 17177)
-- Name: firm_ firm_nace_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.firm_
    ADD CONSTRAINT firm_nace_id_fkey FOREIGN KEY (nace_id) REFERENCES public.nace_(id);


--
-- TOC entry 4841 (class 2606 OID 17152)
-- Name: firm_ firm_tax_office_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.firm_
    ADD CONSTRAINT firm_tax_office_id_fkey FOREIGN KEY (tax_office_id) REFERENCES public.tax_office(id);


--
-- TOC entry 4845 (class 2606 OID 17200)
-- Name: media_ media_media_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.media_
    ADD CONSTRAINT media_media_type_id_fkey FOREIGN KEY (media_type_id) REFERENCES public.media_type(id);


--
-- TOC entry 4846 (class 2606 OID 17221)
-- Name: media_ media_path_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.media_
    ADD CONSTRAINT media_path_id_fkey FOREIGN KEY (path_id) REFERENCES public.path_(id);


--
-- TOC entry 4843 (class 2606 OID 17085)
-- Name: tax_office tax_office_city_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tax_office
    ADD CONSTRAINT tax_office_city_id_fkey FOREIGN KEY (city_id) REFERENCES public.city_(id);


--
-- TOC entry 4844 (class 2606 OID 17131)
-- Name: tax_office tax_office_district_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tax_office
    ADD CONSTRAINT tax_office_district_id_fkey FOREIGN KEY (district_id) REFERENCES public.district_(id);


--
-- TOC entry 4847 (class 2606 OID 17263)
-- Name: user_ user__language_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_
    ADD CONSTRAINT user__language_id_fkey FOREIGN KEY (language_id) REFERENCES public.language_(id);


--
-- TOC entry 4848 (class 2606 OID 17285)
-- Name: user_ user__logo_media_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_
    ADD CONSTRAINT user__logo_media_id_fkey FOREIGN KEY (logo_media_id) REFERENCES public.media_(id) ON DELETE SET NULL;


--
-- TOC entry 4849 (class 2606 OID 17258)
-- Name: user_ user__user_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_
    ADD CONSTRAINT user__user_group_id_fkey FOREIGN KEY (user_group_id) REFERENCES public.user_group(id);


--
-- TOC entry 4850 (class 2606 OID 17279)
-- Name: user_firm user_firm_firm_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_firm
    ADD CONSTRAINT user_firm_firm_id_fkey FOREIGN KEY (firm_id) REFERENCES public.firm_(id) ON DELETE CASCADE;


--
-- TOC entry 4851 (class 2606 OID 17274)
-- Name: user_firm user_firm_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_firm
    ADD CONSTRAINT user_firm_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.user_(id) ON DELETE CASCADE;


-- Completed on 2025-07-12 17:10:01

--
-- PostgreSQL database dump complete
--

