from graphql.responses_generator import *

import argparse


def generate_responses_for_fixture_set(output_folder, fixtures_folder):

    generator = ShopListsGenerator(fixtures_folder, output_folder)
    generator.generate()

    generator = ShopsGenerator(fixtures_folder, output_folder)
    generator.generate()

    generator = ShopCategoriesGenerator(fixtures_folder, output_folder)
    generator.generate()

    generator = ProductListsGenerator(fixtures_folder, output_folder)
    generator.generate()


def main(output_folder, fixtures_folder):
    generate_responses_for_fixture_set(output_folder, fixtures_folder)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate the JSON expected responses to the GraphQL queries tested in the tests.')
    parser.add_argument('-o', '--output-folder', type=str, default='responses',
                        help='Folder where to output the JSON files')
    parser.add_argument('-i', '--fixtures-folder', type=str, default='./fixtures',
                        help='Folder containing the input json fixtures')
    args = parser.parse_args()

    main(args.output_folder, args.fixtures_folder)