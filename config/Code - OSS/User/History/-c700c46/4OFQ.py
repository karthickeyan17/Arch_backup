from leetcode import Leetcode

# Initialize Leetcode API
leetcode_api = Leetcode()

# Retrieve user data
user_data = leetcode_api.get_user("your_username")

# Print user profile
print(user_data)
