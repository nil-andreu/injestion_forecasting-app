FROM ubuntu:latest

LABEL maintainer="nil"

# Run the script sh
# 1. Copy the entrypoint into the image with ADD (add can handle remote url & tar: https://stackoverflow.com/questions/24958140/what-is-the-difference-between-the-copy-and-add-commands-in-a-dockerfile)
ADD docker-entrypoint.sh /

# 2. Change the rights to be able to execute it
RUN chmod u+x /docker-entrypoint.sh

# 3. Run the script to prepare environments
RUN /docker-entrypoint.sh

# Pre-pend the new path
ENV PATH /root/miniconda3/bin:$PATH

# We set which is our workdir and copy the files
WORKDIR /app
COPY * /app/

EXPOSE 8888

# In the case we want an interactive terminal in Python with the environment configured CMD ["ipython"]
CMD ["jupyter", "notebook", "--port=8888", "--ip=0.0.0.0", "--allow-root"]