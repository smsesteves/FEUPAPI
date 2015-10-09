from bs4 import BeautifulSoup
from urllib.request import urlopen
import warnings

# Folder where resources are read from and wrote to
RES_PATH = "../res/"

# Course's class identifier ! DEPRECATED ! Was used by cleanup_courses_classes()
COURSES_MI_CLASS_ID = ["EIC", "EEC", "EBE", "EC", "EA", "EIG", "EM", "EMM", "EQ"]
# Course's names and identifier
COURSES_MI_NAME_ID = {
                      "MIEIC": 2496, "MIEEC": 2639, "MIB": 2475,
                      "MIEC": 2480, "MIEA": 2922, "MIEIG": 2678,
                      "MIEM": 2484, "MIEMM": 2479, "MIEQ": 2708
                     }

# URL's used to obtain the classes of a given course.
# Accepts course_id, year and course_type (only "MI" is complete on the current version)
BASE_URL = "https://sigarra.up.pt/feup/pt/cur_geral.cur_planos_estudos_view?"
COURSE_ID_URL = "pv_plano_id="
COURSE_YEAR_URL = "&pv_ano_lectivo="
COURSE_TYPE_URL = "&pv_tipo_cur_sigla="
COURSE_ORIGIN_URL = "&pv_origem=CUR"


# Removes all 'None' values from a given list
def remove_null_values(l):
    return [x for x in l if x is not None]


# Remove all duplicate values from a list while keeping the order of the elements
def remove_list_duplicates(l):
    seen = set()
    result = []

    for item in l:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


# Removes the "trash" data collecting when scrapping the whole page ! DEPRECATED !
def cleanup_courses_classes(l):
    warnings.warn(
        "Warning! This function is deprecated and shouldn't be used anymore!",
        DeprecationWarning
    )

    end_index = len(l)

    for course_id in COURSES_MI_CLASS_ID:
        for index, string in enumerate(l):
            if course_id in string and index < end_index:
                    end_index = index

    return l[:end_index]


# Gets the classes of a given course
def get_course_classes(course_id, course_year, course_type):
    final_url = BASE_URL + \
                COURSE_ID_URL + str(course_id) + \
                COURSE_YEAR_URL + str(course_year) + \
                COURSE_TYPE_URL + course_type + \
                COURSE_ORIGIN_URL

    html = urlopen(final_url).read()
    soup = BeautifulSoup(html, "lxml")
    soup = soup.find(id="anos_curr_div")
    data = soup.find_all("td", "t")
    table_data = [course.string for course in data]

    return remove_null_values(remove_list_duplicates(table_data))


# Writes the classes of a course to a file
def write_classes_to_file(classes, course_name):
    with open(RES_PATH + course_name + "_CLASSES" + ".txt", "w") as output_file:
        for course in classes:
            print(course, file=output_file)


# For loop, used for testing purposes
# Gets all the classes for all the 'MI' type courses
for course_mi_name, course_mi_id in COURSES_MI_NAME_ID.items():
    course_classes = get_course_classes(course_mi_id, 2015, "MI")
    # cleanup_courses_classes(get_course_classes(course_mi_id, 2015, "MI")) ! DEPRECATED !
    write_classes_to_file(course_classes, course_mi_name)
