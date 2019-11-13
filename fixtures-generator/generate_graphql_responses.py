from responses_generator import ShopCategoriesGenerator, ShopListsGenerator, ProductListsGenerator

import argparse


def generate_responses_for_fixture_set(output_folder, fixtures_folder, fixture_set):

    generator = ShopListsGenerator(fixtures_folder, output_folder, fixture_set)
    generator.generate()

    generator = ShopCategoriesGenerator(
        fixtures_folder, output_folder, fixture_set)
    generator.generate()

    # generator = ProductListsGenerator(fixtures_folder, output_folder, fixture_set)
    # generator.generate()


def main(output_folder, fixtures_folder, fixtures_set):
    if fixtures_set == 'all':
        for set in 'tiny', 'small', 'medium', 'large':
            generate_responses_for_fixture_set(
                output_folder, fixtures_folder, set)
    else:
        generate_responses_for_fixture_set(
            output_folder, fixtures_folder, fixtures_set)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate the JSON expected responses to the GraphQL queries tested in the tests.')
    parser.add_argument('-o', '--output-folder', type=str, default='responses',
                        help='Folder where to output the JSON files')
    parser.add_argument('-i', '--fixtures-folder', type=str, default='./fixtures',
                        help='Folder containing the input json fixtures')
    parser.add_argument('--fixtures-set', type=str, default='all',
                        help='Fixtures set: tiny, small, medium, large, or all')
    args = parser.parse_args()

    main(args.output_folder, args.fixtures_folder, args.fixtures_set)
