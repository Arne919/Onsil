# 아래에 코드를 작성하시오.
from conf import settings #NAME, MAIN_URL
from utils import create_url

result = create_url.create_url(settings.NAME, settings.MAIN_URL)
print(result)
