# The format_date() function expects to receive a datetime object and then use the strftime() method to convert it to a string. 
def format_date(date):
  return date.strftime('%m/%d/%y')


def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]


def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word


