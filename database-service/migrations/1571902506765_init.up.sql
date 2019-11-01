CREATE FUNCTION public.set_current_timestamp_updated_at() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
DECLARE
  _new record;
BEGIN
  _new := NEW;
  _new."updated_at" = NOW();
  RETURN _new;
END;
$$;
CREATE TABLE public.addresses (
    user_id integer NOT NULL,
    street_address text NOT NULL,
    city text NOT NULL,
    postal_code smallint NOT NULL
);
CREATE SEQUENCE public.addresses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER SEQUENCE public.addresses_id_seq OWNED BY public.addresses.user_id;
CREATE TABLE public.images (
    product_id integer NOT NULL,
    url text NOT NULL,
    alt text
);
CREATE SEQUENCE public.images_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER SEQUENCE public.images_id_seq OWNED BY public.images.product_id;
CREATE TABLE public.pricing_modes (
    mode text NOT NULL
);
CREATE TABLE public.product_categories (
    name text NOT NULL,
    id integer NOT NULL,
    description text NOT NULL,
    background_image text NOT NULL
);
CREATE SEQUENCE public.product_categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER SEQUENCE public.product_categories_id_seq OWNED BY public.product_categories.id;
CREATE TABLE public.product_states (
    state text NOT NULL
);
CREATE TABLE public.products (
    id integer NOT NULL,
    name text NOT NULL,
    description text NOT NULL,
    publication_date timestamp with time zone DEFAULT now() NOT NULL,
    updated_at timestamp with time zone DEFAULT now() NOT NULL,
    state text DEFAULT 'INVISIBLE'::text NOT NULL,
    category_id integer NOT NULL,
    producer_id integer NOT NULL
);
CREATE SEQUENCE public.products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER SEQUENCE public.products_id_seq OWNED BY public.products.id;
CREATE TABLE public.productvariant_states (
    state text NOT NULL
);
CREATE TABLE public.productvariants (
    id integer NOT NULL,
    state text DEFAULT 'INVISIBLE'::text NOT NULL,
    product_id integer NOT NULL,
    quantity integer DEFAULT 0 NOT NULL,
    quantity_allocated integer DEFAULT 0 NOT NULL,
    gross_cost_price money DEFAULT 0 NOT NULL,
    pricing_mode text DEFAULT 'FREE'::text NOT NULL,
    name text NOT NULL,
    measure real NOT NULL,
    measure_unit text NOT NULL,
    gross_cost_price_unit text NOT NULL
);
CREATE SEQUENCE public.productvariants_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER SEQUENCE public.productvariants_id_seq OWNED BY public.productvariants.id;
CREATE TABLE public.shops (
    id integer NOT NULL,
    name character varying NOT NULL,
    description text NOT NULL,
    latitude numeric NOT NULL,
    longitude numeric NOT NULL
);
CREATE SEQUENCE public.shops_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER SEQUENCE public.shops_id_seq OWNED BY public.shops.id;
CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying NOT NULL,
    is_superuser boolean DEFAULT false NOT NULL,
    is_active boolean DEFAULT false NOT NULL,
    is_staff boolean DEFAULT false NOT NULL,
    first_name character varying,
    last_name character varying,
    description text
);
CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;
ALTER TABLE ONLY public.addresses ALTER COLUMN user_id SET DEFAULT nextval('public.addresses_id_seq'::regclass);
ALTER TABLE ONLY public.images ALTER COLUMN product_id SET DEFAULT nextval('public.images_id_seq'::regclass);
ALTER TABLE ONLY public.product_categories ALTER COLUMN id SET DEFAULT nextval('public.product_categories_id_seq'::regclass);
ALTER TABLE ONLY public.products ALTER COLUMN id SET DEFAULT nextval('public.products_id_seq'::regclass);
ALTER TABLE ONLY public.productvariants ALTER COLUMN id SET DEFAULT nextval('public.productvariants_id_seq'::regclass);
ALTER TABLE ONLY public.shops ALTER COLUMN id SET DEFAULT nextval('public.shops_id_seq'::regclass);
ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);
ALTER TABLE ONLY public.addresses
    ADD CONSTRAINT addresses_id_key UNIQUE (user_id);
ALTER TABLE ONLY public.addresses
    ADD CONSTRAINT addresses_pkey PRIMARY KEY (user_id);
ALTER TABLE ONLY public.images
    ADD CONSTRAINT images_id_key UNIQUE (product_id);
ALTER TABLE ONLY public.images
    ADD CONSTRAINT images_pkey PRIMARY KEY (product_id);
ALTER TABLE ONLY public.pricing_modes
    ADD CONSTRAINT pricing_modes_pkey PRIMARY KEY (mode);
ALTER TABLE ONLY public.product_categories
    ADD CONSTRAINT product_categories_category_key UNIQUE (name);
ALTER TABLE ONLY public.product_categories
    ADD CONSTRAINT product_categories_id_key UNIQUE (id);
ALTER TABLE ONLY public.product_states
    ADD CONSTRAINT product_states_pkey PRIMARY KEY (state);
ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id);
ALTER TABLE ONLY public.productvariant_states
    ADD CONSTRAINT productvariant_states_pkey PRIMARY KEY (state);
ALTER TABLE ONLY public.productvariants
    ADD CONSTRAINT productvariants_pkey PRIMARY KEY (id);
ALTER TABLE ONLY public.shops
    ADD CONSTRAINT shops_pkey PRIMARY KEY (id);
ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);
ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
CREATE TRIGGER set_public_products_updated_at BEFORE UPDATE ON public.products FOR EACH ROW EXECUTE PROCEDURE public.set_current_timestamp_updated_at();
COMMENT ON TRIGGER set_public_products_updated_at ON public.products IS 'trigger to set value of column "updated_at" to current timestamp on row update';
ALTER TABLE ONLY public.addresses
    ADD CONSTRAINT addresses_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON UPDATE RESTRICT ON DELETE CASCADE;
ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.product_categories(id) ON UPDATE RESTRICT ON DELETE RESTRICT;
ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_id_fkey FOREIGN KEY (id) REFERENCES public.images(product_id) ON UPDATE RESTRICT ON DELETE RESTRICT;
ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_producer_id_fkey FOREIGN KEY (producer_id) REFERENCES public.users(id) ON UPDATE RESTRICT ON DELETE RESTRICT;
ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_state_fkey FOREIGN KEY (state) REFERENCES public.product_states(state) ON UPDATE RESTRICT ON DELETE RESTRICT;
ALTER TABLE ONLY public.productvariants
    ADD CONSTRAINT productvariants_pricing_mode_fkey FOREIGN KEY (pricing_mode) REFERENCES public.pricing_modes(mode) ON UPDATE RESTRICT ON DELETE RESTRICT;
ALTER TABLE ONLY public.productvariants
    ADD CONSTRAINT productvariants_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(id) ON UPDATE RESTRICT ON DELETE CASCADE;
ALTER TABLE ONLY public.productvariants
    ADD CONSTRAINT productvariants_state_fkey FOREIGN KEY (state) REFERENCES public.productvariant_states(state) ON UPDATE RESTRICT ON DELETE RESTRICT;
