#! run.py

'''
************************ APK DOWNLOADER ************************
----------------------------------------------------------------
example requests :
----------------------------------------------------------------
http://0.0.0.0:4444/?id=com.kamasutra.sexual.app.CoupleSexGame

----------------------------------------------------------------
response :
----------------------------------------------------------------
{
    link_download: "https://download.apkpure.com/b/apk/Y29tLmthbWFzdXRyYS5zZXh1YWwuYXBwLkNvdXBsZVNleEdhbWVfM18xZjEyMTIx?_fn=Q291cGxlIFNleCBHYW1lcyAxOF92c2V4dWFsIGFwcF9hcGtwdXJlLmNvbS5hcGs%3D&k=a01c721844384850272621fe0f812f8f58f98997&as=ac3c73c276d943eecf65c920b387804b58f6e70f&_p=Y29tLmthbWFzdXRyYS5zZXh1YWwuYXBwLkNvdXBsZVNleEdhbWU%3D&c=1%7CENTERTAINMENT",
    meta: {
        code: 200,
        message: "OK"
    }
}
'''

from flask import Flask, request, jsonify 
import bs4, requests
app = Flask(__name__)
app.debug = True

@app.route('/')
def apkpure_generator_apk():
    rows = {}
    try:
        docid = request.args.get('id')
        req = requests.get('https://apkpure.com/apkpure/%s/download?from=details' % docid)
        result = bs4.BeautifulSoup(req.text)
        link_download = result.find(attrs={"id": "download_link"}).get('href')
        rows['meta'] = {
            'code'      : 200,
            'message'   : 'OK'
        }
        rows['link_download'] = link_download
    except Exception as e:
        rows['meta'] = {
            'code'      : 404,
            'message'   : str(e)
        }
    return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444)
