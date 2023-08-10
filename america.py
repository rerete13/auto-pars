from selenium import webdriver
import time
from fake_useragent import UserAgent as Ua
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By as by
from selenium.webdriver.firefox.options import Options
from functools import cache


@cache
def get_america(vincode):
    # options
    options = Options()
    user_agent = Ua()
    options.add_argument(
        f"user-agent={user_agent.random}")
    

    options.headless = True
    # proxy
    # options.add_argument('--proxy-server=ingp3021228:31Fh7ndJ08@81.22.44.210:7951')
    # options.add_argument('--proxy-server=103.117.192.14')

    # proxy_options = {
    #     "https": f"http://{proxy_login}:{proxy_password}@81.22.44.210:7951"
    # }

    # conection
    driver = webdriver.Firefox(
        executable_path='geckodriver',
        options=options
    )

    try:
        driver.maximize_window()
        # start
        driver.get('https://bidfax.info')

    except Exception as e:
        print('-----------------------pass------------------------')
        print(e)

    try:
        print('-----------------------pass------------------------')
        driver.save_screenshot('lol.png')

    except Exception as e:
        print(e)
    
    try:
        print('-----------------------pass------------------------')
        time.sleep(4)
        enter_login = driver.find_element(by.XPATH, '//*[@id="search"]')
        enter_login.clear()
        enter_login.send_keys(f'{vincode}')

        enter = driver.find_element(by.XPATH, '//*[@id="submit"]')
        enter.click()

        time.sleep(4)
        getitem = driver.find_element(by.XPATH, '//*[@id="dle-content"]/div/div/div[1]/a/img')
        getitem.click()

        time.sleep(4)
        try:
            name = driver.find_element(by.XPATH, '//*[@id="dle-content"]/div/div[1]/h1').text
        except:
            pass
        try:
            auction = driver.find_element(by.XPATH, '//*[@id="aside"]/div/p[1]/span').text
        except:
            pass

        try:
            lot_number = driver.find_element(by.XPATH, '//*[@id="aside"]/div/p[2]/span').text
        except:
            pass

        try:
            data_sale = driver.find_element(by.XPATH, '//*[@id="aside"]/div/p[3]/span').text
        except:
            pass

        try:
            year = driver.find_element(by.XPATH, '//*[@id="aside"]/div/p[4]/span').text
        except:
            pass

        try:
            vin = driver.find_element(by.XPATH, '//*[@id="aside"]/div/p[5]/span').text
        except:
            pass

        try:
            condition = driver.find_element(by.XPATH, '//*[@id="aside"]/div/p[6]/span').text
        except:
            pass

        try:
            engine = driver.find_element(by.XPATH, '//*[@id="aside"]/div/p[7]/span').text
        except:
            pass

        try:
            mileage = driver.find_element(by.XPATH, '//*[@id="aside"]/div/p[8]/span').text
        except:
            pass

        # try:
        #     seller = driver.find_element(by.XPATH, '//*[@id="aside"]/div/p[9]/span').text
        # except:
        #     pass

        try:
            documents = driver.find_element(by.XPATH, '//*[@id="aside"]/div/p[10]/span').text
        except:
            pass

        try:
            location = driver.find_element(by.XPATH, '//*[@id="aside"]/div/p[11]/span').text
        except:
            pass

        try:
            primary_damage = driver.find_element(by.XPATH, '//*[@id="aside"]/div/p[12]/span').text
        except:
            pass

        try:
            secondary_damage = driver.find_element(by.XPATH, '//*[@id="aside"]/div/p[13]/span').text
        except:
            pass

        try:
            estimated_retail = driver.find_element(by.XPATH, '//*[@id="aside"]/div/p[14]/span').text
        except:
            pass

        try:
            estimated_repair = driver.find_element(by.XPATH, '//*[@id="aside"]/div/p[15]/span').text
        except:
            pass

        try:
            transmission = driver.find_element(by.XPATH, '//*[@id="aside"]/div/p[16]/span').text
        except:
            pass

        try:
            color = driver.find_element(by.XPATH, '//*[@id="aside"]/div/p[17]/span').text
        except:
            pass

        try:
            drive = driver.find_element(by.XPATH, '//*[@id="aside"]/div/p[18]/span').text
        except:
            pass

        try:
            fuel = driver.find_element(by.XPATH, '//*[@id="aside"]/div/p[19]/span').text
        except:
            pass

        try:
            keys = driver.find_element(by.XPATH, '//*[@id="aside"]/div/p[20]/span').text
        except:
            pass

        try:
            notes = driver.find_element(by.XPATH, '//*[@id="aside"]/div/p[21]/span').text
        except:
            pass


        photos = []
        for i in range(2,11):

            try:
                photo = driver.find_element(by.XPATH, f'//*[@id="dle-content"]/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div[{i}]/div/img')
            except:
                pass
            # print(photo.get_attribute('src'))
            photos.append(photo.get_attribute('src'))




    except Exception as ex:
        print(ex)


    finally:
        driver.close()
        driver.quit()
    
    return photos, name, auction, lot_number, data_sale, year, vin, condition, engine, mileage, documents, location, primary_damage, secondary_damage, estimated_retail, estimated_repair, transmission, color, drive, fuel, keys, notes


# print(get_america('3FA6P0H74GR310384'))