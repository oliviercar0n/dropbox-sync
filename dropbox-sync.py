import os

EXTERNAL_DRIVE_PATH = '###'
DROPBOX_TOKEN = '###'

if os.path.ismount(EXTERNAL_DRIVE_PATH):
    
    import dropbox
    import unidecode
    import datetime

    dbx = dropbox.Dropbox(DROPBOX_TOKEN)

    dbx_path = '###'
    hd_path = '###'
    
    dbx_query = dbx.files_list_folder(dbx_path)
    dbx_entries = [unidecode.unidecode(entry.name) for entry in dbx_query.entries]

    succ = 0
    for root, dirs, files in os.walk(hd_path):
        for file in files:
            try:
                if file [:1] != '.' and file[-1] != '\r' and unidecode.unidecode(file) not in dbx_entries:
                    dbx.files_upload(open(hd_path + file, 'rb').read(),dbx_path+file)
                    print(str(datetime.datetime.now()) + "   " + file)
            except Exception as e: print(e)