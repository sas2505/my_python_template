FROM python:3.10

# Install Bash if not already included
RUN apt-get update && apt-get install -y bash

# Create a non-root user
RUN useradd -m vscode

# Switch to the new user
USER vscode

# Set the working directory
WORKDIR /workspace

# Copy the requirements file
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the default command to run when starting the container
CMD ["bash"] 
