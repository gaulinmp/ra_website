import os
import json
from tempfile import mkstemp


# from django.conf import settings as SETTINGS

def between(lower, number, upper):
    return max(lower, min(number, upper))

def handle_uploaded_file(upload_type, upload_file):
    """
    Reads in file (to disk) and returns pandas dataframe.

    Super advanced method to upload files.
    Could it work without hitting disk? Probably.
    Will I write such an improvement? Nopers.
    """
    import pandas as pd
    fd, temp_path = mkstemp()
    with open(temp_path, 'wb+') as fh:
        fh.write(upload_file.read())

    if upload_type == 'xlsx':
        df = pd.read_excel(temp_path)
    elif upload_type == 'json':
        df = pd.read_json(temp_path, orient='records')

    os.close(fd)
    os.remove(temp_path)

    return df

def handle_download_file(objects, download_type='xlsx'):
    import pandas as pd

    df = pd.DataFrame(list(objects.values()))

    fd, temp_path = mkstemp()

    if download_type == 'xlsx':
        df.to_excel(temp_path, index=False, engine='openpyxl')
    elif download_type == 'json':
        df.to_json(temp_path, orient='records', index=False)

    with open(temp_path, 'rb') as fh:
        dat = fh.read()

    os.close(fd)
    os.remove(temp_path)

    return dat
