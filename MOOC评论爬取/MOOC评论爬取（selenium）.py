from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
# selenium更新后有新写法，怎么写上网查

if __name__ == '__main__':
    writer = pd.ExcelWriter("./mooc评论.xlsx") #设置保存Excel的路径
    service = Service(executable_path='./chromedriver.exe')#浏览器输入chrome://version/获取当前版本，并找到对应版本的chromedriver
    driver = webdriver.Chrome(service=service) #设置chrome驱动
    url = 'https://www.icourse163.org/course/BIT-268001'  #设置要爬取的课程网页链接
    #["用户",“评分”,"内容","时间","点赞数","第n次课程"] 待爬取的内容
    
    driver.get(url)
    cont = driver.page_source
    soup = BeautifulSoup(cont, 'html.parser')
    ele = driver.find_element(By.ID, "review-tag-button")  # 点击 课程评价
    ele.click()
    xyy = driver.find_element(By.CLASS_NAME, "ux-pager_btn__next")  # 翻页功能
    connt = driver.page_source
    soup = BeautifulSoup(connt, 'html.parser') #得到网页源代码
 
    all_table = [] #保存所需数据
    all_table.append(["用户","评分","内容","时间","点赞数","第n次开课"])
 
    for i in range(500):  # 选择要爬取的页数
        xyy.click()
        connt = driver.page_source
        soup = BeautifulSoup(connt, 'html.parser')
        content = soup.find_all('div', {
            'class': 'ux-mooc-comment-course-comment_comment-list_item_body'})  # 全部评论
 
        for ctt in content:
            #获取用户名
            user_name = ctt.find("a",{"class":"primary-link ux-mooc-comment-course-comment_comment-list_item_body_user-info_name"})
            user_name = user_name.text
            print(user_name)
            
            #获取评分
            user_star=0
            user_astar = ctt.find_all("i",{"class":"star ux-icon-custom-rating-favorite"})
            for i in user_astar:
              user_star+=1
            print(user_star)
 
            #发布时间
            publish_time = ctt.find('div', {'class': 'ux-mooc-comment-course-comment_comment-list_item_body_comment-info_time'})
            publish_time = publish_time.text
            publish_time = publish_time[4:]
            print(publish_time)
 
            #第几次开课
            course_nums = ctt.find('div', {'class': 'ux-mooc-comment-course-comment_comment-list_item_body_comment-info_term-sign'})
            course_nums = course_nums.text
            course_nums = course_nums.replace(" ","")
            course_nums = course_nums.replace("第","")
            course_nums = course_nums.replace("次开课","")
            course_nums = course_nums.replace("\n", "")
            print(course_nums)
 
            scontent = []
            aspan = ctt.find_all('span')
            for span in aspan:
                scontent.append(span.string)
            
            #点赞数
            like = scontent[5]
            
            #课程内容
            scontent = scontent[1]
            print(scontent)
            
            all_table.append([user_name,user_star,scontent,publish_time,like,course_nums])
    
    #保存到Excel
    all_table = pd.DataFrame(all_table)
    all_table.to_excel(writer, index=False)
    writer.save()