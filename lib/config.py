import os
# SQLAlchemyの設定
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}/001_sample_flask'.format(**{
    'user': os.getenv('DB_USER', 'sample'),
    'password': os.getenv('DB_PASSWORD', 'himitu'),
    'host': os.getenv('DB_HOST', 'localhost:5432'),
})
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'secret_key'