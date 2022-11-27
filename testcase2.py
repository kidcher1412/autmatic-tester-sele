from colorama import Fore, Back, Style
from multiprocessing.connection import wait
from selenium import webdriver
import undetected_chromedriver as uc
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import msvcrt as m
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.action_chains import ActionChains


options = uc.ChromeOptions()
pathProfile = '.\\tmp6k358cfx'
options.user_data_dir=pathProfile
driver = uc.Chrome(use_subprocess=True,options=options)
print("===Khởi Chạy Kiểm Thử===")

def check_exists(xpath):
    try:
        driver.find_element(By.CSS_SELECTOR,xpath)
    except NoSuchElementException:
        return False
    return True
def wait():
    m.getch()
def gohome():
    myElem = myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'logo'))).click()
driver.get("https://doantesting.netlify.app/")
myElem = myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'nav')))
checker = False
def closeModel():
    if(check_exists(".close-modal-login")):
        myElem = myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'close-modal-login'))).click()
def login(us,pw):
    global demTestcaseDangNhap
    driver.get("https://doantesting.netlify.app/")
    myElem = myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'login'))).click()
    time.sleep(0.6)
    myElem = myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'LogIn-email'))).send_keys(us)
    time.sleep(0.6)
    myElem = myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'LogIn-pass'))).send_keys(pw)
    time.sleep(0.6)
    myElem = myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-login'))).click()
    time.sleep(1.5)

    try:
        alert = WebDriverWait(driver, 2).until(EC.alert_is_present())
        testTextAlert = alert.text
        alert.accept()
    except TimeoutException:
        print(Fore.RED+"TestCase Đăng Nhập Tài Khoản Thất Bại")
        return
    if(testTextAlert == 'Tài khoản không tồn tại'):
        print(Fore.RED+"TestCase Đăng Nhập Tài Khoản Thất Bại")
    else:
        demTestcaseDangNhap =demTestcaseDangNhap+1
        print(Fore.GREEN+"TestCase Đăng Nhập Tài Khoản Thành Công"+Fore.RESET)
    # try:
    #     if(check_exists(".close-modal-login")):
    #         myElem = myElem = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, 'close-modal-login'))).click()
    # except TimeoutException:
    #     pass
    # try:
    #     alert = WebDriverWait(driver, 2).until(EC.alert_is_present())
    #     testTextAlert = alert.text
    #     alert.accept()
    # except TimeoutException:
    #     pass
    # gohome()
def sigin(us,em,pw):
    global demTestcaseDangKi
    driver.get("https://doantesting.netlify.app/")
    myElem = myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'bx-user'))).click()
    time.sleep(0.5)
    myElem = myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'Register'))).click()
    time.sleep(0.5)
    myElem = myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'RegisterForm-name'))).send_keys(us)
    time.sleep(0.5)
    myElem = myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'RegisterForm-email'))).send_keys(em)
    time.sleep(0.5)
    myElem = myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'RegisterForm-pass'))).send_keys(pw)
    time.sleep(0.5)
    myElem = myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'RegisterForm-confirmpass'))).send_keys(pw)
    time.sleep(0.5)
    a = driver.execute_script("return Register2()")
    time.sleep(0.5)
    try:
        alert = WebDriverWait(driver, 2).until(EC.alert_is_present())
        testTextAlert = alert.text
        alert.accept()
    except TimeoutException:
        print(Fore.RED+"TestCase Tạo Tài Khoản Thất Bại")
        return
    if(testTextAlert == 'Đăng ký thành công tự động đăng nhập !'):
        print(Fore.GREEN+"TestCase Tạo Tài Khoản Thành Công")
        demTestcaseDangKi = demTestcaseDangKi+1
    else:
        print(Fore.RED+"TestCase Tạo Tài Khoản Thất Bại")
    try:
        alert = WebDriverWait(driver, 2).until(EC.alert_is_present())
        testTextAlert = alert.text
        alert.accept()
        return
    except TimeoutException:
        pass
def findProduct(x):
    global demTestcaseTimKiem
    driver.get("https://doantesting.netlify.app/#")
    myElem = myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'navbar-search-input'))).send_keys(x)
    time.sleep(0.5)
    myElem = myElem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'navbar-search-input'))).send_keys(Keys.RETURN)
    try:
        alert = WebDriverWait(driver, 2).until(EC.alert_is_present())
        time.sleep(0.5)
        testTextAlert = alert.text
        alert.accept()
        print(Fore.RED+"Testcase Tìm Kiếm Thất Bại")
        return
    except TimeoutException:
        pass
    time.sleep(2)
    driver.execute_script("gettestListseach()")
    testthong = driver.execute_script("return testthong")
    if(type(testthong) == type(None)):
        print(Fore.RED+"Testcase Tìm Kiếm ra được 0 Kết quả")
        return
    else:
        dem = 0
        for i in testthong:
            if(x.lower() in i.lower()):
                dem+=1
        if(len(testthong)==0):
            print(Fore.RED+"Testcase Tìm Kiếm ra được 0 Kết quả")
            return
        if(dem>=len(testthong)/2):
            print(Fore.GREEN+"Testcase Tìm Kiếm Thành Công"+Style.RESET_ALL)
            demTestcaseTimKiem+=1
#======================================================
def Menuroot():
    global demTestcaseDangKi
    global demTestcaseDangNhap
    global demTestcaseTimKiem
    demTestcaseDangNhap = 0
    demTestcaseDangKi = 0
    demTestcaseTimKiem = 0
    print(Style.RESET_ALL)
    print("======= Danh Sách Thao Tác =======")
    print("1.Kiểm thử Chức Năng Đăng Nhập")
    print("2.Kiểm thử Chức Năng Đăng Kí")
    print("3.Kiểm Thử Chức Năng Tìm Kiếm")
    print("0.Thoát")
    val = input("mời bạn nhập lựa chọn ")
    val = int(val)
    if(val ==1):
        MenuDangNhap()
    elif(val ==2):
        MenuDangKi()
    elif(val ==3):
        MenuTimKiem()
    elif(val ==4):
        print("chon lua 4")
    else:
        print("Thoat")
        driver.quit()
        global checker
        checker = True
def MenuDangNhap():
    global demTestcaseDangNhap
    print("================= Danh Sách Đăng Nhập =================")
    print("1.TC1 Kiểm Thử Đăng Nhập Tài Khoản Đúng Mật Khẩu Đúng:")
    print("2.TC2 Kiểm Thử Đăng Nhập Tài Khoản sai:")
    print("3.TC3 Kiểm Thử Đăng Nhập Tài Khoản Đúng Nhưng Mật Khẩu Sai:")
    print("4.TC4 Kiểm Thử Đăng Nhập Tài Khoản để trống:")
    print("5.TC5 Kiểm Thử Đăng Nhập Tài Khoản để Đúng Mật Khẩu Để trống:")
    print("6.Kiểm thử Tất Cả Và Xuất Báo Cáo")
    print("7.Nhập Tay Để Đăng Nhập:")
    print("phím Bất Kì Để Thoát Danh Sách")
    val = input("mời bạn nhập lựa chọn ")
    val = int(val)
    if(val ==1):
        login("testdung@gmail.com", "123123123dung")
    elif(val ==2):
        login("testsai@gmail.com", "123123123dung")
    elif(val ==3):
        login("testdung@gmail.com", "123123123sai")
    elif(val ==4):
        login("", "123123123dung")
    elif(val ==5):
        login("testdung@gmail.com", "")
    elif(val ==6):
        demTestcaseDangNhap =0
        login("testdung@gmail.com", "123123123dung")
        login("testsai@gmail.com", "123123123dung")
        login("testdung@gmail.com", "123123123sai")
        login("", "123123123dung")
        login("testdung@gmail.com", "")
    elif(val ==7):
        val1 = input("nhập vào Tên Đăng Nhập (email): ")
        val2 = input("nhập vào Mật Khẩu Đăng Nhập : ")
        login(val1, val2)
    print(Style.RESET_ALL)
    print( Back.GREEN+"Tổng testcase Thành Công ",demTestcaseDangNhap)
    print(Style.RESET_ALL+"Tổng testcase Thất Bại ",(5-demTestcaseDangNhap))
    if(val==0):
        return

def MenuDangKi():
    global demTestcaseDangKi
    print("================= Danh Sách Đăng Kí =================")
    print("1.TC1 TTK có kí tự đặc biệt:")
    print("2.TC2 MK không đủ 8 kí tự:")
    print("3.TC3 TTK và MK Hợp lệ(TK MK không để trống, MK trên 8 kí tự):")
    print("4.TC4 Kiểm Thử Đăng Kí Tài Khoản để trống:")
    print("5.TC5 Kiểm Thử Đăng Kí Tài Khoản để Đúng Mật Khẩu Để trống:")
    print("6.TC6 Kiểm Thử Đăng Kí Tài Khoản có Email không hợp lệ:")
    print("7.TC6 Kiểm Thử Đăng Kí Tài Khoản đã có trong hệ thống:")
    print("8.Kiểm tra Tất cả các testcase trên:")
    print("9.Nhập Tay Để Đăng Kí: ")
    print("nhấn phím bất kì để thoát")
    val = input("mời bạn nhập lựa chọn ")
    val = int(val)
    if(val ==1):
        sigin("userCo@#!", "usertestcase01@gmail.com", "123123123")
    if(val ==2):
        sigin("usertestcase2", "usertestcase02@gmail.com", "pw")
    if(val ==3):
        sigin("usertestcase3", "usertestcase03@gmail.com", "123123123")
    if(val ==4):
        sigin("", "usertestcase04@gmail.com", "123123123")
    if(val ==5):
        sigin("usertestcase5", "usertestcase05@gmail.com", "")
    if(val ==6):
        sigin("usertestcase6", "usertestcase06", "123123123")
    if(val ==7):
        sigin("usertestDaCo", "usertestDaCo@gmail.com", "123123123")
    if(val==8):
        demTestcaseDangKi = 0
        sigin("userCo@#!", "usertestcase01@gmail.com", "123123123")
        sigin("usertestcase2", "usertestcase01@gmail.com", "pw")
        sigin("usertestcase3", "usertestcase03@gmail.com", "123123123")
        sigin("", "usertestcase04@gmail.com", "123123123")
        sigin("usertestcase5", "usertestcase01@gmail.com", "")
        sigin("usertestcase6", "usertestcase06", "123123123")
        sigin("usertestDaCo", "usertestDaCo@gmail.com", "123123123")
        print(Style.RESET_ALL)
        print(Back.GREEN+"tổng số testcase thành công: ",demTestcaseDangKi)
        print(Style.RESET_ALL+"tổng số testcase thất bại: ",(7-demTestcaseDangKi))
    if(val==9):
        val1 = input("Điền Vào Tên Đăng Nhập: ")
        val2 = input("Điền Vào Email: ")
        val3 = input("Điền Vào Mật Khẩu: ")
        sigin(val1, val2, val3)
    else:
        return
def MenuTimKiem():
    global demTestcaseTimKiem
    print("================= Danh Sách Tìm Kiếm=================")
    print("1.TC1 Giá trị tìm kiếm có trong hệ thống:")
    print("2.TC2 Giá trị tìm kiếm không có trong hệ thống:")
    print("3.TC3 Giá trị tìm kiếm là giá trị rỗng:")
    print("4.Kiểm tra Tất cả các testcase trên:")
    print("5.Kiểm tra Tất cả các testcase trên:")
    print("nhấn phím bất kì để thoát")
    val = input("mời bạn nhập lựa chọn ")
    val = int(val)
    if(val==1):
        findProduct("Black Pink")
    if(val==2):
        findProduct("Thông nhập bậy")
    if(val==3):
        findProduct("")
    if(val==4):
        global demTestcaseTimKiem
        demTestcaseTimKiem =0
        findProduct("Black Pink")
        findProduct("Thông nhập bậy")
        findProduct("")
    if(val==5):
        val = input("Nhập vào Giá Trị Kiếm Muốn Kiểm Thử: ")
        findProduct(val)
    print(Style.RESET_ALL)
    print(Back.GREEN+"Tổng số testcase Thành công ",demTestcaseTimKiem)
    print(Style.RESET_ALL+"Tổng số testcase Thất Bại ",3-demTestcaseTimKiem)
 #========================================   
checker = False
demTestcaseDangNhap = 0
demTestcaseDangKi = 0
demTestcaseTimKiem = 0
while(checker != True):
    Menuroot()