# MEMIFY APP
## ENGLISH
This small FastAPI application allows you to **post memes** with description, which are then stored in a S3 storage. You can always **delete memes** you don't like, by the way. Next thing you can do is **watch memes, featuring pagination**!
If you made a mistake when posting a meme, you may **update it** if you feel so inclined.

Full list of endpoints:
- GET /memes: Get a list of memes (with pagination).
- GET /memes/{id}: Get a meme specified by ID.
- POST /memes: Add a new meme (with an image and a description).
- PUT /memes/{id}: Update existing meme.
- DELETE /memes/{id}: Delete a meme.

There is also a docker-compose.yml file for you to build and run this app as a container.
However, for this app to work you should first of all create two files: public_api/.env and private_api/.env
public_api/.env:
DATABASE_HOSTNAME=
DATABASE_PORT=
DATABASE_PASSWORD=
DATABASE_NAME=
DATABASE_USERNAME=
AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY=''
BUCKET_NAME=''
ENDPOINT_S3=""
PRIVATE_API_URL="http://127.0.0.1:8000"

private_api/.env:
AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY=''
BUCKET_NAME=""
ENDPOINT_S3=""
You should fill all the blanks with your own information.

Also make sure that you have performed the alembic migrations (alembic upgrade head) and you should be ready to go!

## RUSSIAN
Это небольшое приложение, написанное на FastAPI, позволяет вам **выкладывать мемы** с описанием к ним, которые затем отправляются на хранение в S3 хранилище. Вы всегда сможете **удалить мемы**, которые вам не нравятся, кстати говоря.
Следующее, что вы можете сделать это **смотреть мемы с пагинацией**! Если вы совершили ошибку, пока выкладывали мем, вы можете его **обновить**, если захотите.

Функциональность:
- GET /memes: Получить список всех мемов (с пагинацией).
- GET /memes/{id}: Получить конкретный мем по его ID.
- POST /memes: Добавить новый мем (с картинкой и текстом).
- PUT /memes/{id}: Обновить существующий мем.
- DELETE /memes/{id}: Удалить мем.

Также я добавил docker-compose.yml файл, чтобы вы могли запустить это приложение в контейнере.
Однако для того, чтобы приложение заработало, необходимо создать два файла: public_api/.env and private_api/.env
public_api/.env:
DATABASE_HOSTNAME=
DATABASE_PORT=
DATABASE_PASSWORD=
DATABASE_NAME=
DATABASE_USERNAME=
AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY=''
BUCKET_NAME=''
ENDPOINT_S3=""
PRIVATE_API_URL="http://127.0.0.1:8000"

private_api/.env:
AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY=''
BUCKET_NAME=""
ENDPOINT_S3=""
Заполните все пропуски в файлах своей информацией, а также убедитесь, что вы провели миграции с помощью alembic (alembic upgrade head), и всё готово для дальнейшей работы.
