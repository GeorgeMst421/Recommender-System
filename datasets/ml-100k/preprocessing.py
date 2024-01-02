import csv
import os



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

def convertion():
    converted_path = 'converted_csv'
    os.makedirs(converted_path, exist_ok=True)
    convert_u_data('u.data', 'converted_csv\u_data.csv')
    # convert_u_info('u.info', 'converted_csv\u_info.csv')
    # convert_u_item('u.item', 'converted_csv\u_item.csv')
    # convert_u_genre('u.genre', 'converted_csv\u_genre.csv')
    # convert_u_user('u.user', 'converted_csv\u_user.csv')
    # convert_u_occupation('u.occupation', 'converted_csv\u_occupation.csv')
    print('finished')



