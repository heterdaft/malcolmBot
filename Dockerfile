# Install base Python image for Raspberry Pi with arm64v8 (aarch64 -- `uname -m` to get version)
# Bullseye is the OS release version (`cat /etc/os-release`)
FROM arm64v8/python:3.8.18-bullseye

# Copy this project to home directory of the Docker container
COPY src/* ./src/
COPY requirements.txt ./
COPY discord.control ./
COPY discord.proxy ./
COPY facebook.cookies ./
COPY facebook.users ./

# Install all python modules
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Trigger Python script
CMD [ "python", "src/app.py" ]