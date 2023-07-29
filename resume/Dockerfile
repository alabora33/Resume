# hazır python image i alınır docker python verison ile bakılabilir
FROM python:3.10-slim
# update yapmayı sağlar
RUN apt-get update
# geliştirici kitleri uygulamada yer yer ihtiyaç var ondan eklendi (-y her soruya yes anlamı içerir)
RUN apt-get install libpq-dev -y
RUN apt-get install python3-dev build-essential -y
RUN apt-get install postgresql-client -y
# multiprocess işlemlerde gereksiz ve önemsiz pyc uzantılı sadece log gibi görünen dosyaları üretmessini engeller
ENV PYTHONDONTWRITEBYTECODE 1
# değişken üretiyoruz ve bu değişkenin karşılıpğı olan yerlere ekliyoruz venv in olduğu yer ( çok fazla kullanılan parametreler için örnek bir uygulama)
ENV VIRTUAL_ENV=/opt/venv
#pip i upgrade yap
RUN pip install --upgrade pip
# virtual enviroment indir ve kur (docker sistemi linux olduğundan opt içine venv adında virtual enviroment kurduk)
RUN pip install virtualenv && python -m virtualenv $VIRTUAL_ENV
#bizim burada linux da oluşturduğumuz venv e bağlanması için aşağıdaki komut ile patj e erişebiliriz
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
# add ile dizinimizde bulunan bir dosyanın alıp docker daki yerine atıyoruz örnek olarak requirements.txt nin aynısını aldı
ADD ./requirements.txt /tmp/requirements.txt
# şimdi de requirements.txt yi çalıştırmamız lazım
RUN pip install -r /tmp/requirements.txt

COPY entrypoints.sh /srv/entrypoint.sh
RUN sed -i 's/\r$//g' /srv/entrypoint.sh
RUN chmod +x /srv/entrypoint.sh

# local deki her şeyi ( . işareti her şeyi demek) linux da serv içinde app e kopyala
COPY . /srv/app
# Workdir ile app in içine git
WORKDIR /srv/app
# Dockerfile dosyasında sürekli çalışan şeyler eklenmez örnek olarak runserver sürekli çalışacak
# Kurulum tarzı şeyler çoğunlukla kullanılır
ENTRYPOINT ["/srv/entrypoint.sh"]