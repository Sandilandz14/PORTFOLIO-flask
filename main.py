from flask import Flask, render_template
from smtplib import SMTP


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# @app.route('/mail/',methods=["POST"])
# def send_mail():
#    try:
#        sender_email = request.form[('firstname')]
#        receiver_email = "type-receiver-address@gmail.com"
#        password = "88888"
#        lastname = request.form[('lastname')]
#        message = request.form[('subject')]
#        server = SMTP('smtp.gmail.com', 587)
#        server.starttls()
#
#        server.login(receiver_email, password )
#        server.sendmail(sender_email, receiver_email, 'This is a test email.')
#        print('the message has been successfully sent')
#
#    except Exception as err:
#        print("Something went wrong..", err)
#    finally:
#        server.close()
#
# if __name__ == '__main__':
#    app.run(debug = True)

