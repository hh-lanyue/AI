from bs4 import BeautifulSoup


# 读取HTML文件
def analy_html_file(file_path):
    file_html = open(file_path, 'r', encoding='utf8')
    contents = file_html.read()
    soup = BeautifulSoup(contents, 'html.parser')
    info = soup.find('script')
    # print(info.text)
    data_list = soup.findAll('script', {'xml:space': 'preserve'})
    for item in data_list:
        key = 'ticketInfoForPassengerForm'
        if key in item.text:
            print(item.text)