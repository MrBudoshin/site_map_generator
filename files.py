import csv


def file(creat):
    table = ['url', 'time', 'count', 'file_name']
    with open('stash.csv', 'a', newline='') as out_csv:
        writer = csv.writer(out_csv)
        writer.writerow(table)
        with open('stash.csv', 'a', newline='') as out:
            write = csv.writer(out)
            for resp in creat:
                write.writerow(resp)