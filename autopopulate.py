# Import Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

# open Chrome
driver = webdriver.Chrome()

# Open URL
driver.get('https://docs.google.com/forms/d/e/1FAIpQLScpoZjdltqsIG5Ld9HYIg7pOwiEcCueYUig0kPRGz1WiimJLg/viewform')

# wait for three second, until page gets fully loaded
time.sleep(1)

users_data = [
    {
        'email': 'john.mathew@gmail.com',
        'name': 'John Mathew',
        'age': 35,
        'occupation': 'Software Engineer'
    },
    {
        'email': 'joseph.thomas@gmail.com',
        'name': 'Joseph Thomas',
        'age': 27,
        'occupation': 'Doctor'
    },
    {
        'email': 'samuel.george@gmail.com',
        'name': 'Samuel George',
        'age': 32,
        'occupation': 'Businessman'
    },
    {
        'email': 'david.paul@gmail.com',
        'name': 'David Paul',
        'age': 29,
        'occupation': 'Architect'
    },
    {
        'email': 'michael.johnson@gmail.com',
        'name': 'Michael Johnson',
        'age': 31,
        'occupation': 'Teacher'
    },
    {
        'email': 'matthew.joseph@gmail.com',
        'name': 'Matthew Joseph',
        'age': 33,
        'occupation': 'Lawyer'
    },
    {
        'email': 'andrew.samuel@gmail.com',
        'name': 'Andrew Samuel',
        'age': 34,
        'occupation': 'Accountant'
    },
    {
        'email': 'peter.davis@gmail.com',
        'name': 'Peter Davis',
        'age': 30,
        'occupation': 'Civil Engineer'
    },
    {
        'email': 'philip.alexander@gmail.com',
        'name': 'Philip Alexander',
        'age': 28,
        'occupation': 'Graphic Designer'
    },
    {
        'email': 'paul.wilson@gmail.com',
        'name': 'Paul Wilson',
        'age': 36,
        'occupation': 'Marketing Manager'
    },
    {
        'email': 'jacob.brown@gmail.com',
        'name': 'Jacob Brown',
        'age': 32,
        'occupation': 'Chef'
    },
    {
        'email': 'thomas.roberts@gmail.com',
        'name': 'Thomas Roberts',
        'age': 30,
        'occupation': 'Pharmacist'
    },
    {
        'email': 'simon.jackson@gmail.com',
        'name': 'Simon Jackson',
        'age': 29,
        'occupation': 'Journalist'
    },
    {
        'email': 'stephen.cook@gmail.com',
        'name': 'Stephen Cook',
        'age': 31,
        'occupation': 'Artist'
    },
    {
        'email': 'luke.morris@gmail.com',
        'name': 'Luke Morris',
        'age': 33,
        'occupation': 'Financial Analyst'
    },
    {
        'email': 'mark.stewart@gmail.com',
        'name': 'Mark Stewart',
        'age': 27,
        'occupation': 'Electrician'
    },
    {
        'email': 'timothy.white@gmail.com',
        'name': 'Timothy White',
        'age': 34,
        'occupation': 'Writer'
    },
    {
        'email': 'nathaniel.rogers@gmail.com',
        'name': 'Nathaniel Rogers',
        'age': 35,
        'occupation': 'Photographer'
    },
    {
        'email': 'james.taylor@gmail.com',
        'name': 'James Taylor',
        'age': 28,
        'occupation': 'Software Developer'
    },
    {
        'email': 'andreas.harris@gmail.com',
        'name': 'Andreas Harris',
        'age': 32,
        'occupation': 'Consultant'
    },
    {
        'email': 'daniel.wright@gmail.com',
        'name': 'Daniel Wright',
        'age': 30,
        'occupation': 'Dentist'
    },
    {
        'email': 'christopher.evans@gmail.com',
        'name': 'Christopher Evans',
        'age': 29,
        'occupation': 'Entrepreneur'
    },
    {
        'email': 'benjamin.kelly@gmail.com',
        'name': 'Benjamin Kelly',
        'age': 31,
        'occupation': 'Event Planner'
    },
    {
        'email': 'jonathan.hall@gmail.com',
        'name': 'Jonathan Hall',
        'age': 33,
        'occupation': 'Real Estate Agent'
    },
    {
        'email': 'patrick.miller@gmail.com',
        'name': 'Patrick Miller',
        'age': 28,
        'occupation': 'Journalist'
    },
    {
        'email': 'william.clark@gmail.com',
        'name': 'William Clark',
        'age': 30,
        'occupation': 'Doctor'
    },
    {
        'email': 'anthony.thompson@gmail.com',
        'name': 'Anthony Thompson',
        'age': 32,
        'occupation': 'Architect'
    },
    {
        'email': 'robert.harris@gmail.com',
        'name': 'Robert Harris',
        'age': 29,
        'occupation': 'Teacher'
    },
    {
        'email': 'richard.lewis@gmail.com',
        'name': 'Richard Lewis',
        'age': 34,
        'occupation': 'Lawyer'
    }
]

for user in users_data:

	# First Page
	primaryemail = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
	radiobuttons = driver.find_element(By.XPATH, '//*[@id="i9"]/div[3]')

	next = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

	primaryemail.send_keys(user['email'])
	radiobuttons.click()
	next.click()

	time.sleep(1)

	# Second Page
	emailID = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
	Name = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
	Age = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
	Sex = driver.find_element(By.XPATH, '//*[@id="i21"]/div[3]/div')

	xpaths_education = [
		'//*[@id="i31"]/div[3]/div',
		'//*[@id="i34"]/div[3]/div',
		'//*[@id="i37"]/div[3]/div',
		'//*[@id="i40"]/div[3]/div',
		'//*[@id="i43"]/div[3]/div'
	]
	selected_education = xpaths_education[random.randint(0, 4)]
	Education = driver.find_element(By.XPATH, selected_education)

	Occupation = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
	City = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input')
	
	xpaths_locality = [
		'//*[@id="i58"]/div[3]/div',
		'//*[@id="i61"]/div[3]/div',
		'//*[@id="i64"]/div[3]/div'
	]
	selected_xpaths_locality = xpaths_locality[random.randint(0, 2)]
	Locality = driver.find_element(By.XPATH, selected_xpaths_locality)

	Religion = driver.find_element(By.XPATH, '//*[@id="i77"]/div[3]/div')
	
	xpaths_family = [
		'//*[@id="i99"]/div[3]/div',
		'//*[@id="i102"]/div[3]/div',
		'//*[@id="i105"]/div[3]/div'
	]
	selected_xpaths_family = xpaths_family[random.randint(0, 2)]
	Family = driver.find_element(By.XPATH, selected_xpaths_family)

	next = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')

	emailID.send_keys(user['email'])
	Name.send_keys(user['name'])
	Age.send_keys(user['age'])
	Sex.click()
	Education.click()
	Occupation.send_keys(user['occupation'])
	City.send_keys("Mumbai")
	Locality.click()
	Religion.click()
	Family.click()

	time.sleep(1)

	next.click()

	time.sleep(1)

	# Third Page

	xpaths1 = [
		'//*[@id="i9"]/div[3]/div',
		'//*[@id="i12"]/div[3]/div',
		'//*[@id="i15"]/div[3]/div',
		'//*[@id="i18"]/div[3]/div',
		'//*[@id="i21"]/div[3]/div'
	]
	selected_xpath1 = xpaths1[random.randint(0, 4)]

	xpaths2 = [
		'//*[@id="i28"]/div[3]/div',
		'//*[@id="i31"]/div[3]/div',
		'//*[@id="i34"]/div[3]/div',
		'//*[@id="i37"]/div[3]/div',
		'//*[@id="i40"]/div[3]/div'
	]
	selected_xpath2 = xpaths2[random.randint(0, 4)]

	xpaths3 = [
		'//*[@id="i47"]/div[3]/div',
		'//*[@id="i50"]/div[3]/div',
		'//*[@id="i53"]/div[3]/div',
		'//*[@id="i56"]/div[3]/div',
		'//*[@id="i59"]/div[3]/div'
	]
	selected_xpath3 = xpaths3[random.randint(0, 4)]

	xpaths4 = [
		'//*[@id="i66"]/div[3]/div',
		'//*[@id="i69"]/div[3]/div',
		'//*[@id="i72"]/div[3]/div',
		'//*[@id="i75"]/div[3]/div',
		'//*[@id="i78"]/div[3]/div'
	]
	selected_xpath4 = xpaths4[random.randint(0, 4)]

	xpaths5 = [
		'//*[@id="i85"]/div[3]/div',
		'//*[@id="i88"]/div[3]/div',
		'//*[@id="i91"]/div[3]/div',
		'//*[@id="i94"]/div[3]/div',
		'//*[@id="i97"]/div[3]/div'
	]
	selected_xpath5 = xpaths5[random.randint(0, 4)]

	xpaths6 = [
		'//*[@id="i104"]/div[3]/div',
		'//*[@id="i107"]/div[3]/div',
		'//*[@id="i110"]/div[3]/div',
		'//*[@id="i113"]/div[3]/div',
		'//*[@id="i116"]/div[3]/div'
	]
	selected_xpath6 = xpaths6[random.randint(0, 4)]

	xpaths7 = [
		'//*[@id="i123"]/div[3]/div',
		'//*[@id="i126"]/div[3]/div',
		'//*[@id="i129"]/div[3]/div',
		'//*[@id="i132"]/div[3]/div',
		'//*[@id="i135"]/div[3]/div'
	]
	selected_xpath7 = xpaths7[random.randint(0, 4)]

	xpaths8 = [
		'//*[@id="i142"]/div[3]/div',
		'//*[@id="i145"]/div[3]/div',
		'//*[@id="i148"]/div[3]/div',
		'//*[@id="i151"]/div[3]/div',
		'//*[@id="i154"]/div[3]/div'
	]
	selected_xpath8 = xpaths8[random.randint(0, 4)]

	xpaths9 = [
		'//*[@id="i161"]/div[3]/div',
		'//*[@id="i164"]/div[3]/div',
		'//*[@id="i167"]/div[3]/div',
		'//*[@id="i170"]/div[3]/div',
		'//*[@id="i173"]/div[3]/div'
	]
	selected_xpath9 = xpaths9[random.randint(0, 4)]

	xpaths10 = [
		'//*[@id="i180"]/div[3]/div',
		'//*[@id="i183"]/div[3]/div',
		'//*[@id="i186"]/div[3]/div',
		'//*[@id="i189"]/div[3]/div',
		'//*[@id="i192"]/div[3]/div'
	]
	selected_xpath10 = xpaths10[random.randint(0, 4)]

	xpaths11 = [
		'//*[@id="i199"]/div[3]/div',
		'//*[@id="i202"]/div[3]/div',
		'//*[@id="i205"]/div[3]/div',
		'//*[@id="i208"]/div[3]/div',
		'//*[@id="i211"]/div[3]/div'
	]
	selected_xpath11 = xpaths11[random.randint(0, 4)]

	xpaths12 = [
		'//*[@id="i218"]/div[3]/div',
		'//*[@id="i221"]/div[3]/div',
		'//*[@id="i224"]/div[3]/div',
		'//*[@id="i227"]/div[3]/div',
		'//*[@id="i230"]/div[3]/div'
	]
	selected_xpath12 = xpaths12[random.randint(0, 4)]

	xpaths13 = [
		'//*[@id="i237"]/div[3]/div',
		'//*[@id="i240"]/div[3]/div',
		'//*[@id="i243"]/div[3]/div',
		'//*[@id="i246"]/div[3]/div',
		'//*[@id="i249"]/div[3]/div'
	]
	selected_xpath13 = xpaths13[random.randint(0, 4)]

	xpaths14 = [
		'//*[@id="i256"]/div[3]/div',
		'//*[@id="i259"]/div[3]/div',
		'//*[@id="i262"]/div[3]/div',
		'//*[@id="i265"]/div[3]/div',
		'//*[@id="i268"]/div[3]/div'
	]
	selected_xpath14 = xpaths14[random.randint(0, 4)]

	xpaths15 = [
		'//*[@id="i275"]/div[3]/div',
		'//*[@id="i278"]/div[3]/div',
		'//*[@id="i281"]/div[3]/div',
		'//*[@id="i284"]/div[3]/div',
		'//*[@id="i287"]/div[3]/div'
	]
	selected_xpath15 = xpaths15[random.randint(0, 4)]

	xpaths16 = [
		'//*[@id="i294"]/div[3]/div',
		'//*[@id="i297"]/div[3]/div',
		'//*[@id="i300"]/div[3]/div',
		'//*[@id="i303"]/div[3]/div',
		'//*[@id="i306"]/div[3]/div'
	]
	selected_xpath16 = xpaths16[random.randint(0, 4)]

	xpaths17 = [
		'//*[@id="i313"]/div[3]/div',
		'//*[@id="i316"]/div[3]/div',
		'//*[@id="i319"]/div[3]/div',
		'//*[@id="i322"]/div[3]/div',
		'//*[@id="i325"]/div[3]/div'
	]
	selected_xpath17 = xpaths17[random.randint(0, 4)]

	xpaths18 = [
		'//*[@id="i332"]/div[3]/div',
		'//*[@id="i335"]/div[3]/div',
		'//*[@id="i338"]/div[3]/div',
		'//*[@id="i341"]/div[3]/div',
		'//*[@id="i344"]/div[3]/div'
	]
	selected_xpath18 = xpaths18[random.randint(0, 4)]

	xpaths19 = [
		'//*[@id="i351"]/div[3]/div',
		'//*[@id="i354"]/div[3]/div',
		'//*[@id="i357"]/div[3]/div',
		'//*[@id="i360"]/div[3]/div',
		'//*[@id="i363"]/div[3]/div'
	]
	selected_xpath19 = xpaths19[random.randint(0, 4)]

	xpaths20 = [
		'//*[@id="i370"]/div[3]/div',
		'//*[@id="i373"]/div[3]/div',
		'//*[@id="i376"]/div[3]/div',
		'//*[@id="i379"]/div[3]/div',
		'//*[@id="i382"]/div[3]/div'
	]
	selected_xpath20 = xpaths20[random.randint(0, 4)]

	xpaths21 = [
		'//*[@id="i389"]/div[3]/div',
		'//*[@id="i392"]/div[3]/div',
		'//*[@id="i395"]/div[3]/div',
		'//*[@id="i398"]/div[3]/div',
		'//*[@id="i401"]/div[3]/div'
	]
	selected_xpath21 = xpaths21[random.randint(0, 4)]

	xpaths22 = [
		'//*[@id="i408"]/div[3]/div',
		'//*[@id="i411"]/div[3]/div',
		'//*[@id="i414"]/div[3]/div',
		'//*[@id="i417"]/div[3]/div',
		'//*[@id="i420"]/div[3]/div'
	]
	selected_xpath22 = xpaths22[random.randint(0, 4)]

	xpaths23 = [
		'//*[@id="i427"]/div[3]/div',
		'//*[@id="i430"]/div[3]/div',
		'//*[@id="i433"]/div[3]/div',
		'//*[@id="i436"]/div[3]/div',
		'//*[@id="i439"]/div[3]/div'
	]
	selected_xpath23 = xpaths23[random.randint(0, 4)]

	xpaths24 = [
		'//*[@id="i446"]/div[3]/div',
		'//*[@id="i449"]/div[3]/div',
		'//*[@id="i452"]/div[3]/div',
		'//*[@id="i455"]/div[3]/div',
		'//*[@id="i458"]/div[3]/div'
	]
	selected_xpath24 = xpaths24[random.randint(0, 4)]

	xpaths25 = [
		'//*[@id="i465"]/div[3]/div',
		'//*[@id="i468"]/div[3]/div',
		'//*[@id="i471"]/div[3]/div',
		'//*[@id="i474"]/div[3]/div',
		'//*[@id="i477"]/div[3]/div'
	]
	selected_xpath25 = xpaths25[random.randint(0, 4)]

	xpaths26 = [
		'//*[@id="i484"]/div[3]/div',
		'//*[@id="i487"]/div[3]/div',
		'//*[@id="i490"]/div[3]/div',
		'//*[@id="i493"]/div[3]/div',
		'//*[@id="i496"]/div[3]/div'
	]
	selected_xpath26 = xpaths26[random.randint(0, 4)]

	radiobuttons1 = driver.find_element(By.XPATH, selected_xpath1)
	radiobuttons2 = driver.find_element(By.XPATH, selected_xpath2)
	radiobuttons3 = driver.find_element(By.XPATH, selected_xpath3)
	radiobuttons4 = driver.find_element(By.XPATH, selected_xpath4)
	radiobuttons5 = driver.find_element(By.XPATH, selected_xpath5)
	radiobuttons6 = driver.find_element(By.XPATH, selected_xpath6)
	radiobuttons7 = driver.find_element(By.XPATH, selected_xpath7)
	radiobuttons8 = driver.find_element(By.XPATH, selected_xpath8)
	radiobuttons9 = driver.find_element(By.XPATH, selected_xpath9)
	radiobuttons10 = driver.find_element(By.XPATH, selected_xpath10)
	radiobuttons11 = driver.find_element(By.XPATH, selected_xpath11)
	radiobuttons12 = driver.find_element(By.XPATH, selected_xpath12)
	radiobuttons13 = driver.find_element(By.XPATH, selected_xpath13)
	radiobuttons14 = driver.find_element(By.XPATH, selected_xpath14)
	radiobuttons15 = driver.find_element(By.XPATH, selected_xpath15)
	radiobuttons16 = driver.find_element(By.XPATH, selected_xpath16)
	radiobuttons17 = driver.find_element(By.XPATH, selected_xpath17)
	radiobuttons18 = driver.find_element(By.XPATH, selected_xpath18)
	radiobuttons19 = driver.find_element(By.XPATH, selected_xpath19)
	radiobuttons20 = driver.find_element(By.XPATH, selected_xpath20)
	radiobuttons21 = driver.find_element(By.XPATH, selected_xpath21)
	radiobuttons22 = driver.find_element(By.XPATH, selected_xpath22)
	radiobuttons23 = driver.find_element(By.XPATH, selected_xpath23)
	radiobuttons24 = driver.find_element(By.XPATH, selected_xpath24)
	radiobuttons25 = driver.find_element(By.XPATH, selected_xpath25)
	radiobuttons26 = driver.find_element(By.XPATH, selected_xpath26)

	next = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')

	radiobuttons1.click()
	radiobuttons2.click()
	radiobuttons3.click()
	radiobuttons4.click()
	radiobuttons5.click()
	radiobuttons6.click()
	radiobuttons7.click()
	radiobuttons8.click()
	radiobuttons9.click()
	radiobuttons10.click()
	radiobuttons11.click()
	radiobuttons12.click()
	radiobuttons13.click()
	radiobuttons14.click()
	radiobuttons15.click()
	radiobuttons16.click()
	radiobuttons17.click()
	radiobuttons18.click()
	radiobuttons19.click()
	radiobuttons20.click()
	radiobuttons21.click()
	radiobuttons22.click()
	radiobuttons23.click()
	radiobuttons24.click()
	radiobuttons25.click()
	radiobuttons26.click()

	time.sleep(1)

	next.click()

	time.sleep(1)

	# Fourth Page
	xpaths1_1 = [
		'//*[@id="i9"]/div[3]/div',
		'//*[@id="i12"]/div[3]/div',
		'//*[@id="i15"]/div[3]/div',
		'//*[@id="i18"]/div[3]/div'
	]
	selected_xpath1_1 = xpaths1_1[random.randint(0, 3)]

	xpaths1_2 = [
		'//*[@id="i25"]/div[3]/div',
		'//*[@id="i28"]/div[3]/div',
		'//*[@id="i31"]/div[3]/div',
		'//*[@id="i34"]/div[3]/div'
	]
	selected_xpath1_2 = xpaths1_2[random.randint(0, 3)]

	xpaths1_3 = [
		'//*[@id="i41"]/div[3]/div',
		'//*[@id="i44"]/div[3]/div',
		'//*[@id="i47"]/div[3]/div',
		'//*[@id="i50"]/div[3]/div'
	]
	selected_xpath1_3 = xpaths1_3[random.randint(0, 3)]

	xpaths1_4 = [
		'//*[@id="i57"]/div[3]/div',
		'//*[@id="i60"]/div[3]/div',
		'//*[@id="i63"]/div[3]/div',
		'//*[@id="i66"]/div[3]/div'
	]
	selected_xpath1_4 = xpaths1_4[random.randint(0, 3)]

	xpaths1_5 = [
		'//*[@id="i73"]/div[3]/div',
		'//*[@id="i76"]/div[3]/div',
		'//*[@id="i79"]/div[3]/div',
		'//*[@id="i82"]/div[3]/div'
	]
	selected_xpath1_5 = xpaths1_5[random.randint(0, 3)]

	xpaths1_6 = [
		'//*[@id="i89"]/div[3]/div',
		'//*[@id="i92"]/div[3]/div',
		'//*[@id="i95"]/div[3]/div',
		'//*[@id="i98"]/div[3]/div'
	]
	selected_xpath1_6 = xpaths1_6[random.randint(0, 3)]

	xpaths1_7 = [
		'//*[@id="i105"]/div[3]/div',
		'//*[@id="i108"]/div[3]/div',
		'//*[@id="i111"]/div[3]/div',
		'//*[@id="i114"]/div[3]/div'
	]
	selected_xpath1_7 = xpaths1_7[random.randint(0, 3)]

	xpaths1_8 = [
		'//*[@id="i121"]/div[3]/div',
		'//*[@id="i124"]/div[3]/div',
		'//*[@id="i127"]/div[3]/div',
		'//*[@id="i130"]/div[3]/div'
	]
	selected_xpath1_8 = xpaths1_8[random.randint(0, 3)]

	xpaths1_9 = [
		'//*[@id="i137"]/div[3]/div',
		'//*[@id="i140"]/div[3]/div',
		'//*[@id="i143"]/div[3]/div',
		'//*[@id="i146"]/div[3]/div'
	]
	selected_xpath1_9 = xpaths1_9[random.randint(0, 3)]

	xpaths1_10 = [
		'//*[@id="i153"]/div[3]/div',
		'//*[@id="i156"]/div[3]/div',
		'//*[@id="i159"]/div[3]/div',
		'//*[@id="i162"]/div[3]/div'
	]
	selected_xpath1_10 = xpaths1_10[random.randint(0, 3)]

	radiobuttons1_1 = driver.find_element(By.XPATH, selected_xpath1_1)
	radiobuttons1_2 = driver.find_element(By.XPATH, selected_xpath1_2)
	radiobuttons1_3 = driver.find_element(By.XPATH, selected_xpath1_3)
	radiobuttons1_4 = driver.find_element(By.XPATH, selected_xpath1_4)
	radiobuttons1_5 = driver.find_element(By.XPATH, selected_xpath1_5)
	radiobuttons1_6 = driver.find_element(By.XPATH, selected_xpath1_6)
	radiobuttons1_7 = driver.find_element(By.XPATH, selected_xpath1_7)
	radiobuttons1_8 = driver.find_element(By.XPATH, selected_xpath1_8)
	radiobuttons1_9 = driver.find_element(By.XPATH, selected_xpath1_9)
	radiobuttons1_10 = driver.find_element(By.XPATH, selected_xpath1_10)

	radiobuttons1_1.click()
	radiobuttons1_2.click()
	radiobuttons1_3.click()
	radiobuttons1_4.click()
	radiobuttons1_5.click()
	radiobuttons1_6.click()
	radiobuttons1_7.click()
	radiobuttons1_8.click()
	radiobuttons1_9.click()
	radiobuttons1_10.click()

	# Submit
	submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')
	submit.click()

	# Another Response
	anotherResponse = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
	anotherResponse.click()

	time.sleep(1)

# close the window
driver.close()