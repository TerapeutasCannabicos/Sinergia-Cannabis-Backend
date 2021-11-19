from app.extensions import scheduler
from flask.views import MethodView

'''
def task1(id):
    def f():
        with scheduler.app.app_context():
            user = User.query.get(id):
            user.username = 'Vasco'
            user.save()
    return f

class UserDetail(MethodView):
    def patch(self, id):
        ... # código padrão de PATCH
        job = scheduler.add_job(
            func=task1(id),
            trigger=’interval’,
            minutes=5,
            id=’test_job_1’,
            name=’test job 1’,
            replace_existing=True
        )
        return schema.dump(user)
'''

