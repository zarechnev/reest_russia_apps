def main():
    from bs4 import BeautifulSoup
    import requests

    with open("out.txt", 'w') as file:
        for page in range(1, 31):
            url = "https://reestr.minsvyaz.ru/reestr/?sort_by=date&sort=asc&sort_by=date&sort=asc&class=&name=%D0%B3%D1%80%D0%B0%D1%84&owner_status=&owner_name=&PAGEN_1={}&class%5B%5D=54131&name=&owner_status=&owner_name=&set_filter=Y".format(page)
            raw_reest_site = requests.get(url, verify="")
            reest_site = BeautifulSoup(raw_reest_site.content, features="html.parser")
            mydivs = reest_site.findAll("div", {"class": "name"}, "a")
            file.write(str(mydivs))


if __name__ == "__main__":
    main()
