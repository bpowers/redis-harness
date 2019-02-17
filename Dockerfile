# docker build -t bpowers/mesh-artifact-1-redis .

FROM bpowers/mesh:git-be630c4aeeef2103e4b6357550d02c3469a212df as mesh

FROM ubuntu:18.04 as builder
MAINTAINER Bobby Powers <bobbypowers@gmail.com>

RUN apt-get update && apt-get install -y \
  build-essential \
  git \
  gcc-8 \
  g++-8 \
  python3 \
  sudo \
 && rm -rf /var/lib/apt/lists/* \
 && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 800 --slave /usr/bin/g++ g++ /usr/bin/g++-8 \
 && update-alternatives --install /usr/bin/python python /usr/bin/python3 10 \
 && rm -rf /usr/local/lib/python3.6

COPY --from=mesh /usr/local/lib/libmesh* /usr/local/lib/
RUN ldconfig

WORKDIR /src

COPY . .

RUN ./build


FROM ubuntu:18.04

COPY --from=mesh /usr/local/lib/libmesh* /usr/local/lib/
RUN ldconfig

WORKDIR /src

COPY . .

COPY --from=builder /src/bin /src
