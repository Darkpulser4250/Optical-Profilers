import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from flask import Flask, render_template, request, redirect

# File Extraction Code
def pdf_extracter(fileName):
    filesize = os. path. getsize("notes.txt") 
    if filesize == 0: 
        print("The file is empty: " + str(filesize))
        vr_doc = ["Texas Voter Registration Application"]
        ballot = []

        file_path = fileName
        pdf = PdfFileReader(file_path)

        with open('notes.txt', 'w') as f:
            for page_num in range(pdf.numPages):
                print('Page: {0}'.format(page_num))
                pageObj = pdf.getPage(page_num)

                try: 
                    txt = pageObj.extractText()
                    print(''.center(100, '-'))
                except:
                    pass
                else:
                    f.write('Page {0}\n'.format(page_num+1))
                    f.write(''.center(100, '-'))
                    f.write(txt)
            f.close()
            f = open("notes.txt", "r")
            # print(f.read())
            if vr_doc[0] in f.read():
                print("Saved in the Texas Voter Registration Application folder")
            else:
                print("NOT")
        
    else: 
        print("File not Empty, Truncating.....")
        with open("notes.txt", 'r+') as f:
            f.truncate(0)
            print("Truncating.....COMPLETE!!!")


# add flask
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/upload',methods=['POST'])
def upload_fileName():
    file = request.files['inputFile']
    pdf_extracter(file.filename)

    return 'extractor completed'



    
    
if __name__ == "__main__":
    # pdf_extracter("vr_app.pdf")
    app.run(debug=True)