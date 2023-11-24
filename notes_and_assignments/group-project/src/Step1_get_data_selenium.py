from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge()
driver.maximize_window()
driver.get('https://footystats.org/england/premier-league')

start_year = 2007
end_year = 2023
Years = [
    f'{year}/{str(year+1)[-2:]}' for year in range(start_year, end_year + 1)]
# year = '2022/23'


for year in Years:
    select = driver.find_element(By.CLASS_NAME, "drop-down-parent.fl.boldFont")
    select.click()
    time.sleep(2)
    # Replace 'your_data_hash_value' with the specific value you want to select
    # chooseSeason = driver.find_element(By.)
    # get element
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, year))
    )
    element.click()
    time.sleep(2)
    # mp, win, draw, loss, gf, ga, gd
    # Find an element by its class (replace 'element_class' with the actual class of the element on the webpage)
    TEAMs = driver.find_elements(
        By.CLASS_NAME, 'bold.hover-modal-parent.hover-modal-ajax-team')
    MPs = driver.find_elements(By.CLASS_NAME, 'mp')
    WINs = driver.find_elements(By.CLASS_NAME, 'win')
    DRAWs = driver.find_elements(By.CLASS_NAME, 'draw')
    LOSSs = driver.find_elements(By.CLASS_NAME, 'loss')
    GFs = driver.find_elements(By.CLASS_NAME, 'gf')
    GAs = driver.find_elements(By.CLASS_NAME, 'ga')
    GDs = driver.find_elements(By.CLASS_NAME, 'gd')
    POINTs = driver.find_elements(By.CLASS_NAME, 'points.bold')
    # Get text content from the element
    team_list = []
    mp_list = []
    win_list = []
    draw_list = []
    loss_list = []
    gf_list = []
    ga_list = []
    gd_list = []
    point_list = []

    for team in TEAMs:
        text_content = team.text
        team_list.append(text_content)

    for mp in MPs:
        text_content = mp.text
        # Use regex to extract only numbers
        numbers = re.findall(r'\d+', text_content)
        # Concatenate the numbers if there are multiple matches
        valid_numbers = [int(num) for num in numbers if num]
        # Append the valid numbers to the list
        mp_list.extend(valid_numbers)

    for win in WINs:
        text_content = win.text
        # Use regex to extract only numbers
        numbers = re.findall(r'\d+', text_content)
        # Concatenate the numbers if there are multiple matches
        valid_numbers = [int(num) for num in numbers if num]
        # Append the valid numbers to the list
        win_list.extend(valid_numbers)

    for draw in DRAWs:
        text_content = draw.text
        # Use regex to extract only numbers
        numbers = re.findall(r'\d+', text_content)
        # Concatenate the numbers if there are multiple matches
        valid_numbers = [int(num) for num in numbers if num]
        # Append the valid numbers to the list
        draw_list.extend(valid_numbers)

    for loss in LOSSs:
        text_content = loss.text
        # Use regex to extract only numbers
        numbers = re.findall(r'\d+', text_content)
        # Concatenate the numbers if there are multiple matches
        valid_numbers = [int(num) for num in numbers if num]
        # Append the valid numbers to the list
        loss_list.extend(valid_numbers)

    for gf in GFs:
        text_content = gf.text
        # Use regex to extract only numbers
        numbers = re.findall(r'\d+', text_content)
        # Concatenate the numbers if there are multiple matches
        valid_numbers = [int(num) for num in numbers if num]
        # Append the valid numbers to the list
        gf_list.extend(valid_numbers)

    for ga in GAs:
        text_content = ga.text
        # Use regex to extract only numbers
        numbers = re.findall(r'\d+', text_content)
        # Concatenate the numbers if there are multiple matches
        valid_numbers = [int(num) for num in numbers if num]
        # Append the valid numbers to the list
        ga_list.extend(valid_numbers)

    for gd in GDs:
        text_content = gd.text
        # Use regex to extract only numbers
        numbers = re.findall(r'-?\d+', text_content)
        # Concatenate the numbers if there are multiple matches
        valid_numbers = [int(num) for num in numbers if num]
        # Append the valid numbers to the list
        gd_list.extend(valid_numbers)

    for point in POINTs:
        text_content = point.text
        # Use regex to extract only numbers
        numbers = re.findall(r'\d+', text_content)
        # Concatenate the numbers if there are multiple matches
        valid_numbers = [int(num) for num in numbers if num]
        # Append the valid numbers to the list
        point_list.extend(valid_numbers)

    # Print the list of extracted numbers
    print('TEAM List is:', team_list)
    print('MP List is:', mp_list)
    print('WIN List is:', win_list)
    print('DRAW List is:', draw_list)
    print('Loss List is:', loss_list)
    print('GF List is:', gf_list)
    print('GA List is:', ga_list)
    print('GD List is:', gd_list)
    print('POINT List is:', point_list)

    # CSV file
    year_file = year.replace('/', '_')
    csv_file_path = './' + 'Data/' + year_file + '.csv'

    # write data to csv
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # edit header
        header = ['Team', 'MP', 'Win', 'Draw',
                  'Loss', 'GF', 'GA', 'GD', 'Points']
        writer.writerow(header)

        # write data
        for i in range(len(team_list)):
            row = [team_list[i], mp_list[i], win_list[i], draw_list[i],
                   loss_list[i], gf_list[i], ga_list[i], gd_list[i], point_list[i]]
            writer.writerow(row)

    print(f'Data has been written to {csv_file_path}')

driver.quit()
