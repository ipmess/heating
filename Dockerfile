# Use a slim Debian image
FROM python:3.13-slim

# Create a working directory
WORKDIR /app

# Copy the project directory to the container
COPY . .

ENV VIRTUAL_ENV=/app/venv

# Create a virtual environment
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install project dependencies inside the virtual environment
RUN pip3 install -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Run gunicorn command
CMD ["gunicorn","--config", "gunicorn_config.py", "app:app"]