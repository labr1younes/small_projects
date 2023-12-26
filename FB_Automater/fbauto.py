import json
import os
import requests
from dotenv import load_dotenv
import mysql.connector


def filtr(responsejson):
    # This function is for filtering the courses we got in results
    filtred_data = []
    for result in responsejson["results"]:
        if result["type"] == "Affiliate":
            continue

        category = result.get("category", None)
        # catslug = result.get("catslug", None)
        # date = result.get("date", None)
        # idd = result.get("id", None)
        image = result.get("image", None)
        # isexpired = result.get("isexpired", None)
        language = result.get("language", None)
        name = result.get("name", None)
        shoer_description = result.get("shoer_description", None)
        # store = result.get("store", None)
        subcategory = result.get("subcategory", None)
        # subcatslug = result.get("subcatslug", None)
        # typee = result.get("type", None)
        urll = result.get("url", None)
        sale_start = result.get("sale_start", None)

        if language not in ["English", "Arabic"]:
            continue
        else:
            tmp_result = [category, image, language, name, shoer_description, subcategory, urll, sale_start]
            # print("--------------------------------------------- ADDED")
        filtred_data.append(tmp_result)
    return filtred_data


def print_data(data):
    # This function is for showing the course information
    for cours in data:
        print("category = ", cours[0])
        print("image = ", cours[1])
        print("language = ", cours[2])
        print("name = ", cours[3])
        print("shoer_description = ", cours[4])
        print("subcategory = ", cours[5])
        print("url = ", cours[6])
        print("sale_start = ", cours[7])
        print("--------------------------------------------")
    print("---- Done Printing courses informations ----")


def add_data_2_db(mysqlconnector, _data):
    # This function is for adding courses to the database
    sql_insert = "INSERT INTO udemy_cpns (category,image,language,name,description,subcategory,courseurl,sale_start) " \
                 "VALUES (%s, %s,%s, %s,%s, %s,%s,%s)"
    mycursor = mysqlconnector.cursor(buffered=True)
    for course in _data:
        if iscourseindb(mycursor, course):
            continue

        val = (course[0], course[1], course[2], course[3], course[4], course[5], course[6], course[7])
        mycursor.execute(sql_insert, val)
        mysqlconnector.commit()

    # print(mycursor.fetchall())
    mysqlconnector.commit()


def get_data_from_db(mysqlconnector):
    # This function is for getting courses to the database
    sql_select = "SELECT * FROM botdb.udemy_cpns where isposted = 0 "
    cursor = mysqlconnector.cursor(buffered=True)

    cursor.execute(sql_select)
    mysqlconnector.commit()

    result = cursor.fetchall()
    print(result)
    return result


def iscourseindb(cursor, course):
    # This function is for checking if the course in our database already
    sql_select = "SELECT * FROM udemy_cpns WHERE courseurl = %s "

    val = (course[6],)
    cursor.execute(sql_select, val)
    # myresult = mycursor.fetchall()

    if cursor.rowcount > 0:
        print("we already have : ", course[3])
        return True

    return False


def database_cnc():
    db = mysql.connector.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE')
    )
    return db


def main():
    # This is the main function
    url = os.getenv('URL')
    mycnc = database_cnc()
    # mycursor = mydb.cursor()

    response = requests.get(url)
    print(len(response.json()["results"]))
    courses = filtr(response.json())
    # print_data(courses)

    # add_data_2_db(mydb, courses)
    get_data_from_db(mycnc)


def add_fb_post():
    # This function is for adding one post to the page
    pageid = os.getenv('PAGEID')
    token = os.getenv('ACCESS_TOKEN')

    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "message": "this is the 3nd post ",
        # "link": link,
        "url": "https://img-c.udemycdn.com/course/750x422/5081398_e792_5.jpg",
        "published": "true",
        # "scheduled_publish_time": scheduled_publish_time
    }
    response = requests.post(
        f"https://graph.facebook.com/v18.0/{pageid}/photos?access_token={token}",
        headers=headers,
        data=json.dumps(data)
    )

    # Check the response status code.
    if response.status_code == 200:
        print("Post published successfully!")
    else:
        print("Error publishing post:", response.status_code)


if __name__ == "__main__":
    load_dotenv()
    # add_fb_post()
    main()
