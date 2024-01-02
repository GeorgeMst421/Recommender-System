import csv
import os
#
# This file is used to convert the files u.data, u.info, u.item,
# u.occupation, u.user and u.genre into csv 's
#

def convert_u_data(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter='\t')
        writer = csv.writer(outfile)

        # Write header
        writer.writerow(['user_id', 'item_id', 'rating', 'timestamp'])

        # Write data
        for row in reader:
            writer.writerow(row)

def convert_u_info(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        lines = infile.readlines()

        # Extract information
        num_users, num_items, num_ratings = map(int, [line.split()[0] for line in lines])

        # Write to CSV
        writer = csv.writer(outfile)
        writer.writerow(['num_users', 'num_items', 'num_ratings'])
        writer.writerow([num_users, num_items, num_ratings])


def convert_u_item(input_file, output_file):
    with open(input_file, 'r', encoding='ISO-8859-1') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile, delimiter='|')
        writer = csv.writer(outfile)

        # Write header
        header = next(reader)
        new_header = header[:5] + header[5:24]  # Extract relevant fields
        writer.writerow(new_header)

        # Write data
        for row in reader:
            movie_id = row[0]
            title = row[1]
            release_date = row[2]
            video_release_date = row[3]
            imdb_url = row[4]
            genres = row[5:]

            # Create a new row with relevant fields
            new_row = [movie_id, title, release_date, video_release_date, imdb_url] + genres
            writer.writerow(new_row)

def convert_u_genre(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter='|')
        writer = csv.writer(outfile)

        # Write header
        writer.writerow(['genre'])

        # Write data
        for row in reader:
            writer.writerow(row)

def convert_u_user(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter='|')
        writer = csv.writer(outfile)

        # Write header
        writer.writerow(['user_id', 'age', 'gender', 'occupation', 'zip_code'])

        # Write data
        for row in reader:
            writer.writerow(row)

def convert_u_occupation(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter='|')
        writer = csv.writer(outfile)

        # Write header
        writer.writerow(['occupation'])

        # Write data
        for row in reader:
            writer.writerow(row)

def convert(directory_path):
    os.makedirs('converted_csv', exist_ok=True)

    u_data_dir = os.path.join(directory_path, 'u.data')
    u_info_dir = os.path.join(directory_path, 'u.info')
    u_item_dir = os.path.join(directory_path, 'u.item')
    u_genre_dir = os.path.join(directory_path, 'u.genre')
    u_user_dir = os.path.join(directory_path, 'u.user')
    u_occupation_dir = os.path.join(directory_path, 'u.occupation')


    convert_u_data(u_data_dir, 'converted_csv\\u_data.csv')
    convert_u_info(u_info_dir, 'converted_csv\\u_info.csv')
    convert_u_item(u_item_dir, 'converted_csv\\u_item.csv')
    convert_u_genre(u_genre_dir, 'converted_csv\\u_genre.csv')
    convert_u_user(u_user_dir, 'converted_csv\\u_user.csv')
    convert_u_occupation(u_occupation_dir, 'converted_csv\\u_occupation.csv')
    print('Files converted to csv')



