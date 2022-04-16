
class Menus:
    login_menu = {
        "title": "LOGIN MENU",
        1: "Login as Existing User.",
        2: "Create new Account.",
        3: "Exit"
    }

    main_menu = {"title": "MAIN MENU",
                 1: "Retrieve Credentials",
                 2: "Update Credentials",
                 3: "Add New Host",
                 4: "Manage Hosts",
                 5: "Manage Platforms",
                 6: "Manage Categories",
                 7: "Exit"
                 }

    retrieve_credentials_menu = {"title": "RETRIEVE CREDENTIALS MENU",
                                1: "Show by Host Platform",
                                2: "Show by Host Category",
                                3: "Show by Host Address",
                                4: "Show by Host Name",
                                5: "Show all Hosts",
                                6: "Retrieve by Host Id",
                                7: "Return"
                                }

    host_menu = {"title": "MANAGE HOSTS MENU",
                 1: "Add Host",
                 2: "Remove Platform",
                 3: "Update Platform",
                 7: "Show Platforms",
                 9: "Return"
                 }

    platform_menu = {"title": "MANAGE PLATFORMS MENU",
                     1: "Add Platform",
                     2: "Remove Platform",
                     3: "Update Platform",
                     4: "Show Platforms",
                     5: "Return"
                     }

    category_menu = {"title": "MANAGE CATEGORIES MENU",
                     1: "Add Category",
                     2: "Remove Category",
                     3: "Update Category",
                     4: "Show Categories",
                     5: "Return"
                     }
