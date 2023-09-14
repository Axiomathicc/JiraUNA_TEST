Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
... 
... # Set your Jira API URL, username, and password
... JIRA_URL = "https://your-jira-instance.atlassian.net/rest/api/3"
... USERNAME = "your-username"
... PASSWORD = "your-password"
... 
... # Define the roles to check and the role to remove
... roles_to_check = ["role1", "role2", "role3"]
... role_to_remove = "unassigned"
... 
... # Function to get user's roles
... def get_user_roles(username):
...     url = f"{JIRA_URL}/user?username={username}"
...     response = requests.get(url, auth=(USERNAME, PASSWORD))
...     response.raise_for_status()
...     return response.json()["groups"]["items"]
... 
... # Function to remove a role from a user
... def remove_role_from_user(username, role):
...     url = f"{JIRA_URL}/user?username={username}"
...     data = {"groups": {"remove": [role]}}
...     response = requests.put(url, json=data, auth=(USERNAME, PASSWORD))
...     response.raise_for_status()
... 
... # Get all users with the unassigned role
... url = f"{JIRA_URL}/group/member?groupname={role_to_remove}"
... response = requests.get(url, auth=(USERNAME, PASSWORD))
... response.raise_for_status()
... unassigned_users = response.json()["values"]
... 
... # Iterate through unassigned users
... for user in unassigned_users:
...     username = user["name"]
...     user_roles = get_user_roles(username)
... 
...     # Check if user has all the specified roles
    has_all_roles = all(role in user_roles for role in roles_to_check)

    if has_all_roles:
        print(f"{username} has all the specified roles.")
        print(f"Removing {role_to_remove} from {username}.")
        remove_role_from_user(username, role_to_remove)
        print(f"{role_to_remove} removed successfully.")
    else:
        print(f"{username} does not have all the specified roles.")
