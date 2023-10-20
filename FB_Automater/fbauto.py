import os
import requests
from dotenv import load_dotenv


def filtr(responsejson):
    for result in responsejson["results"]:
        try:
            if result["language"] not in ["English", "Arabic"]:
                continue
            else:
                print("category = ", result["category"])
                # print("catslug = ", result["catslug"])
                # print("date = ", result["date"])
                print("id = ", result["id"])
                # print("image = ", result["image"])
                # print("isexpired = ", result["isexpired"])
                # print("language = ", result["language"])
                # print("name = ", result["name"])
                # print("shoer_description = ", result["shoer_description"])
                # print("store = ", result["store"])
                # print("subcategory = ", result["subcategory"])
                # print("subcatslug = ", result["subcatslug"])
                # print("type = ", result["type"])
                # print("url = ", result["url"])
                print("---------------------------------------------")
        except Exception as error:
            # handle the exception
            print("An exception occurred:", error)


if __name__ == "__main__":
    load_dotenv()
    url = os.getenv('URL')

    print("Hello world! \n")

    response = requests.get(url)
    print(len(response.json()["results"]))
    filtr(response.json())
