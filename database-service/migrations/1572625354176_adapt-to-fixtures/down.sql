
ALTER TABLE "public"."products" DROP COLUMN "vat_rate";
ALTER TABLE "public"."products" DROP COLUMN "conservation_days";
ALTER TABLE "public"."products" DROP COLUMN "conservation_mode" text NULL;
ALTER TABLE "public"."product_categories" DROP COLUMN "background_image_alt" text NULL;