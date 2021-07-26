import dropbox
def transferData():
    accessToken="Q1CXq4WtNqEAAAAAAAAAAQbsbuK4oodVbqiElodOW_p0NJjr9d5HB6zFI_w0oDXD"
    fileFrom="mahakall.txt"
    fileTo="/KingCoding/mahakall.txt"
    db=dropbox.Dropbox(accessToken)
    f=open(fileFrom,"rb")
    db.files_upload(f.read(),fileTo)
    print("success")
transferData()
