from flask import render_template
from . import *
from flask import make_response


def render_thankyou(message, status_code=200, language='en'):
    template = render_template('thankyou.html', langs=langs, language=language, side_menu=side_menu, header=header,
                               lang_label=lang_label, message=message), status_code
    return add_header(template)


def add_header(template):
    r = make_response(template)
    r.headers['Content-Security-Policy'] = ("default-src"
                                            " 'self';"
                                            " style-src-elem"
                                            " https://fonts.googleapis.com"
                                            " 'self'"
                                            ' sha256-7Amc3B9rHQY0hLlWqTQEKs3q3QvhryqpcXMCm6Q7/3Y='  # Hebrew/German inline style
                                            " 'sha256-rsDlNwegAx9dRLCXhm/zQTlHSR5EIkX8zXrhFMJIq1M='"  # Hebrew/German inline style
                                            " 'sha256-7Amc3B9rHQY0hLlWqTQEKs3q3QvhryqpcXMCm6Q7/3Y=';" #Hebrew
                                            " script-src-elem"
                                            " 'self'"
                                            " https://cdnjs.cloudflare.com/ajax/libs/knockout/3.5.0/knockout-min.js"
                                            " https://www.google-analytics.com;"
                                            " font-src"
                                            " https://fonts.gstatic.com;"
                                            " frame-src"
                                            " https://www.google.com/;")

    return r


def render_page(template, data=None, on_expertise=False, language='en', description=None):
    page_template = render_template(template, on_expertise=on_expertise, langs=langs, data=data, language=language,
                                    side_menu=side_menu, header=header, lang_label=lang_label, description=description)
    return add_header(page_template)


# def render_contact(form, title, name, email, text, submit, language='en'):
#     template = render_template('contact.html', form=form, title=title, name=name, email=email, text=text, submit=submit,
#                                langs=langs, data=contact_info, language=language, on_contact=True, side_menu=side_menu,
#                                header=header, lang_label=lang_label)
#     return add_header(template)
