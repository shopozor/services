from fixtures_generation.responses_generator import ShopCategoriesGenerator, ShopListsGenerator, ProductListsGenerator

import argparse


def generate_responses_for_variant(output_folder, variant):

    generator = ShopListsGenerator(output_folder, variant)
    generator.generate()

    generator = ShopCategoriesGenerator(output_folder, variant)
    generator.generate()

    generator = ProductListsGenerator(output_folder, variant)
    generator.generate()


def main(output_folder, fixture_variant):
    if fixture_variant == 'all':
        for variant in 'tiny', 'small', 'medium', 'large':
            generate_responses_for_variant(output_folder, variant)
    else:
        generate_responses_for_variant(output_folder, fixture_variant)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate the JSON expected responses to the GraphQL queries tested in the acceptance tests.')
    parser.add_argument('-o', '--output-folder', type=str, default='responses',
                        help='Folder where to output the JSON files')
    parser.add_argument('--fixture-variant', type=str, default='all',
                        help='Fixture variant: tiny, small, medium, large, or all')
    args = parser.parse_args()

    main(args.output_folder, args.fixture_variant)
