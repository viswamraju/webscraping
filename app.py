from lxml import etree


def get_html_content():
    tree = etree.parse('fundamentals/src/web_page.html')
    print(etree.tostring(tree))


def find_element():
    tree = etree.parse("fundamentals/src/web_page.html")
    print(tree.find("head/title").text)

def find_p1_body():
    tree = etree.parse("fundamentals/src/web_page.html")
    print(tree.find('body/p').text)

def find_all_elements():
    tree = etree.parse("fundamentals/src/web_page.html")
    elements = tree.findall('body/ul/li')
    for element in elements:
        a = element.find("a")
        if a is not None:
            print(f"{element.text}, {a.text}")
        else:
            print(f"{element.text}")

"""
Find elements always with full absolute path is not good if we have deep dom structure.
To overcome that we have xpath. xpath always gives elements in the form of list

"""

def find_elements_using_xpath():
    tree = etree.parse("fundamentals/src/web_page.html")
    elements = tree.xpath('//title')
    # print(elements)
    # print(dir(elements[0]))
    print(elements[0].text)
    print(tree.xpath("//title/text()")[0])

def find_p_using_xpath():
    tree = etree.parse("fundamentals/src/web_page.html")
    print(tree.xpath("//body/p/text()")[0])

def li_using_xpath():
    tree = etree.parse("fundamentals/src/web_page.html")
    li_elements = tree.xpath("//li")
    for element in li_elements:
        print(",".join (list(map(str.strip, element.xpath(".//text()")))))


def find_title_css_selector():
    tree = etree.parse("fundamentals/src/web_page.html")
    html = tree.getroot()
    title_element = html.cssselect('li')[0]
    print(title_element.text)
    

# get_html_content()
# find_element()
# find_p1_body()
# find_all_elements()

# find_elements_using_xpath()
# find_p_using_xpath()
# li_using_xpath()
find_title_css_selector()