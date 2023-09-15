import random
import datetime


start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2022, 1, 1)

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
file_lines = []

with open("dataset/out.petster-hamster", "r") as old_dataset:
    for line in old_dataset.readlines():
        line = line.strip()
        random_number_of_days = random.randrange(days_between_dates)
        line = "\t".join(line.split("\t"))
        new_line = "\t".join([line, str(random_number_of_days), "\n"])
        file_lines.append(new_line)


with open("dataset/out.petster-hamster.tsv", "w+") as new_dataset:
    new_dataset.writelines(file_lines)

# print(random_number_of_days)
# random_date = start_date + datetime.timedelta(days=random_number_of_days)


# print(random_date)
