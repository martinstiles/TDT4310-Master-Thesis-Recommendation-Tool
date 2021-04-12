""" Main file for data scraping. Will save ... (?) """

from soup import initiate_webdriver, get_soup
from utils import remove_first_word_in_string, remove_last_word_in_string
from pathlib import Path

BASE_URL = 'https://www.idi.ntnu.no/education/masteroppgaver.php?s=2'


def get_ids_and_labels_for_specializations(soup):
    """
    Retrieves the ID of every checkbox (input), which will be used to manipulate
    the URL, as well the label for the specialization (e.g. "Databaser og søk")

    Args:
        soup: BS4 soup

    Returns:
        ids_and_labels: list of tuples containing ID and label for each specialization
    """

    ids_and_labels = []
    trs = soup.find_all("tr")
    for tr in trs:
        tds = tr.find_all("td")
        for td in tds:
            inputs = td.find_all("input")
            labels = td.find_all("label")
            # Last word is the count, thus it is removed:
            label_texts = [remove_last_word_in_string(label.text)
                           for label in labels]
            input_ids = [inp["id"] for inp in inputs]
            ids_and_labels += zip(input_ids, label_texts)

    return ids_and_labels


def get_thesis_title(thesis):
    title = thesis.find("h3").text
    # TODO: Make decision: Remove marking or not? (e.g. [NorwAi])
    if title[0] == "[":
        title = remove_first_word_in_string(title)

    return title


def get_thesis_description(thesis):
    # TODO: Get the full description (this is only the first part)
    desc = thesis.find("p").text
    return desc


def get_thesis_lecturer(thesis):
    bottom_box = thesis.find("div", class_="status")
    anchors = bottom_box.find_all("a")
    lecturer = anchors[0].text
    return lecturer


def get_thesis_assigned_status(thesis):
    bottom_box = thesis.find("div", class_="status")
    assigned_status = bottom_box.find("i").text
    return assigned_status


def get_thesis_url(thesis):
    bottom_box = thesis.find("div", class_="status")
    anchors = bottom_box.find_all("a")
    url = "https://www.idi.ntnu.no/education/" + anchors[1]["href"]
    return url


def main():
    driver = initiate_webdriver()
    soup = get_soup(BASE_URL, driver)
    ids_and_labels = get_ids_and_labels_for_specializations(soup)

    for id, label in ids_and_labels:
        spec_url = BASE_URL + "&" + id + "=1"
        spec_soup = get_soup(spec_url, driver)
        thesises = spec_soup.find_all("div", class_="oppgave")

        for thesis in thesises:
            title = get_thesis_title(thesis)
            description = get_thesis_description(thesis)
            lecturer = get_thesis_lecturer(thesis)
            status = get_thesis_assigned_status(thesis)
            url = get_thesis_url(thesis)
            # TODO: Perform save (to file or DB) -> In batches maybe?

            with open(Path(__file__).parent / "data.txt", "a") as file:
                file.write(" | ".join([
                    title,
                    description,
                    lecturer,
                    status,
                    url
                ]) + "\n")
            # return
        break


if __name__ == "__main__":
    # # Clear data file:
    # with open(Path(__file__).parent / "data.txt", "w") as file:
    #     file.write("")

    main()

    # with open(Path(__file__).parent / "data.txt", "r") as file:
    #     for line in file.readlines():
    #         print(line.split(" | "))
