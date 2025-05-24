# Fixed Global variable issues

#### Time: 2 hrs

#### We had an issue where we had a global database connection and cursor (conn and cur) in the Flask app. While the recipe insert used a fresh connection (which worked), the /recipes/ page reused the old, global cursor to fetch data. Because database cursors can cache results or become stale across requests, this caused the newly inserted recipes to not appear when returning to the recipes page. The fix was to create a new database connection and cursor inside the /recipes/ route each time it is accessed, ensuring that the data fetched is always fresh and up to date.

![image](https://github.com/user-attachments/assets/8316f154-e681-4e1a-b1e8-b5ebcda3fb2b)
