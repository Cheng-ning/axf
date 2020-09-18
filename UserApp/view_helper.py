from django.core.mail import send_mail
from django.template import loader


def sendEmail(username, email, token):
    index = loader.get_template('axf/user/register/active.html')
    context = {
        'name':username,
        'url': 'http://106.53.229.53:8000/axfuser/account/?token='+str(token)
    }
    index_value = index.render(context)
    subject = '邮箱验证'
    html_message = index_value
    from_email = 'm17862726221@163.com'
    recipient_list = [email]

    send_mail(subject=subject, message='', html_message=html_message, from_email=from_email, recipient_list=recipient_list)