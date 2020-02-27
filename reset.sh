# rm watchman.dev.db
# python manage.py flush --noinput
psql -U postgres template1 -c 'DROP DATABASE watchman;'
psql -U postgres template1 -c 'CREATE DATABASE watchman;'

cd services
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
cd ..
python manage.py makemigrations
python manage.py migrate
# python manage.py createsuperuser
# Company identificator Sede
echo "Create a CompanyManager 'Sede'"
python manage.py shell -c "from services.manager.models import CompanyManager; CompanyManager(None, 'Sede', './certificates/RODA CONVENIENCIA EM VENDING LTDA  ME22611447000130.pfx', '226114', '22611447000130', 'brunoguimaraes@rodaconveniencia.com.br').save()"
# Users identificator
echo "Create SuperUser 'diegocatalao' from 'Sede' CompanyManager with e-mail 'diegocatalao@rodaconveniencia.com.br'"
python manage.py shell -c "from services.manager.models import User, CompanyManager; User.objects.create_superuser('diegocatalao@rodaconveniencia.com.br', 'catalao123!', company=CompanyManager.objects.all()[0])"
echo "Create SuperUser 'raphaelqueiroz' from 'Sede' CompanyManager with e-mail 'raphaelqueiroz@rodaconveniencia.com.br'"
python manage.py shell -c "from services.manager.models import User, CompanyManager; User.objects.create_superuser('raphaelqueiroz@rodaconveniencia.com.br', '1490Raph@!', company=CompanyManager.objects.all()[0])"
echo "Create SuperUser 'brunoguimaraes' from 'Sede' CompanyManager with e-mail 'brunoguimaraes@rodaconveniencia.com.br'"
python manage.py shell -c "from services.manager.models import User, CompanyManager; User.objects.create_superuser('brunoguimaraes@rodaconveniencia.com.br', 'rodaroda', company=CompanyManager.objects.all()[0])"
echo "Create SuperUser 'ulrichcamposj' from 'Sede' CompanyManager with e-mail 'ulrichcamposj@rodaconveniencia.com.br'"
python manage.py shell -c "from services.manager.models import User, CompanyManager; User.objects.create_superuser('ulrichcamposj@rodaconveniencia.com.br', 'rodaroda', company=CompanyManager.objects.all()[0])"
echo "Create SuperUser 'alessandropacanowski' from 'Sede' CompanyManager with e-mail 'alessandropacanowski@rodaconveniencia.com.br'"
python manage.py shell -c "from services.manager.models import User, CompanyManager; User.objects.create_superuser('alessandropacanowski@rodaconveniencia.com.br', 'rodaroda', company=CompanyManager.objects.all()[0])"
echo "Create SuperUser 'annamedinaceli' from 'Sede' CompanyManager with e-mail 'annamedinaceli@rodaconveniencia.com.br'"
python manage.py shell -c "from services.manager.models import User, CompanyManager; User.objects.create_superuser('annamedinaceli@rodaconveniencia.com.br', 'rodaroda', company=CompanyManager.objects.all()[0])"
echo "Create SuperUser 'karolinanunes' from 'Sede' CompanyManager with e-mail 'karolinanunes@rodaconveniencia.com.br'"
python manage.py shell -c "from services.manager.models import User, CompanyManager; User.objects.create_superuser('karolinanunes@rodaconveniencia.com.br', 'rodaroda', company=CompanyManager.objects.all()[0])"

# Operational users
echo "Create OperationalUser 'operacao' from 'Sede' CompanyManager with e-mail 'operacao@rodaconveniencia.com.br'"
python manage.py shell -c "from services.manager.models import User, CompanyManager; User.objects.create_superuser('operacao@rodaconveniencia.com.br', 'rodaroda', company=CompanyManager.objects.all()[0])"

echo "Create OperationalUser 'comercial' from 'Sede' CompanyManager with e-mail 'comercial@rodaconveniencia.com.br'"
python manage.py shell -c "from services.manager.models import User, CompanyManager; User.objects.create_superuser('comercial@rodaconveniencia.com.br', 'rodaroda', company=CompanyManager.objects.all()[0])"

echo "Create OperationalUser 'desenvolvimento' from 'Sede' CompanyManager with e-mail 'desenvolvimento@rodaconveniencia.com.br'"
python manage.py shell -c "from services.manager.models import User, CompanyManager; User.objects.create_superuser('desenvolvimento@rodaconveniencia.com.br', 'rodaroda', company=CompanyManager.objects.all()[0])"
