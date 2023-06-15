DB_NOMBRE_DEL_DUMP= ~/Dropbox/Trabajo/APPNAME/backups/app_backup_`date +'%Y%m%d_%Hhs%Mmin'`.dump
DB_DUMP_MAS_RECIENTE=`ls -Art ~/Dropbox/Trabajo/APPNAME/backups/app_*.dump  | tail -n 1`
NOMBRE_BD=bd_name


N=[0m
R=[00;31m
G=[01;32m
Y=[01;33m
B=[01;34m
L=[01;30m

compandos:
	@echo ""
	@echo "${B}COMANDOS DISPONIBLES"
	@echo ""
	@echo "	${G}iniciar${N}: Instalar dependencias"
	@echo "	${G}ejecutar${N}: Correr servidor de pruebas"
	@echo "	${G}crear_migraciones${N}"
	@echo "	${G}migrar${N}"
	@echo "	${G}test${N}"
	@echo "	${G}test_live${N}"
	@echo "	${G}collectstatic${N}"
	@echo "	${G}realizar_backup${N}"
	@echo "	${G}cargar_ultimo_dump${N}"
	@echo "	${G}exportar_backup${N}"
	@echo "	${G}crear_usuario_admin${N}"
	@echo "	${G}version${N}"
	@echo ""

iniciar:
	@pipenv install

ejecutar:
	@pipenv run python manage.py runserver

ejecutar_alt:
	@pipenv run python manage.py runserver 8080

ejecutar_worker:
	@pipenv run python manage.py rqworker

crear_migraciones:
	@pipenv run python manage.py makemigrations

migrar:
	@pipenv run python manage.py migrate --noinput

test:
	@echo "${G}Ejecutando tests ...${N}"
ifeq ($(filtro),)
	pipenv run pytest
else
	pipenv run pytest -k $(filtro)
endif

test_live:
ifeq ($(filtro),)
	pipenv run ptw
else
	pipenv run ptw -- -k $(filtro)
endif

test_ci:
	@echo "${G}Ejecutando tests ...${N}"
	@CI=1 pipenv run pytest

reset:
	dropdb --if-exists ${NOMBRE_BD} -e; createdb ${NOMBRE_BD}
	pipenv run python manage.py migrate --noinput

collectstatic:
	pipenv run python manage.py collectstatic

realizar_backup:
	@echo "Creando el archivo ${DB_NOMBRE_DEL_DUMP}"
	@pg_dump -F c ${NOMBRE_BD} > ${DB_NOMBRE_DEL_DUMP}

cargar_ultimo_dump:
	@echo "Se cargará el dump mas reciente: ${DB_DUMP_MAS_RECIENTE}"
	dropdb --if-exists ${NOMBRE_BD} -e; createdb ${NOMBRE_BD}
	pg_restore --no-acl --no-owner -d ${NOMBRE_BD} ${DB_DUMP_MAS_RECIENTE}
	@make migrar

version:
	@pipenv run bumpversion patch --verbose
	@git push
	@git push --tags

crear_usuario_admin:
	@pipenv run python scripts/create_admin_user.py
