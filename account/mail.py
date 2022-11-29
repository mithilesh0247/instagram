from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException


def sendmail(data):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'
    dict = {"name": "mithilesh", "roll": 101, "college": "IET"}
    print(dict['roll'])

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration))
    subject = "Reset Password Link!"
    sender = {"name": "Tinssle Team", "email": "mithilesh@foreantech.com"}
    replyTo = {"name": "Sendinblue", "email": "contact@sendinblue.com"}
    to = [{"email": data['to'], }]
    html_content = '<html><body><h1>This is your Password Change link dissable in just 5! Minutes!!!</h1><br/><p>' + \
        data['body']+'</p></body></html>'

    params = {"parameter": "My param value", "subject": "New Subject"}
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to, html_content=html_content, sender=sender, subject=subject)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        print(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
