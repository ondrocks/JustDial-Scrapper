from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.justdial.com/Indore/Fine-Dining-Restaurants-(Rs-1000-To-Rs-2000)?t=bktbl")
# abc=driver.find_element_by_class_name("contact-info ").click()
dict1 = {"acb":0,"yz":1,"wx":2,"vu":3,"ts":4,"rq":5,"po":6,"nm":7,"lk":8,"ji":9,"dc":"+","hg":")","fe":"(","ba":"-"}
for key,val in dict1.items():
    print (key,"=",val)

list1=[]
abc=driver.find_element_by_class_name("contact-info ").find_elements_by_class_name("mobilesv")
for abc1 in abc:
    clsname = abc1.get_attribute("class").split("-")[1]
    print(dict1[clsname])