# hazır python image i alınır docker python verison ile bakılabilir
FROM python:3.10-slim
# update yapmayı sağlar
RUN apt-get update
# geliştirici kitleri uygulamada yer yer ihtiyaç var ondan eklendi (-y her soruya yes anlamı içerir)
RUN apt-get install python3-dev build-essential -y
#pip i upgrade yap
RUN pip install --upgrade pip
# virtual enviroment indir ve kur (docker sistemi linux olduğundan opt içine venv adında virtual enviroment kurduk)
RUN pip install virtualenv && python -m virtualenv /opt/venv
#bizim burada linux da oluşturduğumuz venv e bağlanması için aşağıdaki komut ile patj e erişebiliriz
ENV PATH="/opt/venv/bin:$PATH"
# add ile dizinimizde bulunan bir dosyanın alıp docker daki yerine atıyoruz örnek olarak requirements.txt nin aynısını aldı
ADD ./requirements.txt /tmp/requirements.txt
# şimdi de requirements.txt yi çalıştırmamız lazım
RUN pip install -r /tmp/requirements.txt
# local deki her şeyi ( . işareti her şeyi demek) linux da serv içinde app e kopyala
COPY . /srv/app
# Workdir ile app in içine git
WORKDIR /srv/app
# Dockerfile dosyasında sürekli çalışan şeyler eklenmez örnek olarak runserver sürekli çalışacak
# Kurulum tarzı şeyler çoğunlukla kullanılır
