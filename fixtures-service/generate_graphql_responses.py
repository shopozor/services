from responses_generator import ShopCategoriesGenerator, ShopListsGenerator, ProductListsGenerator

import argparse


def generate_responses_for_fixture_set(output_folder, fixture_set):

    generator = ShopListsGenerator(output_folder, fixture_set)
    generator.generate()

    generator = ShopCategoriesGenerator(output_folder, fixture_set)
    generator.generate()

    generator = ProductListsGenerator(output_folder, fixture_set)
    generator.generate()


def main(output_folder, fixture_set):
    if fixture_set == 'all':
        for set in 'tiny', 'small', 'medium', 'large':
            generate_responses_for_fixture_set(output_folder, set)
    else:
        generate_responses_for_fixture_set(output_folder, fixture_set)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate the JSON expected responses to the GraphQL queries tested in the acceptance tests.')
    parser.add_argument('-o', '--output-folder', type=str, default='responses',
                        help='Folder where to output the JSON files')
    parser.add_argument('--fixture-set', type=str, default='all',
                        help='Fixture set: tiny, small, medium, large, or all')
    args = parser.parse_args()

    main(args.output_folder, args.fixture_set)
