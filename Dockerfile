FROM centos:latest
RUN yum install java-11-openjdk.x86_64 -y
RUN yum install wget -y
RUN yum install python3 -y
COPY mail.py /
RUN yum install git -y
RUN wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat/jenkins.repo
RUN rpm --import https://pkg.jenkins.io/redhat/jenkins.io.key
RUN yum install jenkins -y
RUN echo "jenkins 	ALL=(ALL) 	NOPASSWD: ALL">>/etc/sudoers
RUN yum install openssh-server -y
CMD java -jar /usr/lib/jenkins/jenkins.war
EXPOSE 8080