CREATE DATABASE biblioteca_galapagos
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Ecuador.1252'
    LC_CTYPE = 'Spanish_Ecuador.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
	
	
	
	-- Table: public.auth_group

-- DROP TABLE IF EXISTS public.auth_group;

CREATE TABLE IF NOT EXISTS public.auth_group
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT auth_group_pkey PRIMARY KEY (id),
    CONSTRAINT auth_group_name_key UNIQUE (name)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.auth_group
    OWNER to postgres;

GRANT ALL ON TABLE public.auth_group TO postgres WITH GRANT OPTION;
-- Index: auth_group_name_a6ea08ec_like

-- DROP INDEX IF EXISTS public.auth_group_name_a6ea08ec_like;

CREATE INDEX IF NOT EXISTS auth_group_name_a6ea08ec_like
    ON public.auth_group USING btree
    (name COLLATE pg_catalog."default" varchar_pattern_ops ASC NULLS LAST)
    TABLESPACE pg_default;
	
	
	
	-- Table: public.auth_group_permissions

-- DROP TABLE IF EXISTS public.auth_group_permissions;

CREATE TABLE IF NOT EXISTS public.auth_group_permissions
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    group_id integer NOT NULL,
    permission_id integer NOT NULL,
    CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id),
    CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id),
    CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id)
        REFERENCES public.auth_permission (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id)
        REFERENCES public.auth_group (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.auth_group_permissions
    OWNER to postgres;

GRANT ALL ON TABLE public.auth_group_permissions TO postgres WITH GRANT OPTION;
-- Index: auth_group_permissions_group_id_b120cbf9

-- DROP INDEX IF EXISTS public.auth_group_permissions_group_id_b120cbf9;

CREATE INDEX IF NOT EXISTS auth_group_permissions_group_id_b120cbf9
    ON public.auth_group_permissions USING btree
    (group_id ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: auth_group_permissions_permission_id_84c5c92e

-- DROP INDEX IF EXISTS public.auth_group_permissions_permission_id_84c5c92e;

CREATE INDEX IF NOT EXISTS auth_group_permissions_permission_id_84c5c92e
    ON public.auth_group_permissions USING btree
    (permission_id ASC NULLS LAST)
    TABLESPACE pg_default;
	
	
	
	
-- Table: public.auth_permission

-- DROP TABLE IF EXISTS public.auth_permission;

CREATE TABLE IF NOT EXISTS public.auth_permission
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT auth_permission_pkey PRIMARY KEY (id),
    CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename),
    CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id)
        REFERENCES public.django_content_type (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.auth_permission
    OWNER to postgres;

GRANT ALL ON TABLE public.auth_permission TO postgres WITH GRANT OPTION;
-- Index: auth_permission_content_type_id_2f476e4b

-- DROP INDEX IF EXISTS public.auth_permission_content_type_id_2f476e4b;

CREATE INDEX IF NOT EXISTS auth_permission_content_type_id_2f476e4b
    ON public.auth_permission USING btree
    (content_type_id ASC NULLS LAST)
    TABLESPACE pg_default;	
	
	
	
-- Table: public.auth_user

-- DROP TABLE IF EXISTS public.auth_user;

CREATE TABLE IF NOT EXISTS public.auth_user
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    password character varying(128) COLLATE pg_catalog."default" NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) COLLATE pg_catalog."default" NOT NULL,
    first_name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    email character varying(254) COLLATE pg_catalog."default" NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    CONSTRAINT auth_user_pkey PRIMARY KEY (id),
    CONSTRAINT auth_user_username_key UNIQUE (username)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.auth_user
    OWNER to postgres;

GRANT ALL ON TABLE public.auth_user TO postgres WITH GRANT OPTION;
-- Index: auth_user_username_6821ab7c_like

-- DROP INDEX IF EXISTS public.auth_user_username_6821ab7c_like;

CREATE INDEX IF NOT EXISTS auth_user_username_6821ab7c_like
    ON public.auth_user USING btree
    (username COLLATE pg_catalog."default" varchar_pattern_ops ASC NULLS LAST)
    TABLESPACE pg_default;



	-- Table: public.auth_user

-- DROP TABLE IF EXISTS public.auth_user;

CREATE TABLE IF NOT EXISTS public.auth_user
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    password character varying(128) COLLATE pg_catalog."default" NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) COLLATE pg_catalog."default" NOT NULL,
    first_name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    email character varying(254) COLLATE pg_catalog."default" NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    CONSTRAINT auth_user_pkey PRIMARY KEY (id),
    CONSTRAINT auth_user_username_key UNIQUE (username)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.auth_user
    OWNER to postgres;

GRANT ALL ON TABLE public.auth_user TO postgres WITH GRANT OPTION;
-- Index: auth_user_username_6821ab7c_like

-- DROP INDEX IF EXISTS public.auth_user_username_6821ab7c_like;

CREATE INDEX IF NOT EXISTS auth_user_username_6821ab7c_like
    ON public.auth_user USING btree
    (username COLLATE pg_catalog."default" varchar_pattern_ops ASC NULLS LAST)
    TABLESPACE pg_default;
	
	
	
-- Table: public.auth_user_user_permissions

-- DROP TABLE IF EXISTS public.auth_user_user_permissions;

CREATE TABLE IF NOT EXISTS public.auth_user_user_permissions
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    user_id integer NOT NULL,
    permission_id integer NOT NULL,
    CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id),
    CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id),
    CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id)
        REFERENCES public.auth_permission (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id)
        REFERENCES public.auth_user (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.auth_user_user_permissions
    OWNER to postgres;

GRANT ALL ON TABLE public.auth_user_user_permissions TO postgres WITH GRANT OPTION;
-- Index: auth_user_user_permissions_permission_id_1fbb5f2c

-- DROP INDEX IF EXISTS public.auth_user_user_permissions_permission_id_1fbb5f2c;

CREATE INDEX IF NOT EXISTS auth_user_user_permissions_permission_id_1fbb5f2c
    ON public.auth_user_user_permissions USING btree
    (permission_id ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: auth_user_user_permissions_user_id_a95ead1b

-- DROP INDEX IF EXISTS public.auth_user_user_permissions_user_id_a95ead1b;

CREATE INDEX IF NOT EXISTS auth_user_user_permissions_user_id_a95ead1b
    ON public.auth_user_user_permissions USING btree
    (user_id ASC NULLS LAST)
    TABLESPACE pg_default;	
	
	
	
-- Table: public.catalogos

-- DROP TABLE IF EXISTS public.catalogos;

CREATE TABLE IF NOT EXISTS public.catalogos
(
    id bigint NOT NULL,
    catalogo character varying(50) COLLATE pg_catalog."default",
    estado character varying(20) COLLATE pg_catalog."default",
    CONSTRAINT catalogo_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.catalogos
    OWNER to postgres;	
	
	
	
	
-- Table: public.django_admin_log

-- DROP TABLE IF EXISTS public.django_admin_log;

CREATE TABLE IF NOT EXISTS public.django_admin_log
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    action_time timestamp with time zone NOT NULL,
    object_id text COLLATE pg_catalog."default",
    object_repr character varying(200) COLLATE pg_catalog."default" NOT NULL,
    action_flag smallint NOT NULL,
    change_message text COLLATE pg_catalog."default" NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_pkey PRIMARY KEY (id),
    CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id)
        REFERENCES public.django_content_type (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id)
        REFERENCES public.auth_user (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT django_admin_log_action_flag_check CHECK (action_flag >= 0)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.django_admin_log
    OWNER to postgres;

GRANT ALL ON TABLE public.django_admin_log TO postgres WITH GRANT OPTION;
-- Index: django_admin_log_content_type_id_c4bce8eb

-- DROP INDEX IF EXISTS public.django_admin_log_content_type_id_c4bce8eb;

CREATE INDEX IF NOT EXISTS django_admin_log_content_type_id_c4bce8eb
    ON public.django_admin_log USING btree
    (content_type_id ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: django_admin_log_user_id_c564eba6

-- DROP INDEX IF EXISTS public.django_admin_log_user_id_c564eba6;

CREATE INDEX IF NOT EXISTS django_admin_log_user_id_c564eba6
    ON public.django_admin_log USING btree
    (user_id ASC NULLS LAST)
    TABLESPACE pg_default;	
	
	
	
-- Table: public.django_content_type

-- DROP TABLE IF EXISTS public.django_content_type;

CREATE TABLE IF NOT EXISTS public.django_content_type
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    app_label character varying(100) COLLATE pg_catalog."default" NOT NULL,
    model character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT django_content_type_pkey PRIMARY KEY (id),
    CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.django_content_type
    OWNER to postgres;

GRANT ALL ON TABLE public.django_content_type TO postgres WITH GRANT OPTION;




-- Table: public.django_migrations

-- DROP TABLE IF EXISTS public.django_migrations;

CREATE TABLE IF NOT EXISTS public.django_migrations
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    app character varying(255) COLLATE pg_catalog."default" NOT NULL,
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    applied timestamp with time zone NOT NULL,
    CONSTRAINT django_migrations_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.django_migrations
    OWNER to postgres;

GRANT ALL ON TABLE public.django_migrations TO postgres WITH GRANT OPTION;	




-- Table: public.django_session

-- DROP TABLE IF EXISTS public.django_session;

CREATE TABLE IF NOT EXISTS public.django_session
(
    session_key character varying(40) COLLATE pg_catalog."default" NOT NULL,
    session_data text COLLATE pg_catalog."default" NOT NULL,
    expire_date timestamp with time zone NOT NULL,
    CONSTRAINT django_session_pkey PRIMARY KEY (session_key)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.django_session
    OWNER to postgres;

GRANT ALL ON TABLE public.django_session TO postgres WITH GRANT OPTION;
-- Index: django_session_expire_date_a5c62663

-- DROP INDEX IF EXISTS public.django_session_expire_date_a5c62663;

CREATE INDEX IF NOT EXISTS django_session_expire_date_a5c62663
    ON public.django_session USING btree
    (expire_date ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: django_session_session_key_c0390e0f_like

-- DROP INDEX IF EXISTS public.django_session_session_key_c0390e0f_like;

CREATE INDEX IF NOT EXISTS django_session_session_key_c0390e0f_like
    ON public.django_session USING btree
    (session_key COLLATE pg_catalog."default" varchar_pattern_ops ASC NULLS LAST)
    TABLESPACE pg_default;
	
	
	
-- Table: public.usuarios

-- DROP TABLE IF EXISTS public.usuarios;

CREATE TABLE IF NOT EXISTS public.usuarios
(
    cedula character varying(10) COLLATE pg_catalog."default",
    nombre character varying(100) COLLATE pg_catalog."default",
    apellido character varying(100) COLLATE pg_catalog."default",
    fecha_nacimiento date,
    telefono character varying(15) COLLATE pg_catalog."default",
    correo character varying(50) COLLATE pg_catalog."default",
    institucion character varying(100) COLLATE pg_catalog."default",
    es_superusuario smallint,
    genero character varying(10) COLLATE pg_catalog."default",
    nacionalidad character varying(50) COLLATE pg_catalog."default",
    etnia character varying(50) COLLATE pg_catalog."default",
    discapacidad character varying(5) COLLATE pg_catalog."default",
    recibir_informacion character varying(5) COLLATE pg_catalog."default",
    id bigint NOT NULL DEFAULT nextval('usuarios_id_seq'::regclass),
    CONSTRAINT usuarios_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.usuarios
    OWNER to postgres;

GRANT ALL ON TABLE public.usuarios TO postgres WITH GRANT OPTION;	



-- Table: public.visitas

-- DROP TABLE IF EXISTS public.visitas;

CREATE TABLE IF NOT EXISTS public.visitas
(
    "userId" smallint,
    "catalogoId" smallint,
    taller character varying(100) COLLATE pg_catalog."default",
    actividad character varying(100) COLLATE pg_catalog."default",
    id bigint NOT NULL DEFAULT nextval('visitas_id_seq'::regclass),
    fecha character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT visitas_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.visitas
    OWNER to postgres;