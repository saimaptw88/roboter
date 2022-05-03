import csv


class Robot(object):

  filename = 'data/restaurants.csv'

  def __init__(self):
    print('こんにちは! 私はRobokoです。あなたの名前はなんですか？')
    self._name = input('>>')
    with open(self.filename, 'r') as csv_file:
      reader = csv.DictReader(csv_file)
      restaurants = {}
      for row in reader:
        restaurants[row['RestaurantName']] = row['Count']
      self._restaurants = dict(sorted(restaurants.items(), reverse=True))

  @property
  def name(self):
    return self._name

  @property
  def restaurants(self):
    return self._restaurants

  def reccomend_restaurant(self):
    if len(self._restaurants) == 0:
      return
    for restaurant in self._restaurants.keys():
      print('私のオススメのレストランは、{}です。\nこのレストランは好きですか? [Yes/No]'.format(restaurant))
      res = ''
      while(True):
        res = input('>>').capitalize()
        if(res == 'Yes' or res == 'No'):
          break
      if res == 'Yes':
        break
  def which_lestrant_do_you_like(self):
    print('{}さん。どこのレストランが好きですか？'.format(self.name))
    res = input('>>').capitalize()
    if res in self._restaurants:
      count = int(self._restaurants[res])
      self._restaurants[res] = str(count + 1)
    else:
      self._restaurants[res] = '1'
    with open(self.filename, 'w') as csv_file:
      fieldname = ['RestaurantName', 'Count']
      writer = csv.DictWriter(csv_file, fieldnames=fieldname)
      writer.writeheader()
      for k, v in self._restaurants.items():
        writer.writerow({'RestaurantName': k, 'Count': v})
  def __del__(self):
    print('{}さん。ありがとうございました。\n良い1日を!さようなら。'.format(self.name))
