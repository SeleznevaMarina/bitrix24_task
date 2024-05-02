from alembic.config import Config
from alembic import command


alembic_ini_path = '/home/marina/projects/bitrix_task/bitrix_webhook_handler/alembic/alembic.ini'
alembic_cfg = Config(alembic_ini_path)
command.upgrade(alembic_cfg, 'head')
