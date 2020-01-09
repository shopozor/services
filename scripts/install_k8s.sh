# Install jq
yum -y install epel-release
yum -y install jq

# Install jx
curl -L "https://github.com/jenkins-x/jx/releases/download/$(curl --silent https://api.github.com/repos/jenkins-x/jx/releases/latest | jq -r '.tag_name')/jx-linux-amd64.tar.gz" | tar xzv "jx"
mv jx /usr/local/bin

# Install git client
GIT_RELEASE=$(curl -s https://api.github.com/repos/git/git/tags | jq -r 'first(.[]).name')
GIT_RELEASE=${GIT_RELEASE#v}
wget https://github.com/git/git/archive/v${GIT_RELEASE}.tar.gz
tar -zxvf v${GIT_RELEASE}.tar.gz
# Install compilation tool
yum -y install curl-devel expat-devel gettext-devel openssl-devel zlib-devel gcc perl-ExtUtils-MakeMaker
yum -y remove git
cd git-${GIT_RELEASE}
make prefix=/usr/local/git all
make prefix=/usr/local/git install

cd ..
rm -rf v${GIT_RELEASE}.tar.gz
rm -rf git-${GIT_RELEASE}

echo "export PATH=\$PATH:/usr/local/git/bin" >> /etc/profile

source /etc/profile

# Setup Jenkins X configuration
