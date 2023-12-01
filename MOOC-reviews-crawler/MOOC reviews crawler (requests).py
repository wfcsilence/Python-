import requests
import json
import pandas as pd
import xlsxwriter
import time
import random


def fetch_course_reviews(page_index=1, page_size=20, order_by=3):
    url = "https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=31d1b4e657394457be14484af0bcf6b2"

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'NTESSTUDYSI=31d1b4e657394457be14484af0bcf6b2; EDUWEBDEVICE=167d5fa18df84427a83034448b27dd87; utm=eyJjIjoic2hhcmUiLCJjdCI6IiIsImkiOiIiLCJtIjoiaXBob25lU2hhcmUiLCJzIjoid2VpeGluIiwidCI6IiJ9|; hb_MA-A976-948FFA05E931_u=%7B%22utm_source%22%3A%20%22weixin%22%2C%22utm_medium%22%3A%20%22iphoneShare%22%2C%22utm_campaign%22%3A%20%22share%22%2C%22utm_content%22%3A%20%22%22%2C%22utm_term%22%3A%20%22%22%2C%22promotional_id%22%3A%20%22%22%7D; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1700724006; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1700724006; WM_NI=E2%2Bj8oWkGYqlfAGaVGrkWQpc7%2FhxqxNUcn6sjdx0TShxfgrkegs7USeCM765gtTZV4Ox7KplibiSr0%2BmjjGqEQrFfciEpyEQ19INpqwa8ytvp6%2B68kIySiJGd1qgHDp2Rlc%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb3ca3e8599f8d2ee6389bc8ba3c84e939b9eb1c862e9abb991d65eb0aff9a5dc2af0fea7c3b92a87eee58bbb6595b589baf468a69f8982d54db2b599b2f369f5f1a899f4748e8bad8fb579aabcb8d1d759aca8aa88f161a7b9bdd8d859a79d83d8b53fa5ac9cbbd5408da8f9acf368abbea7b4f13ce9b3a68bc67b878fbea7e569ab9bc09ac85bf3e787aff37bb5bff89af77eb4eae5d7bb618ba79d8ac94da8efbf88cb50b4ee9e8de237e2a3; WM_TID=F%2BYuuUBA0NVFUBRVVVfB3v%2B04WRlr7WJ; __yadk_uid=iISBoHTb9eXJfv14zkIC8KTRtsAtnlbq',
        'Dnt': '1',
        'Origin': 'https://www.icourse163.org',
        'Referer': 'https://www.icourse163.org/course/BIT-268001',
        'Sec-Ch-Ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    # 使用上面定义的headers
    response = requests.post(url, headers=headers, data={
        'pageIndex': page_index,
        'pageSize': page_size,
        'orderBy': order_by,
        'courseId': 268001
    })

    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print("Error:", response.status_code)
        return None


def get_total_pages(page_size=20):
    first_page_data = fetch_course_reviews(page_size=page_size)
    if first_page_data:
        return first_page_data['result']['query']['totlePageCount']
    else:
        print("Failed to fetch the first page data")
        return 0


def fetch_all_reviews_to_excel(filename='course_reviews.xlsx'):
    total_pages = get_total_pages()
    all_reviews = []

    for page in range(1, total_pages + 1):
        reviews = fetch_course_reviews(page_index=page)
        if reviews:
            for review in reviews['result']['list']:
                review_data = {
                    'Page': page,
                    'User Nickname': review['userNickName'],
                    'Content': review['content'],
                    'Mark': review['mark'],
                    'Agree Count': review['agreeCount']
                    #无法获取发布时间
                    #第n次课程需要转换数字
                }
                all_reviews.append(review_data)

        print(f"Processed page {page}/{total_pages}")

        # 随机休息200ms到2000ms
        # time.sleep(random.uniform(2, 4.0))

    # Save to Excel
    df = pd.DataFrame(all_reviews)
    df.to_excel(filename, engine='xlsxwriter')
    print(f"Saved all reviews to {filename}")


if __name__ == '__main__':
    fetch_all_reviews_to_excel()
