from __future__ import division, print_function

import os, uuid
import itertools as it

from win32com.client import DispatchEx
import pywintypes # for exception

def send_mail(subject,body_text,sendto,copyto=None,blindcopyto=None,
              attach=None):
    session = DispatchEx('Lotus.NotesSession')
    session.Initialize('your_password')

    server_name = 'your/server'
    db_name = 'your/database.nsf'

    db = session.getDatabase(server_name, db_name)
    if not db.IsOpen:
        try:
            db.Open()
        except pywintypes.com_error:
            print( 'could not open database: {}'.format(db_name) )

    doc = db.CreateDocument()
    doc.ReplaceItemValue("Form","Memo")
    doc.ReplaceItemValue("Subject",subject)

    # assign random uid because sometimes Lotus Notes tries to reuse the same one
    uid = str(uuid.uuid4().hex)
    doc.ReplaceItemValue('UNIVERSALID',uid)

    # "SendTo" MUST be populated otherwise you get this error: 
    # 'No recipient list for Send operation'
    doc.ReplaceItemValue("SendTo", sendto)

    if copyto is not None:
        doc.ReplaceItemValue("CopyTo", copyto)
    if blindcopyto is not None:
        doc.ReplaceItemValue("BlindCopyTo", blindcopyto)

    # body
    body = doc.CreateRichTextItem("Body")
    body.AppendText(body_text)

    # attachment 
    if attach is not None:
        attachment = doc.CreateRichTextItem("Attachment")
        for att in attach:
            attachment.EmbedObject(1454, "", att, "Attachment")

    # save in `Sent` view; default is False
    doc.SaveMessageOnSend = True
    doc.Send(False)

if __name__ == '__main__':
    subject = "test subject"
    body = "test body"
    sendto = ['abc@def.com',]
    files = ['/path/to/a/file.txt','/path/to/another/file.txt']
    attachment = it.takewhile(lambda x: os.path.exists(x), files)

    send_mail(subject, body, sendto, attach=attachment)
