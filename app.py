from flask import Flask, request, render_template, redirect, url_for
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("models/modelForPrediction.pkl", 'rb'))



@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        
        having_IP_Address = int(request.form.get('having_IP_Address'))
        URL_Length = int(request.form.get('URL_Length'))
        Shortining_Service = int(request.form.get('Shortining_Service'))
        having_At_Symbol = int(request.form.get('having_At_Symbol'))
        double_slash_redirecting = int(request.form.get('double_slash_redirecting'))
        Prefix_Suffix = int(request.form.get('Prefix_Suffix'))
        having_Sub_Domain = int(request.form.get('having_Sub_Domain'))
        SSLfinal_State = int(request.form.get('SSLfinal_State'))
        Domain_registeration_length = int(request.form.get('Domain_registeration_length'))
        Favicon = int(request.form.get('Favicon'))
        port = int(request.form.get('port'))
        HTTPS_token = int(request.form.get('HTTPS_token'))
        Request_URL = int(request.form.get('Request_URL'))
        URL_of_Anchor = int(request.form.get('URL_of_Anchor'))
        Links_in_tags = int(request.form.get('Links_in_tags'))
        SFH = int(request.form.get('SFH'))
        Submitting_to_email = int(request.form.get('Submitting_to_email'))
        Abnormal_URL = int(request.form.get('Abnormal_URL'))
        Redirect = int(request.form.get('Redirect'))
        on_mouseover = int(request.form.get('on_mouseover'))
        RightClick = int(request.form.get('RightClick'))
        popUpWidnow = int(request.form.get('popUpWidnow'))
        Iframe = int(request.form.get('Iframe'))
        age_of_domain = int(request.form.get('age_of_domain'))
        DNSRecord = int(request.form.get('DNSRecord'))
        web_traffic = int(request.form.get('web_traffic'))
        Page_Rank = int(request.form.get('Page_Rank'))
        Google_Index = int(request.form.get('Google_Index'))
        Links_pointing_to_page = int(request.form.get('Links_pointing_to_page'))
        Statistical_report = int(request.form.get('Statistical_report'))
        
        
        data=[[having_IP_Address, URL_Length, Shortining_Service,
       having_At_Symbol, double_slash_redirecting, Prefix_Suffix,
       having_Sub_Domain, SSLfinal_State, Domain_registeration_length,
       Favicon, port, HTTPS_token, Request_URL, URL_of_Anchor,
       Links_in_tags, SFH, Submitting_to_email, Abnormal_URL,
       Redirect, on_mouseover, RightClick, popUpWidnow, Iframe,
       age_of_domain, DNSRecord, web_traffic, Page_Rank,
       Google_Index, Links_pointing_to_page, Statistical_report]]

        columns = ['having_IP_Address', 'URL_Length', 'Shortining_Service',
       'having_At_Symbol', 'double_slash_redirecting', 'Prefix_Suffix',
       'having_Sub_Domain', 'SSLfinal_State', 'Domain_registeration_length',
       'Favicon', 'port', 'HTTPS_token', 'Request_URL', 'URL_of_Anchor',
       'Links_in_tags', 'SFH', 'Submitting_to_email', 'Abnormal_URL',
       'Redirect', 'on_mouseover', 'RightClick', 'popUpWidnow', 'Iframe',
       'age_of_domain', 'DNSRecord', 'web_traffic', 'Page_Rank',
       'Google_Index', 'Links_pointing_to_page', 'Statistical_report']

        # Create DataFrame
        input_df = pd.DataFrame(data, columns=columns)

        prediction=model.predict(input_df)

        return render_template('result.html', result=prediction)

    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")

