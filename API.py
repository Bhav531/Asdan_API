import requests

course_id = input("Enter Course ID: ")
url = f"http://www.asdan-computing.org.uk/courses/info/{course_id}"
params = {
    "format": "json"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("Course ID:", data["id"])
    print("Course Name:", data["course_name"])
    print("Description:", data["course_description"])
    print("Administrator:",
          data["administrator_first_name"],
          data["administrator_last_name"])
    print("Start Date:", data["start_date"])
    print("End Date:", data["end_date"])
    print("Active:", data["is_active"])
else:
    print("Failed to retrieve course information")
