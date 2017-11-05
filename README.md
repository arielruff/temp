# City Complaints - Web App by: Ariel
This is a project which users can uses in order to document complaints in their city.

## About:
City Complaints is a RESTful web app which uses Flask as its underlying framework. This app also depends on OAuth in order to enable it's user system. For it's database communication, this app utilizes sqlalchemy.

## Dependencies:
- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## Installation:
1. Install Vagrant & VirtualBox
2. Clone the Udacity Vagrantfile
3. Copy the 'complaints' folder from this app to your vagrant folder.
4. Inside the cloned directory, run Vagrant with: `vagrant up`
5. Open an ssh connection to Vagrant: `vagrant ssh`
6. Navigate to root '/' then: `cd/vagrant`
7. Create the needed database: `python /complaints/make_database.py`
8. Populate the database: `python /complaints/fill_database.py`
9. Run the application: `python /complaints/app.py`
10. Browse to: http://localhost:8000

## Add Support for Google Login

1. Go to [Google Dev Console](https://console.developers.google.com)
2. Sign up or Login if prompted
3. Go to Credentials
4. Select Create Crendentials > OAuth Client ID
5. Select Web application
6. Enter the name 'Complaint-App'
7. Authorized JavaScript origins = 'http://localhost:8000'
8. Authorized redirect URIs = 'http://localhost:8000/login' && 'http://localhost:8000/gconnect'
9. Select Create
10. Copy the Client ID and paste it into the `data-clientid` in login.html (THERE IS NONE INCLUDED IN FOR SAFTEY)
11. On the Dev Console Select Download JSON
12. Rename JSON file to client_secrets.json
13. Place JSON file in item-complaints directory (THERE IS NONE INCLUDED IN FOR SAFTEY)
14. Run application using `python /complaints/application.py`

## JSON Endpoints
complaints JSON: `/complaints/JSON`
    - Displays the whole complaints. Categories and all items.

Categories JSON: `/complaints/categories/JSON`
    - Displays all categories

Category Items JSON: `/complaints/<path:category_name>/items/JSON`
    - Displays items for a specific category

Category Item JSON: `/complaints/<path:category_name>/<path:item_name>/JSON`
    - Displays a specific category item.
