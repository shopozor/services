import os.path

from behave import fixture
from behave.fixture import use_composite_fixture_with, fixture_call_params

import settings


@fixture
def unknown(context):
    user_data = {
        "email": "new_consumer@shopozor.ch",
        "is_active": false,
        "is_staff": false,
        "is_superuser": false
    }
    return user_data


@fixture
def inactive_customer(context):
    user_data = {
        "email": "inactive_consumer@budzons.ch",
        # TODO: get user id from existing fixtures
        "id": 100,
        "isActive": false,
        "isStaff": false,
        "isSuperUser": false
    }
    context.inactive_customer = user_data
    return user_data


@fixture
def consumer(context):
    user_data = json.load(
        os.path.join(settings.json_fixtures_dir(context), 'Users', 'consumers.json'))[0]
    context.consumer = user_data
    return user_data


@fixture
def producer(context):
    user_data = json.load(
        os.path.join(settings.json_fixtures_dir(context), 'Users', 'producers.json'))[0]
    context.producer = user_data
    return user_data


@fixture
def manager(context):
    user_data = json.load(
        os.path.join(settings.json_fixtures_dir(context), 'Users', 'managers.json'))[0]
    context.manager = user_data
    return user_data


@fixture
def rex(context):
    user_data = json.load(
        os.path.join(settings.json_fixtures_dir(context), 'Users', 'rex.json'))[0]
    context.rex = user_data
    return user_data


@fixture
def softozor(context):
    user_data = json.load(
        os.path.join(settings.json_fixtures_dir(context), 'Users', 'softozor.json'))[0]
    context.softozor = user_data
    return user_data


@fixture
def wrong_credentials_response(context):
    data = json.load(
        os.path.join(settings.GRAPHQL_RESPONSES_DIR, 'Authentication', 'Login', 'WrongCredentials.json'))
    context.wrong_credentials_response = data
    return data


@fixture
def failed_query_response(context):
    data = json.load(
        os.path.join(settings.GRAPHQL_RESPONSES_DIR, 'Authentication', 'Logout', 'QueryResponseAfterLogout.json'))
    context.failed_query_response = data
    return data


@fixture
def successful_logout_response(context):
    data = json.load(
        os.path.join(settings.GRAPHQL_RESPONSES_DIR, 'Authentication', 'Logout', 'Success.json'))
    context.successful_logout_response = data
    return data


@fixture
def successful_signup(context):
    data = json.load(
        os.path.join(settings.GRAPHQL_RESPONSES_DIR, 'Authentication', 'RegisterConsumer', 'SuccessfulConsumerCreation.json'))
    context.successful_signup = data
    return data


@fixture
def successful_account_confirmation(context):
    data = json.load(
        os.path.join(settings.GRAPHQL_RESPONSES_DIR, 'Authentication', 'RegisterConsumer', 'SuccessfulAccountConfirmation.json'))
    context.successful_account_confirmation = data
    return data


@fixture
def successful_password_reset(context):
    data = json.load(os.path.join(
        settings.GRAPHQL_RESPONSES_DIR, 'Authentication', 'ResetUserPassword', 'SuccessfulPasswordReset.json'))
    context.successful_password_reset = data
    return data


@fixture
def successful_set_password(context):
    data = json.load(
        os.path.join(settings.GRAPHQL_RESPONSES_DIR, 'Authentication', 'ResetUserPassword', 'SuccessfulSetPassword.json'))
    context.successful_set_password = data
    return data


@fixture
def signup_password_not_compliant(context):
    data = json.load(
        os.path.join(settings.GRAPHQL_RESPONSES_DIR, 'Authentication', 'SignupPasswordNotCompliant.json'))
    password_not_compliant = data['data']['consumerCreate']['errors'][0]
    context.password_not_compliant = password_not_compliant
    return password_not_compliant


@fixture
def password_reset_password_not_compliant(context):
    data = json.load(
        os.path.join(settings.GRAPHQL_RESPONSES_DIR, 'Authentication', 'PasswordResetPasswordNotCompliant.json'))
    password_not_compliant = data['data']['setPassword']['errors'][0]
    context.password_not_compliant = password_not_compliant
    return password_not_compliant


@fixture
def signup_expired_link(context):
    data = json.load(
        os.path.join(settings.GRAPHQL_RESPONSES_DIR, 'Authentication', 'SignupExpiredLink.json'))
    expired_link = data['data']['consumerActivate']
    context.expired_link = expired_link
    return expired_link


@fixture
def password_reset_expired_link(context):
    data = json.load(
        os.path.join(settings.GRAPHQL_RESPONSES_DIR, 'Authentication', 'PasswordResetExpiredLink.json'))
    expired_link = data['data']['setPassword']
    context.expired_link = expired_link
    return expired_link


@fixture
def login(context):
    return use_composite_fixture_with(
        context, [
            fixture_call_params(unknown),
            fixture_call_params(wrong_credentials_response)
        ]
    )


@fixture
def signup(context):
    return use_composite_fixture_with(
        context, [
            fixture_call_params(unknown),
            fixture_call_params(successful_signup),
            fixture_call_params(signup_expired_link),
            fixture_call_params(successful_account_confirmation),
            fixture_call_params(signup_password_not_compliant)
        ]
    )


@fixture
def password_reset(context):
    return use_composite_fixture_with(
        context, [
            fixture_call_params(unknown),
            fixture_call_params(successful_set_password),
            fixture_call_params(password_reset_password_not_compliant),
            fixture_call_params(password_reset_expired_link),
            fixture_call_params(successful_password_reset)
        ]
    )


@fixture
def expected_shop_list(context):
    shop_list = json.load(
        os.path.join(settings.graphql_responses_dir(context), 'Consumer', 'Shops.json'))
    context.expected_shop_list = shop_list
    return shop_list


@fixture
def expected_shop_catalogues(context):
    catalogues_folder = os.path.join(
        settings.graphql_responses_dir(context), 'Consumer', 'Catalogues')
    shops = [shop for shop in os.listdir(catalogues_folder) if os.path.isdir(
        os.path.join(catalogues_folder, shop))]
    shop_catalogues = {}
    for shop in shops:
        shop_id = int(shop.split('-')[1])
        shop_dir = os.path.join(catalogues_folder, shop)
        categories = [category for category in os.listdir(
            shop_dir) if os.path.isfile(os.path.join(shop_dir, category))]
        shop_catalogues[shop_id] = {}
        for category in categories:
            category_id = int(category.split('.')[0].split('-')[1])
            shop_catalogues[shop_id][category_id] = json.load(os.path.join(
                catalogues_folder, shop, category))
    context.expected_shop_catalogues = shop_catalogues
    return shop_catalogues


@fixture
def expected_shop_categories(context):
    categories = json.load(os.path.join(
        settings.graphql_responses_dir(context), 'Consumer', 'Categories.json'))
    context.expected_categories = categories
    return categories


@fixture
def expected_product_details(context):
    products_folder = os.path.join(
        settings.graphql_responses_dir(context), 'Consumer', 'Products')
    product_details_filenames = [item for item in os.listdir(products_folder) if os.path.isfile(
        os.path.join(products_folder, item))]
    product_details = {}
    for filename in product_details_filenames:
        product_id = int(filename.split('.')[0].split('-')[1])
        product_details[product_id] = json.load(os.path.join(
            products_folder, filename))
    context.expected_product_details = product_details
    return product_details


@fixture
def shops_fixtures(context):
    return use_composite_fixture_with(
        context, [
            fixture_call_params(expected_shop_list),
            fixture_call_params(expected_shop_catalogues),
            fixture_call_params(expected_shop_categories),
            fixture_call_params(expected_product_details)
        ]
    )
