from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pymysql
from django.conf import settings


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        email = data.get('email')
        username = data.get('username')

        if email and username:
            conn = pymysql.connect(
                host=settings.DATABASES['default']['HOST'],
                database=settings.DATABASES['default']['NAME'],
                charset='utf8mb4',
                user=settings.DATABASES['default']['USER'],
                cursorclass=pymysql.cursors.DictCursor,
                password=settings.DATABASES['default']['PASSWORD'],
            )

            cursor = conn.cursor()
            try:
                sql = "select * from auth_user where email='%s' and username = '%s'" % (
                    email, username)
                cursor.execute(sql)

                # defense sql injection
                # sql = "select * from auth_user where email=%s"
                # cursor.execute(sql, (email))

                conn.commit()
                result = cursor.fetchone()

                cursor.close()
                conn.close()

                if result is not None:
                    return JsonResponse({
                        'status': 0,
                        'message': 'login successfully',
                        'sql': sql
                    })
                else:
                    return JsonResponse({
                        'status': 1,
                        'message': 'login failed',
                        'sql': sql
                    }, status=422)
            except Exception as e:
                return JsonResponse({
                    'status': 1,
                    'sql': sql,
                    'message': str(e)
                }, status=500)

        return JsonResponse({
            'status': 1,
            'message': 'input error'
        }, status=422)

    return JsonResponse({
        'status': 1,
        'message': 'method not allowed'
    }, status=405)
