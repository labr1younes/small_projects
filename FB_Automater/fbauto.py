import os
import requests
from dotenv import load_dotenv
import mysql.connector


def filtr(responsejson):
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
        shoer_description = result.get("shoer_description", None)
        # store = result.get("store", None)
        subcategory = result.get("subcategory", None)
        # subcatslug = result.get("subcatslug", None)
        typee = result.get("type", None)
        urll = result.get("url", None)

        if language not in ["English", "Arabic"]:
            continue
        else:
            print("category = ", category)
            # print("catslug = ", catslug)
            # print("date = ", date)
            # print("id = ", idd)
            print("image = ", image)
            # print("isexpired = ", isexpired)
            print("language = ", language)
            print("name = ", result["name"])
            print("shoer_description = ", shoer_description)
            # print("store = ", store)
            print("subcategory = ", subcategory)
            # print("subcatslug = ", subcatslug)
            print("type = ", typee)
            print("url = ", urll)
            print("---------------------------------------------")


if __name__ == "__main__":
    load_dotenv()
    url = os.getenv('URL')

    print("Hello world! \n")

    response = requests.get(url)
    print(len(response.json()["results"]))
    filtr(response.json())

    mydb = mysql.connector.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE')
    )

    print(mydb)
