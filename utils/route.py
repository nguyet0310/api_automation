from email.mime import base


class Route:
    base_url = "https://reqres.in/api/"
    # Get user
    user_url = base_url + "users"
    get_users_by_page_url = user_url + "?page="
    register_url = base_url + "register"
    delete_url = user_url + "/2"
