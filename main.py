from http.cookiejar import MozillaCookieJar
import utils.robot as r

def main():
  # name settings & get restaurants
  robot = r.Robot()
  # reccomend
  robot.reccomend_restaurant()
  # ask favorite restaurant
  robot.which_lestrant_do_you_like()


if __name__ == '__main__':
  main()
