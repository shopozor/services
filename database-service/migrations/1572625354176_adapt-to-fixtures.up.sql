
ALTER TABLE "public"."product_categories" ADD COLUMN "background_image_alt" text NUL;
ALTER TABLE "public"."products" ADD COLUMN "conservation_mode" text NULL;
ALTER TABLE "public"."products" ADD COLUMN "conservation_days" integer NULL;
ALTER TABLE "public"."products" ADD COLUMN "vat_rate" float4 NULL;