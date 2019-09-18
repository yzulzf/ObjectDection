import requests

my=requests.get('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3ij0ZaYKDDw7i24coKygUk1HVWpAtBDkgBsvL6UqBm06M5qNmEA').content

now=open('image\\1.jpg','ab')
now.write(my)
