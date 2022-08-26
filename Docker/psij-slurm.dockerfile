FROM slurm-docker-cluster:19.05.1

# RUN pip3 install --upgrade pip
RUN yum install -y gcc openssl-devel bzip2-devel libffi-devel zlib-devel
RUN wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz
RUN tar -xvf Python-3.9.6.tgz
RUN cd Python-3.9.6 ; ./configure --enable-optimizations ; make altinstall
#RUN python3.9 --version 
RUN cd ..
RUN git clone https://github.com/ExaWorks/psi-j-python.git
RUN cd psi-j-python ; pip3.9 install .
