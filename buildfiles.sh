echo "BUILD START"
python 3.11.0 -m pip install -r requirements.txt
python 3.11.o manage.py collectstatic --noinput --clear
echo "BUILD END"