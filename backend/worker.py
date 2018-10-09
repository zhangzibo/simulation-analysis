from celery import Celery
from algorithm import approx

app = Celery(__name__, backend='rpc://', broker='redis://localhost:6379/')

@app.task
def inegrate(*args, **kwargs):
	try:
		return approx(*args, **kwargs)
	except Exception:
		return

# or use integrate = app.task(approx)


# to run redis :
#redis-erver
# $ celery -A worker worker --loglevel= debug

