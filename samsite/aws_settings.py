import os

AWS_QUERYSTRING_AUTH = False
AWS_ACCESS_KEY_ID = os.environ['AKIAJ3TA6YJVYHVWYHPQ']
AWS_SECRET_ACCESS_KEY = os.environ['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']
AWS_STORAGE_BUCKET_NAME = os.environ['chieffoley-samsite-cards-assets']
MEDIA_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"