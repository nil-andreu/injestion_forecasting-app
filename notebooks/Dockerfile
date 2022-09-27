FROM ubuntu:latest

LABEL maintainer="nil"

# Run the script sh
# 1. Copy the entrypoint into the image with ADD (add can handle remote url & tar)
ADD docker-entrypoint.sh /

# 2. Change the rights to be able to execute it
RUN chmod u+x /docker-entrypoint.sh

# 3. Run the script to prepare environments
RUN /docker-entrypoint.sh

# Pre-pend the new path
ENV PATH /root/miniconda3/bin:$PATH

# # Create, activate environment (conda init bash initializes conda in bash config) & install packages
# RUN conda create -n environment python=3.8
# RUN conda init bash

# # RUN commands will be using the environment
# # https://pythonspeed.com/articles/activate-conda-dockerfile/
# SHELL ["conda", "run", "-n", "environment", "/bin/bash", "-c"]

# RUN conda install -y jupyter pandas seaborn statsmodels pystan && \
#     conda install -c conda-forge -y fbprophet


# We set which is our workdir and copy the files
WORKDIR /app
COPY * /app/

EXPOSE 8888

# In the case we want an interactive terminal in Python with the environment configured CMD ["ipython"]
CMD ["jupyter", "notebook", "--port=8888", "--ip=0.0.0.0", "--allow-root"]