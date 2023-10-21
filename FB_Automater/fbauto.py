import os
import requests
from dotenv import load_dotenv
import mysql.connector


def filtr(responsejson):
    filtred_data = []
    for result in responsejson["results"]:
        if result["type"] == "Affiliate":
            continue

        tmp_result = []

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
        typee = result.get("type", None)
        urll = result.get("url", None)

        if language not in ["English", "Arabic"]:
            continue
        else:
            tmp_result = [category, image, language, name, shoer_description, subcategory, typee, urll]
            print("--------------------------------------------- ADDED")
        filtred_data.append(tmp_result)
    return filtred_data


def print_data(data):
    for cours in data:
        print("category = ", cours[0])
        print("image = ", cours[1])
        print("language = ", cours[2])
        print("name = ", cours[3])
        print("shoer_description = ", cours[4])
        print("subcategory = ", cours[5])
        print("type = ", cours[6])
        print("url = ", cours[7])
        print("---------------------------------------------")
    print("--- Done ---")


if __name__ == "__main__":
    load_dotenv()
    url = os.getenv('URL')

    response = requests.get(url)
    print(len(response.json()["results"]))
    tmpdata = filtr(response.json())
    print_data(tmpdata)

    mydb = mysql.connector.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE')
    )

    print(mydb)
