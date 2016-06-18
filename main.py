# [START app]
from flask import Flask, request
import twilio.twiml
from src import translate

app = Flask(__name__)


@app.route("/", methods=['POST'])
def translate_text_message_and_respond():
    """ A text message should contain a two language codes and a query payload.
    e.g: 'en es How do I pay for my lunch?'
    Then we query the Google translate API and return the response message back
    to the user."""

    body_text = request.values.get('Body', None)
    query_string, source_lang, target_lang = translate.parse_body(body_text)
    translated_text = translate.translate(query_string,
                                          source_lang, target_lang)

    resp = twilio.twiml.Response()
    resp.message(translated_text)

    return str(resp)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
if __name__ == '__main__':
    app.run(debug=True)
