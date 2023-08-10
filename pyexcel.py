import xlsxwriter

def makePDF():
   # Create a new Excel workbook and add a worksheet
    workbook = xlsxwriter.Workbook('output.xlsx')
    worksheet = workbook.add_worksheet()

    # Set the width of the columns
    worksheet.set_column('A:C', 20)

    # Add headers
    headers = ['No', 'Name', 'Position', 'Office','Facebook','Instagram', 'twitter','LinkedIn', 'Tiktok', 'Youtube','Start date', 'Salary']
    worksheet.write_row('A1', headers)

    # Sample data
    data = [
        (1, 'Ashton Cox', 'Junior Technical Author','San Fransico', 'https://github.com/','https://github.com/','https://github.com/','https://github.com/','https://github.com/','https://github.com/','2009-01-12', '$86,000'),
        (2, 'Cedric Kelly', 'Senior Javascript Developer','Edinburgh', 'https://github.com/','https://github.com/','https://github.com/','https://github.com/','https://github.com/','https://github.com/','2012-013-29', '$433,060'),
        (3, 'Tiger Hair', 'System Architect','Edinburgh', 'https://github.com/','https://github.com/','https://github.com/','https://github.com/','https://github.com/','https://github.com/','2011-04-25', '$320,800'),
        (4, 'Tiger Nixon', 'System Architect','Edinburgh', 'https://github.com/','https://github.com/','https://github.com/','https://github.com/','https://github.com/','https://github.com/','2011-04-25', '$320,800'),
    ]

    image_width = 80
    image_height = 80
    # Add data to the worksheet
    for row_num, (no, name, position, office, facebook_url, instagram_url, twitter_url, linkedin_url, tiktok_url, youtube_url,startdate, salary ) in enumerate(data, start=2):
        worksheet.write_number(row_num-1, 0, no)
        worksheet.write_string(row_num-1, 1, name)
        worksheet.write_string(row_num-1, 2, position)
        worksheet.write_string(row_num-1, 3, office)
        
        # Create a clickable image with a hyperlink
        image_path = 'twitter.png'  # Replace with the actual path to your image
        worksheet.insert_image(row_num-1, 4, image_path, {'url': facebook_url, 'x_scale': image_width/100, 'y_scale': image_height/100})

        image_path = 'youtube.png'  # Replace with the actual path to your image
        worksheet.insert_image(row_num-1, 5, image_path, {'url': instagram_url, 'x_scale': image_width/100, 'y_scale': image_height/100})

        image_path = 'twitter.png'  # Replace with the actual path to your image
        worksheet.insert_image(row_num-1, 6, image_path, {'url': twitter_url, 'x_scale': image_width/100, 'y_scale': image_height/100})

        image_path = 'youtube.png'  # Replace with the actual path to your image
        worksheet.insert_image(row_num-1, 7, image_path, {'url': linkedin_url, 'x_scale': image_width/100, 'y_scale': image_height/100})

        image_path = 'twitter.png'  # Replace with the actual path to your image
        worksheet.insert_image(row_num-1, 8, image_path, {'url': tiktok_url, 'x_scale': image_width/100, 'y_scale': image_height/100})

        image_path = 'youtube.png'  # Replace with the actual path to your image
        worksheet.insert_image(row_num-1, 9, image_path, {'url': youtube_url, 'x_scale': image_width/100, 'y_scale': image_height/100})

        worksheet.write_string(row_num-1, 10, startdate)
        worksheet.write_string(row_num-1, 11, salary)

    # Close the workbook
    workbook.close()

    return 'output'
